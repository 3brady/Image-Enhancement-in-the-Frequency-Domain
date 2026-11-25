# Project 6: Image Enhancement in the Frequency Domain

Python + OpenCV (cv2.dft / cv2.idft), Tkinter GUI, Pillow only to show images in Tkinter.

Setup: `pip install -r requirements.txt` then `python main.py`

| File | Owner |
|---|---|
| main.py, methods.py | 1. Integration lead |
| gui.py | 2. GUI |
| frequency.py | 3. DFT engine |
| lowpass.py | 4. Low-Pass |
| highpass.py | 5. High-Pass |
| bandpass.py | 6. Band-Pass |
| homomorphic.py | 7. Homomorphic |
| spatial.py | 8. Spatial filters |
| compare.py, images/, results/ | 9. Comparison |
| report/ | 10. Report and slides |

Rules: every filter takes a grayscale uint8 image and returns a grayscale uint8 image of the same size. Only edit your own file. Ask the owner of frequency.py if you need something from it.
