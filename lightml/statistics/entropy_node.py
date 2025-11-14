import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    y = np.asarray(y)

    cls,counts = np.unique(y, return_counts=True)
    n = len(y)

    p = counts/n
    HS = - np.sum(p * np.log2(p))


    return HS