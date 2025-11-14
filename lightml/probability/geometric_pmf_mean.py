import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """

    pmf = [(p* (1-p)**(ki-1)) for ki in k]

    pmf = np.asarray(pmf, dtype=float)

    mean = (1./p)

    return pmf, mean