import numpy as np 
import pandas as pd 
import cv2
import matplotlib.pyplot as plt 


cap=cv2.VideoCapture(0)
nose_cascade=cv2.CascadeClassifier("Nose18x15.xml")
eye_cascade=cv2.CascadeClassifier("frontalEyes35x16.xml")


def overlay_image_alpha(img, img_overlay, pos, alpha_mask):
    """Overlay img_overlay on top of img at the position specified by
    pos and blend using alpha_mask.

    Alpha mask must contain values within the range [0, 1] and be the
    same size as img_overlay.
    """

    x, y = pos

    # Image ranges
    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    # Overlay ranges
    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    # Exit if nothing to do
    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    channels = img.shape[2]

    alpha = alpha_mask[y1o:y2o, x1o:x2o]
    alpha_inv = 1.0 - alpha

    for c in range(channels):
        img[y1:y2, x1:x2, c] = (alpha * img_overlay[y1o:y2o, x1o:x2o, c] +
                                alpha_inv * img[y1:y2, x1:x2, c])




glasses=cv2.imread('glasses.png',-1)
mustache=cv2.imread('mustache.png',-1)

while True:
    ret,frame=cap.read()
    
    if ret == False:
        continue
    eyes=eye_cascade.detectMultiScale(frame,1.3,2)
    nose=nose_cascade.detectMultiScale(frame,1.3,5)
    print(eyes)
    print(nose)
    if(len(eyes) != 0):
        x,y,w,h=eyes[0]
        glasses=cv2.resize(glasses,(w,h))
        overlay_image_alpha(frame,glasses[:, :, 0:3],(x, y),glasses[:, :, 3] / 255.0)
    
    if(len(nose)!=0):
        (x,y,w,h)=nose[0]
        xs=mustache.shape[1]
        ys=mustache.shape[0]
        per=w/xs
        xh=int(ys*per)
        mustache=cv2.resize(mustache,(w+20,xh+11))
    
        ypos=int(y+0.56*h)
        overlay_image_alpha(frame,mustache[:, :, 0:3],(x, ypos),mustache[:, :, 3] / 255.0)

    cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("frame",frame)
    
    key_pressed=cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
