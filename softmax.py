import numpy as np
class Softmax:
    def forward(self, input):
        exp_values = np.exp(input - np.max(input, axis=1, keepdims=True))
        probabilities = exp_values/  np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities


# softmax = Softmax()

# input = [4.8, 1.21, 2.385]

# softmax.forward(input)
# print(softmax.output)