import numpy

input = [1.2, 5.1, 2.1]



weight1 = [0.2, 0.1, -8.7]
weight2 = [0.1, -1, 0.7]
weight3 = [-0,5, 2.1, 0.2]
bias1 = 3
bias2 = 2
bias3 = 1

output1 = weight1[0]* input[0] + weight1[1]* input[1] + weight1[2]* input[2] + bias1
output2 = weight2[0]* input[0] + weight2[1]* input[1] + weight2[2]* input[2] + bias2
output3 = weight3[0]* input[0] + weight3[1]* input[1] + weight3[2]* input[2] + bias3
outputs = [output1, output2, output3]
print(outputs)

