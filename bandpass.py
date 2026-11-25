"""
Owner: 6 (Band-Pass filter). Keeps only a ring of frequencies between two radii.

What to implement:
- ideal_bandpass_mask(shape, r_low, r_high): mask = 1 where r_low <= D(u,v) <= r_high, else 0. (The lecture slide has the title only, no formula, so we use this ring.)
- bandpass(gray, r_low=20, r_high=60): return frequency.apply_mask(gray, mask).

Done when: the result shows medium details, without the smooth areas and without the finest noise.
Depends on: frequency.py (owner 3). Used by: methods.py, compare.py.
"""

import frequency

def ideal_bandpass_mask(shape, r_low, r_high):
    ...


def bandpass(gray, r_low=20, r_high=60):
    ...
