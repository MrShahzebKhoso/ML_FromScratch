import numpy as np
from lightml.activations.sigmoid import sigmoid
from lightml.activations.relu import relu

x = np.array([-2, -1, 0, 1, 2])
x_sigmoid = sigmoid(x)
x_relu = relu(x)
print(f"Sigmoid: {x_sigmoid}")
print(f"ReLU:{x_relu}")
