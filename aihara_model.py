import math
import numpy as np

a = 0
kr = 0.95
kf = 0.15
alpha = 4.0
epsilon = 0.02

n = 2500
m = 50

d = 2

kh = 0
#W is not define


#use Capital name function, others are variate

def Zeta(t):
    return kr*Zeta(t-1)-alpha*Chi(t-1) + a

def Chi(t):
    return F(Zeta(t)+Eta(t))

def Eta(t):
    return kf*Eta(t-1)+W*Chi(t-1)

def F(x):
    return 1/(1+np.exp(-x/epsilon))

def DT(i,j):
    return m/2-abs(m/2-(abs(i-j)%m))
def DL(i,j):
    return m/2-abs(m/2-abs(np.ceil(i/m)-np.ceil(j/m)))

def SI(i):
    d = 2
    Si = np.zeros(50)
    step = 0
    for j in range(2500):
        if DL(i,j) <= d and DT(i,j) <= d:
            Si[step] = j
            step = step+1
    return Si


def wij(i,j,array,Si):
    for num in range(50):
        if Si[num] == j:
            #return (-1)**(i+j+math.ceil(i/m)+math.ceil(j/m))
            return (2*array[i]-1)*(2*array[j]-1)
        else:
            return 0

def Xor(arrayx,arraye):
    arraytemp = np.zeros(2500)
    for i in range(2500):
        arraytemp[i] = (arraye[i] != np.ceil(arrayx[i] - 0.5))
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

def Hi(t):
    return kh * Hi(t-1) + np.log10(1+abs(Eta(t-1)))

def U(t,array):
    return min(array(t))
