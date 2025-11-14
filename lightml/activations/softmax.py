import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """

    x = np.asarray(x, float)

    if x.ndim ==1:
        x_max = np.max(x)
        x_sub = x - x_max
        soft_x = (np.exp(x_sub)) / (np.sum(np.exp(x_sub)))
        return soft_x

    if x.ndim ==2:
        x = np.asarray(x, float)
        x_max = np.max(x, axis=1, keepdims=True)
        x_sub = x - x_max
        soft_x = (np.exp(x_sub)) / (np.sum(np.exp(x_sub), axis=1, keepdims=True))
        return soft_x

    return 0.