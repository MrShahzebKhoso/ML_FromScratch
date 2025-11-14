import numpy as np

def nesterov_momentum_step(w, v, grad, lr=0.01, momentum=0.9):
    """
    Perform one Nesterov Momentum update step.
    """

    w = np.asarray(w, float)
    v = np.asarray(v, float)
    g = np.asarray(grad, float)


    w_look = w - (momentum *  v)
    v_new = (momentum * v) + (lr * g)
    w_new = w - v_new

    return w_new, v_new