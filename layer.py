import numpy as np


np.random.seed(0)

X =[[2, 2, 3, 2.5],
            [3, 6, 1, 9],
            [1, 7, 2, 5]]

class Layer:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, input):
        self.output = np.dot(input, self.weights) + self.biases

# layer1 = Layer(4, 5)
# layer1.forward(X)
# print(layer1.output)

# layer2 = Layer(5, 2)
# layer2.forward(layer1.output)
# print(layer2.output)