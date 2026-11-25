"""
Owner: 4 (Low-Pass filter). Smooths the image and reduces noise.

What to implement:
- ideal_lowpass_mask(shape, cutoff): mask = 1 where D(u,v) <= cutoff, else 0. Use frequency.distance_grid. (Formula: Chapter-3 lecture, Ideal Low-Pass.)
- lowpass(gray, cutoff=30): return frequency.apply_mask(gray, mask).

Done when: lowpass(img, 30) is visibly blurred, and a smaller cutoff blurs more.
Depends on: frequency.py (owner 3). Used by: methods.py, compare.py.
"""
import frequency


def ideal_lowpass_mask(shape, cutoff):
    ...


def lowpass(gray, cutoff=30):
    ...
