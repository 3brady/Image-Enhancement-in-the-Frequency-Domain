"""
Owner: 7 (Homomorphic filter). Fixes uneven lighting and keeps details.

What to implement (steps from the lecture):
1. ln(image + 1)  (use float, avoid log(0))
2. DFT (frequency.to_frequency)
3. Multiply by a mask: gamma_low (< 1) for low frequencies (lighting), gamma_high (> 1) for high frequencies (details). Use a two-level Ideal mask based on cutoff. The lecture gives no formula, so this is our choice.
4. IDFT (frequency.to_spatial logic, but keep float before the exp)
5. exp(result) - 1, then normalize to 0..255 uint8

Signature: homomorphic(gray, cutoff=30, gamma_low=0.5, gamma_high=2.0)

Done when: an unevenly lit image looks more balanced and details are clearer.
Depends on: frequency.py (owner 3). Used by: methods.py, compare.py.
"""
import frequency


def homomorphic(gray, cutoff=30, gamma_low=0.5, gamma_high=2.0):
    ...
