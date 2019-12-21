import numpy as np 
import random
import aihara_model

m = 50
n = m**2


def site_e():
    e  = np.zeros(n)
    for i in range(n):
        if (i%2) and (int(i/50))%2:
            e[i] = 1
        elif (i%2) == 0 and (int(i/50))%2 == 0:
            e[i] = 1
        else:
            e[i] = 0
    return e

def re_site_e():
    e  = np.zeros(n)
    for i in range(n):
        if (i%2) and (int(i/50))%2:
            e[i] = 0
        elif (i%2) == 0 and (int(i/50))%2 == 0:
            e[i] = 0
        else:
            e[i] = 1
    return e

def site_random():
    e = np.zeros(n)
    for i in range(n):
        e[i] = random.choice([0,1])
    return e

def wijMat():
    a = np.zeros((2500,2500))
    for i in range(2500):
        for j in range(2500):
            a[i][j] = aihara_model.wij(i,j)
    return a

def nArray():
    array = np.zeros(2500)
    for i in range(2500):
        array[i] = random.uniform(25/(2*(1-aihara_model.kf)),
        aihara_model.alpha/(25*(1-aihara_model.kf)))
    return array

def cArray():
    array = np.zeros(2500)
    for i in range(2500):
        array[i] = random.uniform(-aihara_model.alpha/(2*(1-aihara_model.kr)),
        aihara_model.alpha/(2*(1-aihara_model.kr)))
    return array
#print(re_site_e())
#np.save('data/site_e',site_e())
#np.save('data/re_e',re_site_e())
#np.save('data/random',site_random())

#np.save('data/c0',cArray())
#np.save('data/n0',nArray())
np.save('data/wMat',wijMat())
