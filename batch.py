import numpy as np
inputs =[[2, 3, 2, 5],
            [3, 6, 1, 9],
            [1, 7, 2, 5]]


weights =[[0.2, 0.1, -8.7, 1],
            [0.1, -1, 0.7, 5],
            [-0.5, 2.1, 0.2, -1]]

biases = [2, 4, 3]

outputs = np.dot(inputs, np.array(weights).T)
print(outputs)
outputs = np.dot(inputs, np.array(weights).T) + biases
print(outputs)

def transport(weights):
    matrix = [[0 for _ in range(len(weights))] for _ in range(len(weights[0]))]
    for i in range(len(weights)):
        for j in range(len(weights[0])):
            matrix[j][i] = weights[i][j]
    return matrix


print(transport(weights))
matrix = transport(weights)
print(len(matrix[0]))
def multiarray(inputs, weights):
    if len(inputs[0]) != len(weights):
        print("Matrices can't be multiplied!!!")
        return
    else:
        
        matrix = [[0 for _ in range(len(weights[0]))] for _ in range(len(inputs))]
        
        
        for i in range(len(inputs)):  
            for j in range(len(weights[0])):  
                for k in range(len(weights)):  
                    matrix[i][j] += inputs[i][k] * weights[k][j]
        
        return matrix
        
print(multiarray(inputs, matrix))


