import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """

    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)


    # error  = np.where(condition, True, False)
    error  = y_true - y_pred
    HL = np.where(np.abs(error) <= delta,
    (1./2.)* error **2,
    delta * (np.abs(error) - (1./2.)* delta)
     )

    err = np.mean(HL)

    return err