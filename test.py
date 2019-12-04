import numpy as np 
import math

si = np.load('data/si.npy')
wMat = np.load('data/wMat.npy')
xa = np.load('data/first.npy')
ca = np.load('data/cArray.npy')
na = np.load('data/nArray.npy')
"""
for i in range(2500):
    sum = 0
    for j in range(2500):
        if wMat[i][j] != 0:
            sum = sum + 1
    if sum != 25:
        print(i)

def DL(i,j):
    return 25-abs(25-abs(math.ceil(i/50)-math.ceil(j/50)))

def DT(i,j):
    return 25-abs(25-(abs(i-j)%50))
print(DT(1,4))
"""
for i in range(500):
    print(na[0][i])