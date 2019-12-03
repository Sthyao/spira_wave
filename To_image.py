import numpy as np 
from PIL import Image
import os,sys

import aihara_model

f_zero = "data/0.png"
f_one = "data/1.png"
mw = 10



#init



def bigger(a):
    largeMat = np.zeros((150,150))
    for i in range(2500):
        tempX = i%50*3
        tempY = (int(i/50))*3
        if a[i] == 1:
            for j in range(3):
                for k in range(3):
                    largeMat[tempX+j][tempY+k] = 1
        else:
           for j in range(3):
                for k in range(3):
                    if j == 1 and k == 1 :
                        largeMat[tempX+j][tempY+k] = 1
                    else:
                        largeMat[tempX+j][tempY+k] = 0      
    return largeMat

def To_image(a,id):
    toImage = Image.new('RGB',(150,150))
    pixTupleB = (0,0,0,15)
    pixTupleW = (255,255,255,15)
    for j in range(150):
        for k in range(150):
            if a[j][k] == 1:
                toImage.putpixel((j,k),pixTupleB)
            else:
                toImage.putpixel((j,k),pixTupleW)
    string = str(id) + '.png'
    toImage.save('fig/'+string,'PNG')


#print(len(bigger(a)))

a = np.load('data/site_e.npy')
To_image(bigger(a),0)

a = np.load('data/re_e.npy')
To_image(bigger(a),1)

a = np.load('data/random.npy')
To_image(bigger(a),2)

a = np.load('data/first.npy')
b = np.load('data/site_e.npy')
a = aihara_model.Xor(a[50],b)
To_image(bigger(a),10050)








