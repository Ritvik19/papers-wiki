#!/usr/bin/env python3
"""Prune duplicate raw images, orphan assets, and compress wiki figures."""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required: python3 -m pip install Pillow") from exc

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
ASSETS = WIKI / "assets"
RAW = ROOT / "raw"
ARTIFACTS = ROOT / "artifacts"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
ASSET_REF_RE = re.compile(
    r"(?:wiki/)?assets/([^)\s\"']+)|\.\./assets/([^)\s\"']+)"
)
IMG_SRC_RE = re.compile(r'src=["\'](images/[^"\']+)["\']', re.IGNORECASE)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for base in (WIKI, ARTIFACTS, RAW):
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.suffix.lower() in {".md", ".html", ".js", ".json"}:
                if "assets" in path.parts and base == WIKI:
                    continue
                files.append(path)
    return files


def collect_referenced_assets() -> set[str]:
    refs: set[str] = set()
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for m in ASSET_REF_RE.findall(text):
            rel = next(part for part in m if part)
            refs.add(rel.strip())
    return refs


def rewrite_raw_html_image_paths() -> int:
    updated = 0
    for html_path in RAW.rglob("full-article.html"):
        slug = html_path.parent.name
        text = html_path.read_text(encoding="utf-8", errors="ignore")
        new_text = IMG_SRC_RE.sub(
            lambda m: f'src="../../wiki/assets/{slug}/{Path(m.group(1)).name}"',
            text,
        )
        if new_text != text:
            html_path.write_text(new_text, encoding="utf-8")
            updated += 1
    return updated


def dedupe_raw_images(dry_run: bool) -> tuple[int, int, list[str]]:
    removed_files = 0
    removed_bytes = 0
    warnings: list[str] = []

    for images_dir in sorted(RAW.glob("*/images")):
        if not images_dir.is_dir():
            continue
        slug = images_dir.parent.name
        asset_dir = ASSETS / slug
        asset_dir.mkdir(parents=True, exist_ok=True)

        for image_path in sorted(images_dir.iterdir()):
            if not image_path.is_file():
                continue
            if image_path.suffix.lower() not in IMAGE_EXTS:
                continue
            target = asset_dir / image_path.name
            if not target.exists():
                if dry_run:
                    warnings.append(f"would copy missing twin: {image_path} -> {target}")
                else:
                    shutil.copy2(image_path, target)
            elif image_path.read_bytes() != target.read_bytes():
                warnings.append(f"content mismatch: {image_path} vs {target}")

            size = image_path.stat().st_size
            if dry_run:
                removed_files += 1
                removed_bytes += size
            else:
                image_path.unlink()
                removed_files += 1
                removed_bytes += size

        if not dry_run and images_dir.exists() and not any(images_dir.iterdir()):
            images_dir.rmdir()

    return removed_files, removed_bytes, warnings


def delete_orphan_assets(refs: set[str], dry_run: bool) -> tuple[int, int]:
    removed_files = 0
    removed_bytes = 0
    if not ASSETS.exists():
        return removed_files, removed_bytes

    for asset_path in sorted(ASSETS.rglob("*")):
        if not asset_path.is_file():
            continue
        rel = asset_path.relative_to(ASSETS).as_posix()
        if rel in refs:
            continue
        size = asset_path.stat().st_size
        if dry_run:
            removed_files += 1
            removed_bytes += size
            continue
        asset_path.unlink()
        removed_files += 1
        removed_bytes += size

    if not dry_run:
        for folder in sorted(ASSETS.rglob("*"), reverse=True):
            if folder.is_dir() and not any(folder.iterdir()):
                folder.rmdir()
    return removed_files, removed_bytes


def _save_image(img: Image.Image, path: Path, ext: str) -> None:
    ext = ext.lower()
    if ext in {".jpg", ".jpeg"}:
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")
        img.save(path, format="JPEG", quality=82, optimize=True)
    elif ext == ".webp":
        img.save(path, format="WEBP", quality=82, method=6)
    elif ext == ".png":
        img.save(path, format="PNG", optimize=True)
    elif ext == ".gif":
        img.save(path, format="GIF", optimize=True)
    else:
        img.save(path)


def compress_assets(dry_run: bool, max_edge: int = 1600, max_bytes: int = 500_000) -> tuple[int, int, int]:
    compressed_files = 0
    before_bytes = 0
    after_bytes = 0
    if not ASSETS.exists():
        return compressed_files, before_bytes, after_bytes

    for path in sorted(ASSETS.rglob("*")):
        ext = path.suffix.lower()
        if ext not in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
            continue
        size = path.stat().st_size
        needs_resize = False
        try:
            with Image.open(path) as img:
                w, h = img.size
                needs_resize = max(w, h) > max_edge
        except OSError:
            continue
        if size <= max_bytes and not needs_resize:
            continue

        before_bytes += size
        if dry_run:
            compressed_files += 1
            after_bytes += min(size, max_bytes)
            continue

        with Image.open(path) as img:
            if needs_resize:
                img.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
            if ext == ".gif":
                frames = []
                try:
                    while True:
                        frame = img.copy()
                        if max(frame.size) > max_edge:
                            frame.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
                        frames.append(frame.convert("P", palette=Image.Palette.ADAPTIVE))
                        img.seek(img.tell() + 1)
                except EOFError:
                    pass
                if frames:
                    frames[0].save(
                        path,
                        save_all=True,
                        append_images=frames[1:],
                        optimize=True,
                        loop=img.info.get("loop", 0),
                        duration=img.info.get("duration", 100),
                    )
                else:
                    _save_image(img, path, ext)
            else:
                _save_image(img, path, ext)

        new_size = path.stat().st_size
        after_bytes += new_size
        compressed_files += 1

    return compressed_files, before_bytes, after_bytes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-compress", action="store_true")
    parser.add_argument("--skip-dedupe", action="store_true")
    parser.add_argument("--skip-orphans", action="store_true")
    args = parser.parse_args()

    print(f"Root: {ROOT}")
    if args.dry_run:
        print("DRY RUN — no files will be modified\n")

    if not args.skip_dedupe:
        html_updates = 0 if args.dry_run else rewrite_raw_html_image_paths()
        removed_files, removed_bytes, warnings = dedupe_raw_images(args.dry_run)
        print(f"Raw image dedupe: {removed_files} files, {removed_bytes / 1e6:.1f} MB")
        if html_updates:
            print(f"Updated {html_updates} full-article.html files")
        for warning in warnings[:20]:
            print(f"  warning: {warning}")
        if len(warnings) > 20:
            print(f"  ... {len(warnings) - 20} more warnings")

    refs = collect_referenced_assets()
    print(f"Referenced asset paths: {len(refs)}")

    if not args.skip_orphans:
        orphan_files, orphan_bytes = delete_orphan_assets(refs, args.dry_run)
        print(f"Orphan assets removed: {orphan_files} files, {orphan_bytes / 1e6:.1f} MB")

    if not args.skip_compress:
        compressed, before, after = compress_assets(args.dry_run)
        saved = before - after
        print(
            f"Compressed assets: {compressed} files, "
            f"{before / 1e6:.1f} MB -> {after / 1e6:.1f} MB "
            f"(saved {saved / 1e6:.1f} MB)"
        )


if __name__ == "__main__":
    main()
