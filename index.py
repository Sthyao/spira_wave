import numpy as np 
import aihara_model
import random

a = np.load('data/random.npy')
site_e = np.load('data/site_e.npy')

t = 300
xArray = np.zeros((t,2500))
xArray[0] = a

wMat = np.load('data/wMat.npy')
cArray = np.zeros((t,2500))
cArrayStar = np.zeros(t)
nArray = np.zeros((t,2500))
hArrray = np.zeros((t,2500))
umin = np.zeros(t)
si = np.zeros((2500,50))
#si =  np.load('data/si.npy')

#init cArray 

for i in range(2500):
    cArray[0][i] = random.uniform(-aihara_model.alpha/(2*(1-aihara_model.kr)),
    aihara_model.alpha/(2*(1-aihara_model.kr)))
    nArray[0][i] = random.uniform(25/(2*(1-aihara_model.kf)),
    aihara_model.alpha/(25*(1-aihara_model.kf)))

def wijMat(x):
    a = np.zeros((2500,2500))
    for i in range(2500):
        Si = aihara_model.SI(i)
        si[i] = Si 
        #a[i] = Si
        for j in range(2500):
            #print(aihara_model.wij(i,j,x,Si))
            a[i][j] = aihara_model.wij(i,j,x,Si)
    return a
    
def siTest(i):
    return aihara_model.SI(i)


def main(x):
    for i in range(t):
        if i > 0:
            #contorl model
            #hArrray[i] = aihara_model.kh*hArrray[i-1] + np.log10(1+abs(nArray[i-1]))
            #umin[i] = hArrray[i].min()
            #cArrayStar[i] = aihara_model.c0 + np.exp(aihara_model.c1 + aihara_model.c2*(umin[i]))
            #contorl model end
            cArray[i] = aihara_model.kr * cArray[i-1] - aihara_model.alpha * x[i-1] + aihara_model.a
            
            #temp = cArrayStar[i]
            #cArray[cArray > temp] = temp
            #cArray[cArray < -temp] = -temp 
            nArray[i] = aihara_model.kf * nArray[i-1] + wMat.dot(x[i-1]) 
            #nArray[i] = aihara_model.kf * nArray[i-1] + x[i-1].dot(wMat) 
            x[i] = aihara_model.F(cArray[i]+nArray[i])
        else:
            pass
    return x


"""

for i in range(300):
    if wMat[122][i] != 0:
        print(wMat[122][i])
"""
#wijMat(xArray[0])
np.save('data/second_c',main(xArray))
#np.save('data/wMat',wijMat(site_e))
#np.save('data/si',si)
#np.save('data/cArray',cArray)
#np.save('data/nArray',nArray)

"""

for i in range(30):
    print(na[i])
"""

#print(siTest(0))


