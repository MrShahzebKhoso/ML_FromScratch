import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    x = np.asarray(x, float)
    y = np.asarray(y, float)

    L1 = np.sum(np.abs(x-y))

    return float(L1)