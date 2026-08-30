# Papers wiki artifact scaffold

Copy this folder to create a new artifact with the standard Papers wiki look.

## Quick start

1. Copy:

   `artifacts/_scaffold/papers-wiki/` → `artifacts/<YYYY-MM-DD>-<slug>/`

2. Edit `index.html`:

- Replace the `{{PLACEHOLDER}}` tokens (title, subtitle, bullets, sources).
- Put images in `figures/` and reference them.

3. Optional (recommended): add a small `build_figures.py` in the artifact folder to
   generate `figures/*.png` from the paper PDF (PyMuPDF clips), like the
   Gym-Anything artifact does.

