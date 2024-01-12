#create an array ([[1,2,3,5],[45,67,89,77],[33,55,70,99]]]& print it.#
import numpy as np
x=np.array([[1,2,3,5],[45,67,89,77],[33,55,70,99]])
print(x)
print(x[1:2])
y=x[1:2]
print(y)
print(y.shape)