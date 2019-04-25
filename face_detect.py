import numpy as np
import cv2 as cv
import os
# from PIL import Image

def detect_face(fname,name,ext,DST_PATH):
    os.getcwd()
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # print("face_detect",fname)
    img = cv.imread(fname)
    # print("img",img)
    try:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # print("faces",faces)
        count=1
        for (x,y,w,h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255, 255, 255, 0),0)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            cropped = img[y:y+h, x:x+w]
            cv.imwrite(DST_PATH+name+"_"+ str(count) + "." +ext, cropped)
            print(DST_PATH+name+"_"+ str(count) + "." +ext, "cropped")
            img_size = cv.imread(DST_PATH+name+"_"+ str(count) + "." +ext)
            height, width, channels = img_size.shape
            # print(height, width, channels)
            if width<90 and height<90:
                # print("delete ",DST_PATH+name+"_"+ str(count) + "." +ext)
                # print(width,height)
                # cv.imwrite(DST_PATH+"delete/"+name+"_"+ str(count) + "." +ext, cropped)
                # print(DST_PATH+name+"_"+ str(count) + "." +ext)
                os.remove(DST_PATH+name+"_"+ str(count) + "." +ext)
            else:
                continue
            count+=1

    except:
        pass
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    # print("done crop for "+fname)
