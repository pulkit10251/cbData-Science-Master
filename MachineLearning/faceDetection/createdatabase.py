import cv2
import numpy

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

skip=0

face_data=[]

dataset_path='./data/'

while True:
    ret,frame=cap.read()
    
    if ret == False:
        continue
        
    #face_section=   
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   
    
    faces=face_cascade.detectMultiScale(frame,1.3,5)
    faces=sorted(faces,key=lambda f:f[2]*f[3])
    
    print(faces)
    
    for face in faces[-1:]:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

        #Extract (Crop out the required face) : Region of Interest
        offset = 10
        face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
        face_section = cv2.resize(face_section,(100,100))

        skip += 1
        if skip%10==0:
            face_data.append(face_section)
            print(len(face_data))


    cv2.imshow("Frame",frame)
    cv2.imshow("Face Section",face_section)
   # cv2.imshow("face_section",face_section)
        
    key_pressed=cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
        
        
cap.release()
cv2.destroyAllWindows()