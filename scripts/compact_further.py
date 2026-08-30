#!/usr/bin/env python3
"""Further compaction: WebP conversion and markdown-only raw sources."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
from html.parser import HTMLParser
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:
    raise SystemExit("Pillow required: python3 -m pip install Pillow") from exc

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
ASSETS = WIKI / "assets"
RAW = ROOT / "raw"
ARTIFACTS = ROOT / "artifacts"

CONVERT_EXTS = {".png", ".jpg", ".jpeg"}
TEXT_SUFFIXES = {".md", ".html", ".js", ".json"}


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []
        self._skip = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip = True
        if tag in {"p", "div", "br", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr"}:
            self._chunks.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip = False
        if tag in {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "table"}:
            self._chunks.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip:
            self._chunks.append(data)

    def text(self) -> str:
        out = "".join(self._chunks)
        out = re.sub(r"\n{3,}", "\n\n", out)
        return out.strip()


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for base in (WIKI, ARTIFACTS, RAW, ROOT):
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if "assets" in path.parts and base == WIKI:
                continue
            if path.name in {"index.md", "log.md", "AGENTS.md", "README.md", "purpose.md"}:
                files.append(path)
            elif base in (WIKI, ARTIFACTS, RAW):
                files.append(path)
    return files


def convert_to_webp(
    dry_run: bool,
    max_edge: int = 1600,
    quality: int = 80,
) -> tuple[int, int, int, dict[str, str]]:
    mapping: dict[str, str] = {}
    converted = 0
    before = 0
    after = 0

    if not ASSETS.exists():
        return converted, before, after, mapping

    for src in sorted(ASSETS.rglob("*")):
        if src.suffix.lower() not in CONVERT_EXTS:
            continue
        dst = src.with_suffix(".webp")
        rel_old = src.relative_to(ASSETS).as_posix()
        rel_new = dst.relative_to(ASSETS).as_posix()
        size = src.stat().st_size
        before += size

        if dry_run:
            mapping[rel_old] = rel_new
            converted += 1
            after += max(size // 3, 50_000)
            continue

        try:
            with Image.open(src) as img:
                if max(img.size) > max_edge:
                    img = img.copy()
                    img.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
                if img.mode in ("RGBA", "LA"):
                    img.save(dst, format="WEBP", quality=quality, method=6)
                elif img.mode == "P" and "transparency" in img.info:
                    img = img.convert("RGBA")
                    img.save(dst, format="WEBP", quality=quality, method=6)
                else:
                    if img.mode not in ("RGB", "L"):
                        img = img.convert("RGB")
                    img.save(dst, format="WEBP", quality=quality, method=6)
        except OSError as exc:
            print(f"  skip {rel_old}: {exc}")
            after += size
            continue

        after += dst.stat().st_size
        mapping[rel_old] = rel_new
        src.unlink()
        converted += 1

    return converted, before, after, mapping


def rewrite_asset_refs(mapping: dict[str, str], dry_run: bool) -> int:
    if not mapping:
        return 0
  # longest paths first to avoid partial replacements
    replacements = sorted(mapping.items(), key=lambda kv: len(kv[0]), reverse=True)
    updated = 0
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        new_text = text
        for old, new in replacements:
            new_text = new_text.replace(old, new)
        if new_text != text:
            updated += 1
            if not dry_run:
                path.write_text(new_text, encoding="utf-8")
    return updated


def html_to_markdown(html_path: Path) -> str:
    if shutil.which("pandoc"):
        result = subprocess.run(
            ["pandoc", "-f", "html", "-t", "markdown", str(html_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()

    parser = _TextExtractor()
    parser.feed(html_path.read_text(encoding="utf-8", errors="ignore"))
    body = parser.text()
    title = html_path.stem
    title_match = re.search(r"<title[^>]*>(.*?)</title>", html_path.read_text(encoding="utf-8", errors="ignore"), re.I | re.S)
    if title_match:
        title = re.sub(r"\s+", " ", title_match.group(1)).strip()
    return f"# {title}\n\n{body}\n"


def migrate_raw_to_markdown_only(dry_run: bool) -> tuple[int, int, int]:
    converted = 0
    deleted_html = 0
    updated_sources = 0

    html_files = sorted(RAW.rglob("*.html"))
    for html_path in html_files:
        md_path = html_path.with_suffix(".md")
        if html_path.name == "full-article.html":
            md_path = html_path.parent / "full-article.md"

        if not md_path.exists():
            if dry_run:
                converted += 1
            else:
                md_path.write_text(html_to_markdown(html_path), encoding="utf-8")
                converted += 1

        if dry_run:
            deleted_html += 1
        else:
            html_path.unlink()
            deleted_html += 1

    html_ref_re = re.compile(r"(raw/[^\s`\"']+)\.html")
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        new_text = html_ref_re.sub(r"\1.md", text)
        new_text = new_text.replace("full-article.html", "full-article.md")
        if new_text != text:
            updated_sources += 1
            if not dry_run:
                path.write_text(new_text, encoding="utf-8")

    if not dry_run:
        for folder in sorted(RAW.rglob("*"), reverse=True):
            if folder.is_dir() and not any(folder.iterdir()):
                folder.rmdir()

    return converted, deleted_html, updated_sources


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--webp-only", action="store_true")
    parser.add_argument("--markdown-only", action="store_true")
    args = parser.parse_args()

    if not args.markdown_only:
        converted, before, after, mapping = convert_to_webp(args.dry_run)
        refs = rewrite_asset_refs(mapping, args.dry_run)
        print(
            f"WebP: {converted} files, {before/1e6:.1f} MB -> {after/1e6:.1f} MB "
            f"(saved {(before-after)/1e6:.1f} MB); {refs} text files updated"
        )

    if not args.webp_only:
        converted, deleted, sources = migrate_raw_to_markdown_only(args.dry_run)
        print(
            f"Markdown-only raw: converted {converted} html->md, "
            f"deleted {deleted} html files, updated {sources} source refs"
        )


if __name__ == "__main__":
    main()
