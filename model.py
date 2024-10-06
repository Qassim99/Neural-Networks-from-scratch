from layer import Layer
from activation import Relu
import nnfs
from nnfs.datasets import spiral_data
from softmax import Softmax

nnfs.init()

X, y = spiral_data(100, 3)

# print(X)

fc1 = Layer(2, 5)
fc1.forward(X)
activation1 = Relu()
activation1.forward(fc1.output)
output = activation1.output
print(output)
fc2 = Layer(5, 3)
fc2.forward(output)
softmax = Softmax()
softmax.forward(fc2.output)
print(softmax.output)
# print(layer2.output)