import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # print(f"x : {x}")
    x = np.atleast_1d(x).astype(float)
    x_r = np.maximum(0,x)
    # print(f"ReLU(x) : {x_r}")

    return x_r