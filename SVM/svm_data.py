import random
import numpy as np
#all data point is two dimension, which means x[n][2],  y[n]
# np.random.seed(100)

classA=np.concatenate((
    np.random.randn(10,2) * 0.2 + [1.5, 0.5],
    np.random.randn(10,2) * 0.2 + [-1.5,0.5]
    ))

classB=np.random.randn(20,2) * 0.2 + [0,-1.5]

input=np.concatenate((classA,classB))
target=np.concatenate((
    np.ones(classA.shape[0]),
    -np.ones(classB.shape[0])
))
n=input.shape[0]

permute=list(range(n))
random.shuffle(permute)
input=input[permute,:]
target=target[permute]