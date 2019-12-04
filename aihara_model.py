import math
import numpy as np

a = 0
kr = 0.85
kf = 0.15
alpha = 2.5
epsilon = 0.2

n = 2500
m = 50

d = 2

kh = 0.95
#W is not define

c0 = 2.0
c1 = -10.0
c2 = 0.2

#use Capital name function, others are variate

def Zeta(t):
    return kr*Zeta(t-1)-alpha*Chi(t-1) + a

def Chi(t):
    return F(Zeta(t)+Eta(t))

def Eta(t):
    return kf*Eta(t-1)+W*Chi(t-1)

def F(x):
    x[(-1.000 * x ) > 25] = 25
    return 1.0000 / ( 1.0000 + np.exp( -1.0000 * x / epsilon))

def DT(i,j):
    return m/2-abs(m/2-(abs(i-j)%m))
def DL(i,j):
    return m/2-abs(m/2-abs(math.ceil(i/m)-math.ceil(j/m)))

def SI(i):
    d = 2
    Si = np.zeros(50)
    step = 0
    for j in range(2500):
        #print(DL(i,j),DT(i,j))
        
        if DL(i,j) <= d and DT(i,j) <= d:
            Si[step] = j
            step = step+1
        
    return Si


def wij(i,j,array,Si):
    for num in range(50):
        if Si[num] == j:
            if j == 0 and num == 0:
            #return (-1)**(i+j+math.ceil(i/m)+math.ceil(j/m))
                return (2*array[i]-1)*(2*array[j]-1)
            elif j == 0 and num != 0:
                return 0
            else:
                return (2*array[i]-1)*(2*array[j]-1)
        else:
            pass
    return 0

def Xor(arrayx,arraye):
    arraytemp = np.zeros(2500)
    #arrayx[arrayx <= 0.5] = 0
    #arrayx[arrayx > 0.5] = 1
    arraytemp = arrayx
    arraytemp = (arraye != np.ceil(arrayx - 0.5))
    #arraytemp = (arraye != np.ceil(arraytemp - 0.5)) 
    #print(arrayx)
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
