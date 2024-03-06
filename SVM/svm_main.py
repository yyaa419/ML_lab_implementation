import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import kernal_function as k
import svm_data

#first select the data
classA=svm_data.classA
classB=svm_data.classB
target=svm_data.target
input=svm_data.input

# call the minimize function to get the alpha value
# make preparation first, define zero_fun and objective
def zero_fun(alpha):
    return np.dot(alpha,target)

n=len(target)
p_ij= np.zeros((n,n)) # ti*tj*K(xi*xj)
for i in range(0,n):
    for j in range(0,n):
        p_ij[i][j]=target[i]*target[j]*k.linear_kernel(input[i],input[j])
        # print("p",i,j,"is ",p_ij[i][j])
def objective(alpha):
    ret=0
    for i in range(0,n):
        for j in range(0,n):
            ret+=alpha[i]*alpha[j]*p_ij[i][j]

    ret=0.5*ret-np.sum(alpha)
    return ret

start=np.zeros(n)
B=[(0,None) for b in range(n)]
XC={'type':'eq','fun':zero_fun}
ret=minimize(objective, start, bounds=B, constraints=XC)
alpha=ret['x'] 


# extract non-zero alpha value and corresponding input points, target value
alpha_selected=[]
datapoint_selected=[]
target_selected=[]
for index in range(0,n):
    if (alpha[index]>=1e-5):
        alpha_selected.append(alpha[index])
        datapoint_selected.append(input[index,:])
        target_selected.append(target [index])

# calculate b value, here we choose the first supporting vector
n_slected=len(target_selected)
s=datapoint_selected[0]
sum=0
for index in range(0,n_slected):
    sum += alpha_selected[index]*target_selected[index]*k.linear_kernel(s,datapoint_selected[index])
b=sum-target_selected[0]

# implement the indicator function
def ind(s):
    sum=0
    for index in range(0,n_slected):
        sum += alpha_selected[index]*target_selected[index]*k.linear_kernel(s,datapoint_selected[index])
    return sum-b

# plotting
plt.figure(figsize=(8,4))
# plot two classes seperetly
plt.plot([p[0] for p in classA],
         [p[1] for p in classA],
         'b.')

plt.plot([p[0] for p in classB],
         [p[1] for p in classB],
         'r.')

plt.axis('equal')

# plot the decision boundary
xgrid = np.linspace(-5,5)
ygrid = np.linspace(-4,4)
grid = np.array([[ind((x,y))
                  for x in xgrid]
                  for y in ygrid])

plt.contour(xgrid,ygrid,grid,
            (-1.0, 0.0, 1.0),
            colors=('red','black','blue'),
            linewidths=(1,3,1))
plt.show()