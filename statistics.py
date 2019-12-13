import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
import aihara_model

t = 300
xArray = np.load('data/second.npy')
site_e = np.load('data/site_e.npy')

x = np.arange(2500)
xMini = np.arange(1200,1400,1)
y = np.zeros(2500)
yMini = np.zeros(200)

for i in range(20):
    temp = aihara_model.Xor(xArray[i*20+60],site_e)
    y = y + temp

for i in range(200):
    yMini[i] = y[1250+i]
fig1 = plt.figure(2)
#rects =plt.bar(x,y,align="center")
rects = plt.bar(xMini,yMini,align="center")
plt.title('Frequency')
plt.show()


