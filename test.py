import numpy as np 
import math
import aihara_model


wMat = np.load('data/wMat.npy')

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
j = 999
num = 0 
"""
for i in range(2500):
    if wMat[j][i] != 0:
        #print(wMat[j][i])
        num = num + 1
        print(i+1)

print(num)

m = 50

def dt(i,j):
    return m/2-abs(m/2-((abs(i-j)%m)))

def dl(i, j):
    return m/2-abs(m/2-abs(math.ceil((1+i)/m)-math.ceil((j+1)/m)))

print(dt(1000,852))
print(dl(1000,852))
"""
print(aihara_model.wij(1000,1101))
print(wMat[1000][852])