import numpy as np
class Relu:
    def __init__(self):
        pass
    def forward(self, input):
        self.output = np.maximum(0, input)