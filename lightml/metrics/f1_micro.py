def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    correct = [(x == y) for x,y in zip(y_true,y_pred)]
    tp = sum(correct)
    fp = len(y_pred) - tp
    fn = fp

    f1 = (2. * tp)/ (2. * tp + fp +fn)

    return f1

