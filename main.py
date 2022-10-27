import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

def Empirical_F(x):
    l = len(x)
    x.sort()
    matrixAsArrays = [[x[i], (lastIndexOf(x, x[i])+1)*(1/l)]     for i in range(l)]


    res = np.matrix(matrixAsArrays)
    return res

def lastIndexOf(arr, val):
    for i in range(len(arr)):
        if arr[len(arr)-(i+1)] == val:
            return len(arr)-(i+1)
    return -1
b= [1,2,3,3,5,6,6]
print(Empirical_F(b))