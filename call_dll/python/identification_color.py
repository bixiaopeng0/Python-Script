import find_car_contour
import cv2
import time
import ctypes
import os
import numpy as np

from ctypes import *
#黑
# img_path = 'G:/19\lab\python\Vehicle Re-identification\doc\dataset\VRID\image/1\License_1/4404000000002940408492.jpg'
#金色
# img_path = 'G:/19\lab\python\Vehicle Re-identification\doc\dataset\VRID\image/4\License_302/4404000000002947607742.jpg'
#白色
# img_path = 'G:/19\lab\python\Vehicle Re-identification\doc\dataset\VRID\image/6\License_522/4404000000002940377174.jpg'
#红色
# img_path = 'G:/19\lab\python\Vehicle Re-identification\doc\dataset\VRID\image/2\License_109/4404000000002946026672.jpg'
#绿色
img_path = 'G:/19\lab\python\Vehicle Re-identification\doc\dataset\VRID\image/3\License_203/4404000000002940410681.jpg'

img = cv2.imread(img_path)



def recog_car_color(img):
    img1 = img.copy()
    x, y, w, hi = find_car_contour.find_car_contour(img1)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    color_hist = {'blank':0,'gray':0,'white':0,'red':0,
                  'origin':0,'yellow':0,'green':0,'qing':0,
                  'blue':0,
                  'purple':0}
    print(img.shape)
    print(x,y,w,hi)
    start = time.time()
    CUR_PATH = os.path.dirname(__file__)
    dllPath = os.path.join(CUR_PATH, "./dll/color_recog_dll.dll")
    print(dllPath)

    #DLL
    dll = ctypes.WinDLL(dllPath)
    frame_data = np.asarray(img_hsv, dtype=np.uint8)
    frame_data = frame_data.ctypes.data_as(ctypes.c_char_p)
    print(dll.recog_color(frame_data,img.shape[0],img.shape[1], x, y, w, hi))

    end = time.time()
    print("循环运行时间:%.2f秒"%(end-start))
    max_color_hist = max(zip(color_hist.values(), color_hist.keys()))
    print(max_color_hist,color_hist)
    cv2.imshow("hsv_", img)
    cv2.imshow("hsv",img_hsv)
    cv2.waitKey()

if __name__ == '__main__':
    recog_car_color(img)
