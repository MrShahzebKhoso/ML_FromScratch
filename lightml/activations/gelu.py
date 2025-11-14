import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: scalar, list, or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    x = np.asarray(x)

    erf =  np.vectorize(math.erf)(x / np.sqrt(2.))

    GELU = (1./2.) * x * (1 + erf)

    return GELU