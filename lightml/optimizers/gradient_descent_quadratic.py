def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    for step in range(0,steps):

        f_d_x = 2 * a * x0 + b

        x0 = x0 - lr * f_d_x

    return x0