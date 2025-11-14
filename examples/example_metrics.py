import numpy as np
from lightml.metrics.f1_micro import f1_micro

y_true = np.array([1,0,1,1])
y_pred = np.array([1,1,1,0])
f1_score = f1_micro(y_true, y_pred)
print(f"Micro F1: {f1_score}")
