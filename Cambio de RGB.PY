import cv2
import numpy as np


BGR=cv2.imread('RGB.jpg')                  #Leemos la imagen (por default en forma de matriz tenemos B=0,G=1,R=2 en lugar de RGB)

C1=BGR[:,:,0]                              #Canal con intensidad Azul(B)

C2=BGR[:,:,1]                              #Canal con intensidad Verde(G)

C3=BGR[:,:,2]                              #Canal con intensidad Roja(R) 

cv2.imwrite("1.Blue.jpg",C1)               #Creamos la imagen solo con intensidad Azul

cv2.imwrite("2.Green.jpg",C2)              #Creamos la imagen solo con intensidad Verde

cv2.imwrite("3.RED.jpg",C3)                #Creamos la imagen solo con intensidad Roja

RG=np.copy(BGR)                            #Hacemos una copia de la imagen original

RG[:,:,0]=0                                #Le damos al canal azul(B) el valor 0

RB=np.copy(BGR)

RB[:,:,1]=0 

GB=np.copy(BGR)

GB[:,:,2]=0

cv2.imwrite("4.RG.jpg",RG)                #Creamos la imagen solo con intensidaded RG

cv2.imwrite("5.RB.jpg",RB)                #Creamos la imagen solo con intensidades RB

cv2.imwrite("6.GB.jpg",GB)                #Creamos la imagen solo con intensidades GB

cv2.imshow("B",C1)
cv2.imshow("G",C2)
cv2.imshow("R",C3)
cv2.imshow("RG",RG)
cv2.imshow("RB",RB)
cv2.imshow("GB",GB)


cv2.waitKey(0)
cv2.destroyAllWindows()