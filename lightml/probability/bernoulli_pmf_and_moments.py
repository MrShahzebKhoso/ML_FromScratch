import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    x = np.asarray(x, float)
    mean = p
    var = p* (1. - p)
    # b = np.where(condition, true, False)
    PMF = np.where(x == 1., p, 1. - p)

    return PMF, float(mean), float(var)