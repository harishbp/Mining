import os
from face_detect import *
import time

# SRC_PATH = './0317/'
# DST_PATH = "./result_crop_031/"
fnames=[]

def walk_folder(SRC_PATH,DST_PATH):
    #Creates Dst folder
    try:
        if not os.path.exists(DST_PATH):
            os.makedirs(DST_PATH)
    except OSError:
        print ('Error: Creating directory. ' +  DST_PATH)


    for (dirpath, dirnames, filenames) in os.walk(SRC_PATH):
        # print(dirpath)
        fnames.extend(filenames)
        break

    for file in fnames:
        sep = file.split('.')
        if sep[1] == "gif":
            continue
        # print("walk",file)
        detect_face(SRC_PATH+file,sep[0], sep[1], DST_PATH)
        # time.sleep(1)
