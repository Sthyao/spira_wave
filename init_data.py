import numpy as np 
import random

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

print(re_site_e())
np.save('data/site_e',site_e())
np.save('data/re_e',re_site_e())
np.save('data/random',site_random())