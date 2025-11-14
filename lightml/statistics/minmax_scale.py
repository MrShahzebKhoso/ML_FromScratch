import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    #min - max + eps
    x = np.asarray(X, float)
    if x.ndim==1:
        x_min = np.min(x)
        x_max = np.max(x)
        x_new = (x - x_min)/ np.maximum(x_max - x_min, eps)
        return x_new

    if x.ndim==2:
        x_min = np.min(x, axis = axis, keepdims=True)
        x_max = np.max(x, axis = axis, keepdims=True)
        x_new = (x - x_min)/ np.maximum(x_max - x_min, eps)
        return x_new

