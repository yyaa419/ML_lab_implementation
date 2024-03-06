import numpy as np
import random

np.random.seed(100)
# generate the data set
# the easier one is as followed
# classA=np.concatenate((
#     np.random.randn(10,2) * 0.1 + [0.5, 1],
#     np.random.randn(10,2) * 0.1 + [-0.5,1]
#     ))

# classB=np.concatenate((
#     np.random.randn(10,2) * 0.1 + [0.5, -1],
#     np.random.randn(10,2) * 0.1 + [-0.5,-1]
#     ))

# the difficult one is as followed
# and we find that when there shows overlapping, the optimizer
# will be not able to find a solution at all
classA=np.random.randn(10,2) * 0.5 + [0,-1]
classB=np.random.randn(10,2) * 0.5 + [0,-1]


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