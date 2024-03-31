import numpy as np
# ###################################################
# Modeling - What we want to compute
# points = [(np.array([2]),4),(np.array([4]),2)]
# d = 1
true_w = np.array([1,2,3,4,5])
d = len(true_w)

points = []
for i in range(0000):
    x = np.random.rand(d)
    y = true_w.dot(x) + np.random.rand()
    points.append((x,y))




def F(w):
    result = sum((w.dot(x) - y) ** 2 for x,y in points)/len(points)
    return result
def dF(w):
    result = sum(2*(w.dot(x)-y)*x for x,y in points)/len(points)
    return result

def sF(w, i):
    (x,y) = points[i]
    result = (w.dot(x)-y)**2
    return result
def sdF(w, i):
    (x,y) = points[i]
    result = 2*(w.dot(x)-y)*x
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
def stocasticGradientDescent(sF, sdF, d, n):
        w = np.zeros(d)
        numOfUpdates = 0

        for t in range(1000):
            for i in range(n):
                  value = sF(w,i)
                  gradient = sdF(w,i)
                  numOfUpdates+=1
                  eta = 1/numOfUpdates
                  w = w-eta*gradient
            print(f'iteration {t}: w = {w}, F(w) = {value}')
# gradientDescent(F,dF,d)
stocasticGradientDescent(sF,sdF,d,len(points))
