#import the library opencv
import cv2
#globbing utility.
import glob
from ocr_core import ocr_core
import os
#select the path
def cropper(path):

    path = "/home/raniya/dev/check/images/*.*"
    path1="/home/raniya/dev/check/images"
    list=os.listdir(path1)
    n1=len(list)
    print(n1)
    for bb,file in enumerate(glob.glob(path)):
        print(bb,file)
        img= cv2.imread(file)
        cv2.imshow("Image",img)
        cv2.namedWindow("Crop")
        (h, w,) = img.shape[:2] 
        delta1 = int(w-(w*0.30))
        delta = int((h*0.42) - (h * 0.1))
        y=int(0.6*h)
        bottom= img[delta:y, delta1:w]
        cv2.imshow("Crop",bottom)
        cv2.imwrite("crop/checksaver"+str(bb)+".png",bottom)
        cv2.waitKey(0)
    ocr_core(path)
