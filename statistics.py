import numpy as np 
import matplotlib.pyplot as plt

"""
t = 50

xArray = np.load('data/output.npy')
hArray = np.load('data/hArray.npy')

x1 = 126
xArray1 = np.zeros(t)
xArrayhArray1 = np.zeros(t) 
x2 = 220
xArray2 = np.zeros(t)
xArrayhArray2 = np.zeros(t) 

tArray = range(t)

for i in range(50):
    xArray1[i] = xArray[100+i*10][x1]
    xArray2[i] = xArray[100+i*10][x2]

for i in range(50):
    xArrayhArray1[i] = hArray[100+i*10][x1]
    xArrayhArray2[i] = hArray[100+i*10][x2]

#plt.plot(tArray, xArray1 , c = 'k',label = 'one of the spiral center')
#plt.plot(tArray, xArray2 , c = 'b',label = 'one of a nomal neure')
#plt.ylim(-0.2,1.2)
#plt.legend(loc = 'upper right')
#plt.title('X\' Contrast ')

#plt.plot(tArray, xArrayhArray1 , c = 'k',label = 'H of the spiral center')
#plt.plot(tArray, xArrayhArray2 , c = 'b',label = 'H of a nomal neure')
#plt.ylim(0,30)
#plt.legend(loc = 'upper right')
#plt.title('H\' Contrast ')
"""
#function

x = np.arange(-5.1,5.1,0.05)

y1 = 1 /  (1 + np.exp(-x/0.02))
y2 =  0.5 * (1 + np.tanh(0.5 * x))


plt.plot(x,y1,c = 'k',label = 'exp')
plt.plot(x,y2,c = 'b',label = 'tanh')

plt.title('Output Function\' Contrast ')
plt.legend(loc = 'upper right')
#plt.ylim(0,1.1)
plt.show()
