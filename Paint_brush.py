# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:17:27 2020

@author: VIvek
"""

""" Press left mouse button and drag the mouse to start drawing"""
"""TO clear the image press the right mouse button and press c or if you have change your mind about clearing the image: press escape"""
""" To stop drawing just stop pressing the mouse button"""
"""To change the color of the brush press right mouse button then press p in the keyboard- Adjust the colour """
"""To change the color of the background press right mouse button then press b in the keyboard- Adjust the colour """
"""Color is chosen by adjusting the amount of R,G,B pigments from the trackbar"""
"""TO close the program press escape on keyboard"""

import cv2
import numpy as np

img=np.ones((500,800,3),dtype="uint8")

for i in range(0,3):
    img[:,:,i]=255

cv2.imshow("Image",img)
cv2.destroyAllWindows()


start=False

        
def paint(event,x,y,flags,param):
    global img
    global r,g,b
    if event==cv2.EVENT_LBUTTONDOWN:
        global start
        global point 
        point=(x,y)
        start=True
    elif event==cv2.EVENT_MOUSEMOVE and start==True:
    
         cv2.circle(img,point,3,(b,g,r),-1)
         point=(x,y)
        
    elif event==cv2.EVENT_LBUTTONUP:
        start=False
    elif event==cv2.EVENT_RBUTTONDOWN:
        while(True):
            ch=cv2.waitKey(1)
            if ch==ord("c"):
                
                img=np.zeros((500,800,3),dtype="uint8")
                for i in range(0,3):
                    img[:,:,i]=255
                break
                
            
            if ch==ord("b"):    
                cv2.destroyWindow("Frame")
                cv2.imshow("Frame",img)
                cv2.createTrackbar("Background_R","Frame",0,255,Color_change)
                cv2.createTrackbar("Background_G","Frame",0,255,Color_change)
                cv2.createTrackbar("Background_B","Frame",0,255,Color_change)  
                while(True):
                                  
                    R=cv2.getTrackbarPos("Background_R","Frame")
                    G=cv2.getTrackbarPos("Background_G","Frame")
                    B=cv2.getTrackbarPos("Background_B","Frame")
                    t=cv2.waitKey(1)
                    if t==27:
                        break
                print(R)
                print(B)
                print(G)
                a=[]
                a.append(B)
                a.append(G)
                a.append(R)
                
                for i in range(0,3):
                    img[:,:,i]=a[i]
                print(img)
                global img2
                img2=np.copy(img)
                cv2.destroyWindow("Frame")
                cv2.imshow("Frame",img)
                cv2.setMouseCallback("Frame",paint)
                break
            if ch==ord("p"):    
                
                cv2.createTrackbar("Draw_R","Frame",0,255,Color_change)
                cv2.createTrackbar("Draw_G","Frame",0,255,Color_change)
                cv2.createTrackbar("Draw_B","Frame",0,255,Color_change)
                R=0
                G=0
                B=0
                while(True):
                    R=cv2.getTrackbarPos("Draw_R","Frame")
                    G=cv2.getTrackbarPos("Draw_G","Frame")
                    B=cv2.getTrackbarPos("Draw_B","Frame")
                    t=cv2.waitKey(1)
                    if t==27:
                        break
                
                r=R
                g=G
                b=B
                
                
                print(img)
                cv2.destroyWindow("Frame")
                cv2.imshow("Frame",img)
                cv2.setMouseCallback("Frame",paint)
                break
            elif ch==27:
                break
    
def Color_change(x):
    pass
    
cv2.imshow("Frame",img)



cv2.setMouseCallback("Frame",paint)

r=0
g=0
b=0

while(True):
    cv2.imshow("Frame",img)
    
   
    ch=cv2.waitKey(1)
   
    if ch==27:
        break
cv2.destroyAllWindows()