import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    euc_norm_a = np.linalg.norm(a)
    euc_norm_b = np.linalg.norm(b)
    a_do_b = np.dot(a,b)

    if (euc_norm_a == 0) or (euc_norm_b == 0):
        return 0.0

    cos_sim = (a_do_b) / (euc_norm_a * euc_norm_b)

    return float(cos_sim)