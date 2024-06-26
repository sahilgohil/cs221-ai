import numpy as np
# ###################################################
# Modeling - What we want to compute
points = [(2,4),(4,2)]

def F(w):
    result = sum((w * x - y) ** 2 for x,y in points)
    return result
def dF(w):
    result = sum(2*(w * x-y)*x for x,y in points)
    return result

######################################################
# Algorithms - How we want to compute it
def gradientDescent(F , dF, d):
    w = np.zeros(d) # initial guess
    eta = 0.01 # learning rate or step for each iteration

    for i in range(1000):
        
        value = F(w)
        gradient = dF(w)
        w = w-eta*gradient
        print(f'iteration {i}: w = {w}, F(w) = {value}')

gradientDescent(F,dF,1)