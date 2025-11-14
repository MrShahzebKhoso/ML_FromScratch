import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.atleast_1d(x).astype(float)

    tanh_x = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


    return np.asarray(tanh_x, dtype=float)

    