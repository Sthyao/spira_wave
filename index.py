import numpy as np 
import aihara_model

a = np.load('data/random.npy')

t = 300
xArray = np.zeros((t,2500))
xArray[0] = a

wMat = np.load('data/wMat.npy')
cArray = np.zeros((t,2500))
nArray = np.zeros((t,2500))

def wijMat(x):
    a = np.zeros((2500,2500))
    for i in range(2500):
        Si = aihara_model.SI(i)
        #a[i] = Si
        for j in range(2500):
            a[i][j] = aihara_model.wij(i,j,x,Si)
    return a
    



def main(x):
    for i in range(t):
        if i > 0:
            cArray[i] = aihara_model.kr*cArray[i-1] - aihara_model.alpha * x[i-1] + aihara_model.a
            nArray[i] = aihara_model.kf*nArray[i-1] + wMat.dot(x[i-1]) 
            x[i] = aihara_model.F(cArray[i]+nArray[i])
        else:
            pass
    return x

#print(wijMat(a))
np.save('data/first',main(xArray))
#np.save('data/wMat',wijMat(a))


