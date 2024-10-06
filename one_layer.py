inputs = [1.2, 5.1, 2.1]
weights =[[0.2, 0.1, -8.7],
            [0.1, -1, 0.7],
            [-0.5, 2.1, 0.2]]

biases = [2, 4, 3]


layer_outputs = []
for neuron_weights, bias in zip (weights, biases):
    neuron_output = 0
    for weight, input in zip(neuron_weights, inputs):
        neuron_output += weight* input
    neuron_output += bias
    layer_outputs.append(neuron_output)
print(layer_outputs)




import numpy as np
outputs = np.dot(weights, inputs) +biases
print(outputs)