"""
Owner: 9 (Comparison, images/ and results/).

What to implement:
- Put 3 to 5 test images in images/ (one noisy, one unevenly lit, one low contrast, one with clear edges).
- run_comparisons(gray): for each (freq_name, spatial_name) in methods.PAIRS, run both and return a dict {pair: (freq_result, spatial_result)}.
- save_all(): loop over images/, save original + both results side by side into results/ (cv2.hconcat + cv2.imwrite), one file per pair per image.
- Write 2 to 3 lines per pair about the visible difference, and send them to owner 10 for the report.

Pairs (from Chapter-3): Low-Pass vs Averaging, High-Pass vs Laplacian, Homomorphic vs Histogram Equalization, and Band-Pass vs DoG (Lecture 2).
Depends on: methods.py (owner 1). Run with `python compare.py`.
"""

def run_comparisons(gray):
    ...

def save_all(images_dir="images", results_dir="results"):
    ...


if __name__ == "__main__":
    save_all()
