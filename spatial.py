"""
Owner: 8 (Spatial-domain filters). These are the comparison side: same goals, done directly on pixels.

What to implement (OpenCV is fine):
- histogram_equalization(gray): cv2.equalizeHist
- averaging(gray, k=5): cv2.blur with a k x k kernel  (compare with Low-Pass)
- laplacian(gray): cv2.Laplacian, then sharpen (gray - laplacian) and clip to uint8  (compare with High-Pass)
- dog(gray, sigma1=1.0, sigma2=2.0): difference of two GaussianBlur results, normalized to uint8  (compare with Band-Pass, Lecture 2)

Every function takes a grayscale uint8 image and returns grayscale uint8 of the same size.
Does not depend on other files. Used by: methods.py, compare.py.
"""

def histogram_equalization(gray):
    ...


def averaging(gray, k=5):
    ...


def laplacian(gray):
    ...


def dog(gray, sigma1=1.0, sigma2=2.0):
    ...
