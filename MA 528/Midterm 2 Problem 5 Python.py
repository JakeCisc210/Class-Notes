"""
Checking Midterm 2 Problem 5 Answer
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

def rsArray(n):
    # n - size of r Array
    rsArray = np.zeros(n)
    
    dt = 1/n
    
    for k in range(n):
        if k == 0:
            rsArray[k] = .05
            
        if k != 0:
            dr = 5*(.04-rsArray[k-1])*dt + .2*np.random.normal(0,1)*np.sqrt(dt)
            rsArray[k] = rsArray[k-1] + dr
    
    return rsArray

#numerical integration
def Intrt2(rsArray):
    intVal = scipy.integrate.simps(rsArray, x=None, dx=1/len(rsArray))
    return intVal

def MonteCarloAns(n,numTrials):
    IntVals = np.zeros(numTrials)
    AnsSum = 0
    for m in range(numTrials):
        myArray = rsArray(n)
        myIntVal = Intrt2(myArray)
        IntVals[m] += myIntVal
        AnsSum += np.exp(myIntVal)
    
    IntAvg = np.mean(IntVals)
    IntStDev = np.std(IntVals)
    Answer = round(AnsSum/numTrials,4)
    return Answer

print("The Answer to Problem is " +str(MonteCarloAns(50,10000)) + " P0")