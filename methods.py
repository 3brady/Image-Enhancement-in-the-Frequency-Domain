import lowpass
import highpass
import bandpass
import homomorphic
import spatial

# should re check on it after all of them push their code

METHODS = {
    "Low-Pass": lowpass.lowpass,
    "High-Pass": highpass.highpass,
    "Band-Pass": bandpass.bandpass,
    "Homomorphic": homomorphic.homomorphic,
    "Histogram Equalization": spatial.histogram_equalization,
    "Averaging": spatial.averaging,
    "Laplacian": spatial.laplacian,
    "DoG": spatial.dog,
}

PAIRS = [
    ("Low-Pass", "Averaging"),
    ("High-Pass", "Laplacian"),
    ("Band-Pass", "DoG"),
    ("Homomorphic", "Histogram Equalization"),
]
