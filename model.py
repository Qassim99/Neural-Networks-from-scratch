from layer import Layer
from activation import Relu
import nnfs
from nnfs.datasets import spiral_data
from softmax import Softmax

nnfs.init()

X, y = spiral_data(100, 3)

# print(X)

layer1 = Layer(2, 5)
layer1.forward(X)
activation1 = Relu()
activation1.forward(layer1.output)
output = activation1.output
print(output)
layer2 = Layer(5, 3)
layer2.forward(output)
softmax = Softmax()
softmax.forward(layer2.output)
print(softmax.output)
# print(layer2.output)