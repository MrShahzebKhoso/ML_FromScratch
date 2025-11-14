import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x = np.asarray(x, float)
    alpha = np.asarray(alpha, float)
    fx = np.where(x >= 0, x, alpha * x)
    return fx