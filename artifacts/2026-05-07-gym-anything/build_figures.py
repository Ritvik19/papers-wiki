#!/usr/bin/env python3
"""Crop Gym-Anything figures from the arXiv PDF (exact embedded image bounds).

Requires PyMuPDF (`import fitz`). PDF path:
  raw/2604.06126_Gym-Anything.pdf

Outputs PNGs under figures/ for the interactive artifact.
"""

from __future__ import annotations

from pathlib import Path

import fitz

REPO = Path(__file__).resolve().parents[2]
PDF_CANDIDATES = (
    REPO / "raw/2026-05-07_Gym-Anything-Turn-any-Software-into-an-Agent-Environment.pdf",
    REPO / "raw/2604.06126_Gym-Anything.pdf",
)
OUT = Path(__file__).resolve().parent / "figures"


def resolve_pdf() -> Path:
    for p in PDF_CANDIDATES:
        if p.is_file():
            return p
    return PDF_CANDIDATES[0]

# Page indices are 0-based (PyMuPDF). Figure 2 caption is on PDF viewer page 3 → index 2.
PAGE_FIG2 = 2
PAGE_FIG3 = 3


def largest_image_rect(page: fitz.Page) -> fitz.Rect | None:
    """Return the union of image placements on the page (single full-width figure)."""
    rects: list[fitz.Rect] = []
    for img in page.get_images(full=True):
        xref = img[0]
        rects.extend(page.get_image_rects(xref))
    if not rects:
        return None
    # Paper pages here use one main diagram image per figure page.
    r0 = rects[0]
    for r in rects[1:]:
        r0 |= r
    return r0


def subdivide_grid(fig_rect: fitz.Rect, pad_pt: float = 1.5) -> tuple[fitz.Rect, fitz.Rect]:
    """Figure 2 layout: TL=P1, TR=P2, BL=P4, BR=P3 → return Phase 2 (TR) and Phase 4 (BL)."""
    x0, y0, x1, y1 = fig_rect
    mx = (x0 + x1) / 2
    my = (y0 + y1) / 2
    p = pad_pt
    phase2 = fitz.Rect(mx + p, y0 + p, x1 - p, my - p)
    phase4 = fitz.Rect(x0 + p, my + p, mx - p, y1 - p)
    return phase2, phase4


def render_clip(page: fitz.Page, clip: fitz.Rect, zoom: float, out_path: Path) -> None:
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=clip, alpha=False)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pix.save(out_path.as_posix())


def main() -> None:
    pdf = resolve_pdf()
    if not pdf.is_file():
        dest = PDF_CANDIDATES[-1]
        raise SystemExit(
            f"Missing PDF. Save the paper as one of:\n"
            f"  {PDF_CANDIDATES[0]}\n  {dest}\n"
            f"Example: curl -fsSL -o {dest} https://arxiv.org/pdf/2604.06126.pdf"
        )

    doc = fitz.open(pdf.as_posix())
    page2 = doc[PAGE_FIG2]
    page3 = doc[PAGE_FIG3]

    fig2_rect = largest_image_rect(page2)
    fig3_rect = largest_image_rect(page3)
    if fig2_rect is None or fig3_rect is None:
        raise SystemExit("Could not locate embedded figure images on expected pages.")

    phase2_rect, phase4_rect = subdivide_grid(fig2_rect)

    zoom = 4.0

    render_clip(page2, fig2_rect, zoom, OUT / "overview-pipeline-crop.png")
    render_clip(page3, fig3_rect, zoom, OUT / "software-selection-crop.png")
    render_clip(page2, phase2_rect, zoom, OUT / "creation-audit-phase2.png")
    render_clip(page2, phase4_rect, zoom, OUT / "verification-phase4.png")

    doc.close()

    print("PDF figure clips (PDF points):")
    print("  Figure 2 image:", fig2_rect)
    print("  Phase 2 (TR):", phase2_rect)
    print("  Phase 4 (BL):", phase4_rect)
    print("  Figure 3 image:", fig3_rect)
    print(f"Source PDF: {pdf}")
    print(f"Zoom {zoom}x → artifacts in {OUT}/")


if __name__ == "__main__":
    main()
