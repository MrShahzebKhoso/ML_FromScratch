import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """

    w = np.asarray(w, float)
    m = np.asarray(m, float)
    v = np.asarray(v, float)
    g = np.asarray(grad, float)


    m_new = beta1 * m + (1. - beta1) * g
    v_new = beta2 * v + (1. - beta2) * g*g

    w_new = w - lr * (weight_decay * w) - (lr * m_new / (np.sqrt(v_new)+ eps))

    return w_new, m_new, v_new
