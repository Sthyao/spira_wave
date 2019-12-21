import numpy as np 
import aihara_model
import random

a = np.load('data/random.npy')
site_e = np.load('data/site_e.npy')

t = 800
xArray = np.zeros((t,2500))
xArray[0] = a

wMat = np.load('data/wMat.npy')

n0 = np.load('data/n0.npy')
c0 = np.load('data/c0.npy')

cArray = np.zeros((t,2500))
cArray[0] = c0
nArray = np.zeros((t,2500))
nArray[0] = n0


#control model
hArrray = np.zeros((t,2500))
umin = np.zeros(t)
cArrayStar = np.zeros(t)



def main(x):
    for i in range(t):
        if i > 0:
            #contorl model
            hArrray[i] = aihara_model.kh*hArrray[i-1] + np.log10(1.0+abs(nArray[i-1]))
            umin[i] = hArrray[i].min()
            cArrayStar[i] = aihara_model.c0 + np.exp(aihara_model.c1 + aihara_model.c2*(umin[i]))

            #contorl model end
            cArray[i] = aihara_model.kr * cArray[i-1] - aihara_model.alpha * x[i-1] + aihara_model.a
            nArray[i] = aihara_model.kf * nArray[i-1] + wMat.dot(x[i-1])  
            x[i] = aihara_model.F(cArray[i]+nArray[i])
    return x



np.save('data/output',main(xArray))
np.save('data/nArray',nArray)
np.save('data/cArray',cArray)
np.save('data/hArray',hArrray)
