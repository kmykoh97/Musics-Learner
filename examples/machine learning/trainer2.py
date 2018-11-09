# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:57:23 2018

@author: kmykoh
"""



# =============================================================================
# this is implemetation of neural network using the maximum likelihood estimation cost function
# rewriten based on trainer1.py
# =============================================================================

# data samples (training sets)
# type 0
data1 = [1, 1, 0]
data2 = [2, 1, 0]
data3 = [2, 0.5, 0]
data4 = [3, 1, 0]
# type 1
dataA = [3, 1.5, 1]
dataB = [3.5, 0.5, 1]
dataC = [4, 1.5, 1]
dataD = [5.5, 1, 1]
# unknown type to be determined
unknown = [4.5,  1, "Is this 1?"]

points = [data1, data2, data3, data4, dataA, dataB, dataC, dataD]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def train(noTrain):
    # initialised with random values
    w1 = random.random()
    w2 = -random.random()
    b = random.random()
    
    learningRate = 0.25
    
    # iterate for n times. If weights found are not acceptable, increase learning rate or increase iteration
    for i in range(0, noTrain):
        initialPoint = points[random.randint(0, len(points)-1)] # random point
        targetPoint = initialPoint[2] # target in 3rd coordinate
        
        hypothesis = w1 * initialPoint[0] + w2 * initialPoint[1] + b
        activation = sigmoid(hypothesis)
        
        cost = (targetPoint * np.log(activation) + (1 - targetPoint) * np.log(1 - activation)) # logistic regression cost function
        
        # now we have to get the slope of cost w.r.t w1, w2, b
        # first get the required derivatives
        dcostdactivation = 2 * (activation - targetPoint)
        dactivationdhypothesis = sigmoid(hypothesis) * (1 - sigmoid(hypothesis))
        dhypothesisdw1 = initialPoint[0]
        dhypothesisdw2 = initialPoint[1]
        dhypothesisdb = 1
        
        # backpropogation
        # use chain rule to get the partial derivatives of cost
        dcostdw1 = 
        dcostdw2 = dcostdactivation * dactivationdhypothesis * dhypothesisdw2
        dcostdb = dcostdactivation * dactivationdhypothesis * dhypothesisdb
        
        # update parameter w1, w2, b
        w1 -= learningRate * dcostdw1
        w2 -= learningRate * dcostdw2
        b -= learningRate * dcostdb
    
    return [w1, w2, b]

def classifier(para):
    h = unknown[0] * para[0] + unknown[1] * para[1] + para[2]
    prediction = sigmoid(h)
    
    # give predicted results
    if prediction < 0.5:
        return 0
    else:
        return 1
    
def plotData(noTrain):
    sample = train(noTrain)
    
    # plot scattered points
    plt.axis([0, 6, 0, 6])
    plt.grid()
    
    for i in range(0, len(points)):
        individualPoints = points[i]
        if individualPoints[2] == 0:
            color = "b"
        else:
            color = "r"
        plt.scatter(individualPoints[0], individualPoints[1], c = color)
    
    # plot unknown points
    plt.scatter(unknown[0], unknown[1], c = "y")
    
    # draw classfier lines
    x = np.array(range(0, 7))  
    y = (0.5 - sample[2] - x * sample[0]) / sample[1]
    plt.plot(x, y)
    plt.show()
    
    return classifier(sample)

# perform numerical estimation of gradient
def gradientCheck():
    epsilon = 10 ** (-4)
    

def main():
    # for testing, print the w1, w2, b for checking
    print("The parameters we got are approximately: ", train(100000))
    
    # visualise the graph
    result = plotData(1000000)
    
    # determine the type of unknown
    if result == 0:
        print("The unknown is of type 0 (blue)")
    else:
        print("The unknown is of type 1 (red)")



if __name__ == "__main__":
    import numpy as np
    import random
    import matplotlib.pyplot as plt
    
    main()