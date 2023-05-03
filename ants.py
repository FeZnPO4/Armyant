import cv2
import numpy
import math
import gradio
import os.path
from selenium import webdriver
def main():
    itf=gradio.Interface(process,inputs="image",outputs="image")
    itf.launch()
    
 
    
def process(im,output="D:\\pythonres\\blue.bmp"):
    
    
    size=im.shape
    
    print(size)
    szx=size[0]
    szy=size[1]
    img=numpy.zeros((szx+1,szy+1),int)
    print(img)
    for x in range(1,szx):
        for y in range(1,szy):
            img[x][y]=(int(im[x][y][0])+int(im[x][y][1])+int(im[x][y][2]))/3
    
    for x in range(1,szx-1):
        for y in range(1,szy-1):
            img[x][y]=(int(img[x-1][y-1])+int(img[x-1][y])+int(img[x-1][y+1])+int(img[x][y-1])+int(img[x][y])+int(img[x][y+1])+int(img[x+1][y-1])+int(img[x+1][y])+int(img[x+1][y+1]))/9




    for x in range(1,szx):
        for y in range(1,szy):
            if(img[x][y]>=128):
                img[x][y]=255
            else:
                img[x][y]=0

    
    for x in range(1,szx-1):
        for y in range(1,szy-1):
            px=((int(img[x+1][y])-int(img[x][y]))+(int(img[x+1][y+1])-int(img[x][y+1])))/2
            py=((int(img[x][y+1])-int(img[x][y]))+(int(img[x+1][y+1])-int(img[x+1][y])))/2
            p=math.sqrt(px*px+py*py)
            
            img[x][y]=p

    cv2.imwrite(output,img)
    return img

sourceImagePath="D:\\orangesrc\\5f0868c25447aeecc0f3b020c0e3c18a.jpeg"
OutputPath="D:\\pythonres\\blue.bmp"



if __name__=="__main__":
    main()
  
