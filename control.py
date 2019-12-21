import numpy as np 
import aihara_model

cArray = np.load('data/cArray.npy')
nArray = np.load('data/nArray.npy')
xArray = np.load('data/output.npy')
wMat = np.load('data/wMat.npy')

start = 105
t = 200

xArrayControl = np.zeros((t,2500))
cArrayControl = np.zeros((t,2500))
nArrayControl = np.zeros((t,2500))

xArrayControl[0] = xArray[start]
cArrayControl[0] = cArray[start]
nArrayControl[0] = nArray[start]

hArrray = np.zeros((t,2500))
umin = np.zeros(t)
cArrayStar = np.zeros(t)

def main(x):
    for i in range(t):
        if i > 0:
            #contorl model
            hArrray[i] = aihara_model.kh*hArrray[i-1] + np.log10(1.0+abs(nArrayControl[i-1]))
            umin[i] = hArrray[i].min()  
            cArrayStar[i] = aihara_model.c0 + np.exp(aihara_model.c1 + aihara_model.c2*(umin[i])) 
            #contorl model end

            cArrayControl[i] = aihara_model.kr * cArrayControl[i-1] - aihara_model.alpha * x[i-1] + aihara_model.a
            temp = cArrayStar[i] 
            cArrayControl[abs(cArrayControl) > temp] = cArrayControl[abs(cArrayControl) > temp] / abs(cArrayControl[abs(cArrayControl) > temp]) * temp

            nArrayControl[i] = aihara_model.kf * nArrayControl[i-1] + wMat.dot(x[i-1]) 
            x[i] = aihara_model.F(cArrayControl[i]+nArrayControl[i])
    return x

np.save('data/control',main(xArrayControl))
np.save('data/hArrayControl',hArrray)


