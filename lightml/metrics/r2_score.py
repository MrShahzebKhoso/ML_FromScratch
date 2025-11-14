import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    y_mean = np.mean(y_true)

    if (len(np.unique(y_true)) == 1):
      if (np.array_equal(y_true, y_pred)):
        return 1.0
      else:
         return 0.0
    else:

      SSR = np.sum((y_true - y_pred)**2)
      TSS  = np.sum((y_true - y_mean)**2)

      R2 = 1. - (SSR / TSS)

      return float(R2)