"""
Owner: 3 (DFT engine). Everyone else depends on this file, so finish it FIRST.

What to implement:
- to_frequency(gray): float32 -> cv2.dft(flags=cv2.DFT_COMPLEX_OUTPUT) -> np.fft.fftshift, so low frequencies are in the center. Return the shifted complex array (H, W, 2).
- to_spatial(F_shifted): ifftshift -> cv2.idft(flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT) -> clip to 0..255 -> uint8.
- distance_grid(shape): array (H, W) with each pixel's distance D(u,v) from the center. All Ideal masks use it.
- apply_mask(gray, mask): to_frequency, multiply by mask (mask shape (H, W), apply to both channels), to_spatial.

Done when: apply_mask(img, np.ones(img.shape)) returns the same image as the input.
Used by: lowpass.py, highpass.py, bandpass.py, homomorphic.py.
"""

def to_frequency(gray):
    ...


def to_spatial(F_shifted):
    ...


def distance_grid(shape):
    ...


def apply_mask(gray, mask):
    ...
