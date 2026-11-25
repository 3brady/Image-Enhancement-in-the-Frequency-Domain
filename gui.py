"""
Owner: 2 (GUI, Tkinter). Pillow is used only to show images.

What to implement:
- run_app(methods): open a Tkinter window. `methods` is a dict {name: function}; call function(gray_image) to get the result.
- Load image button (file dialog) -> cv2.imread(path, cv2.IMREAD_GRAYSCALE).
- Dropdown (or buttons) to pick the filter from methods.keys().
- Show original and result side by side (convert numpy -> PIL.Image.fromarray -> ImageTk.PhotoImage).
- Save result button (cv2.imwrite into results/).
- Optional: slider for the cutoff value.

Done when: you can load an image, pick any filter, and see the result. You can test with fake filters before the others finish.
Used by: main.py.
"""

def run_app(methods):
    ...
