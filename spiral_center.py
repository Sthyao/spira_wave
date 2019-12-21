import numpy as np
from PIL import Image

def bigger(a):
    largeMat = np.zeros((150,150))
    for i in range(2500):
        tempX = i%50*3
        tempY = (int(i/50))*3
        for j in range(3):
            for k in range(3):
                largeMat[tempX+j][tempY+k] = a[i]
    return largeMat

def To_image(a,imageName):
    toImage = Image.new('RGB',(150,150))
    tempDepth = 0
    
    max = a.max()
    min = a.min()
    for j in range(150):
        for k in range(150):
            tempDepth = int(255 * (a[j][k]-min) / (max-min))
            pixTuple = (tempDepth,tempDepth,tempDepth,15)
            toImage.putpixel((j,k),pixTuple)
    
    string = str(imageName) + '.png'
    toImage.save('fig/spiral_center_control/'+string,'PNG')
    #print(max,min)
    

def draw(x):
    t = 130
    for i in range(50):
        temp = x[t+i]
        To_image(bigger(temp),'t=' + str(t+i))

hArray = np.load('data/hArray.npy')
hArrayControl = np.load('data/hArrayControl.npy')

draw(hArrayControl)
#print(hArray[200].min())
