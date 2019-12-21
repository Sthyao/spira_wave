import math
import numpy as np

a = 0
kr = 0.95
kf = 0.15
alpha = 4
epsilon = 0.02

n = 2500
m = 50

d = 2.0

kh = 0.95
c0 = 4.00
c1 = -10.00
c2 = 0.60

#use Capital name function, others are variate


def F(x):
    #temp = x
    #x[(-1.000 * x ) > 5.1] = 5.1
    #print(x)
    
    return 1 / (1 + np.exp(-x/epsilon))
    #return 0.5 * (1 + np.tanh(0.5 * x))

def wij(i,j):
    DL = m/2-abs(m/2-((abs(i-j)%m)))
    DT = m/2-abs(m/2-abs(math.ceil((1+i)/m)-math.ceil((j+1)/m)))
    if DL <= d and DT <= d and i != j:
        return (-1)**(i + j + math.ceil((1+i)/m) + math.ceil((1+j)/m))
    return 0


def Xor(arrayx,arraye):
    arraytemp = np.zeros(2500)
    arraytemp = np.logical_xor(arraye , np.ceil(arrayx - 0.5))
    return arraytemp

def MatToArr(Mat):
    arraytemp = np.zeros(2500)
    index = 0
    for i in range(50):
        for j in range(50):
            arraytemp[index] = Mat[i][j]
            index += 1
    return arraytemp
def ArrToMat(Arr):
    mattemp = np.zeros((50,50))
    index = 0
    for i in range(50):
        for j in range(50):
            mattemp[i][j] = Arr[index]
            index += 1
    return mattemp
        

#phase space control