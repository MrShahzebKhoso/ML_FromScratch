import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    y_train = np.asarray(y_train)

    classes, counts = np.unique(y_train, return_counts=True)
    max = classes[np.argmax(counts)]
    y_pred = np.asarray([max for i in range(0, len(X_test))], dtype=int)

    return y_pred