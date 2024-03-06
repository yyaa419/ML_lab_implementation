import math
import numpy as np


def linear_kernel(x,y):
    return np.dot(x,y)

# exponent=1
# exponent=2
# exponent=3
# exponent=4
# exponent=5
# exponent=6
exponent=7
# exponent=8
# exponent=9
def polynomial_kernel(x,y):
    return math.pow(np.dot(x,y),exponent)

# derivation=0.2  # gamma=25
# derivation=0.22 # gamma=10
# derivation=0.6 # gamma=2.7
derivation=0.8 # gamma=1.5
# derivation is used to control whether the curve is smooth enough,
# derivation is larger (gamma smaller), smoother, less likely to get
# overfitting 
def RBF_kernal(x,y):
    return math.exp(-np.linalg.norm(x-y)/(2*math.pow(derivation,2)))