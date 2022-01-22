import cv2
import time
import numpy as np
from numpy.core.defchararray import upper


camera=cv2.VideoCapture(0)
image=cv2.imread('Background.cms')



while (True):
    ret,frame=camera.read()
    print(frame)
    frame=cv2.resize(frame,(640,480))
    image=cv2.resize(image,(640,480))

    lowerBlack=np.array([30,30,0])
    upperBlack=np.array([104,153,70])
    mask=cv2.inRange(frame,lowerBlack,upperBlack)
    res=cv2.bitwise_and(frame,frame,mask=mask)


    f=frame-res
    f= np.where(f==0,image,f)
   
    
   
    
    cv2.imshow('COUNTRIES',frame)
    cv2.imshow('Background',f)
    
    if cv2.waitKey(1)& 0xFF==ord('Q'):
        break 

camera.release()
cv2.destroyAllWindows()

