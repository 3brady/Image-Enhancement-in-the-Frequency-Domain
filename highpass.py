"""
Owner: 5 (High-Pass filter). Sharpens and highlights edges.

What to implement:
- ideal_highpass_mask(shape, cutoff): mask = 0 where D(u,v) <= cutoff, else 1. (Same as 1 - lowpass mask.)
- highpass(gray, cutoff=30): return frequency.apply_mask(gray, mask).

Done when: highpass(img, 30) shows mostly edges and fine details.
Depends on: frequency.py (owner 3). Used by: methods.py, compare.py.
"""
import frequency


def ideal_highpass_mask(shape, cutoff):
    ...


def highpass(gray, cutoff=30):
    ...
