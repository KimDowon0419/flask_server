import sys
import cv2
import numpy as np

def input(x):
    res = cv2.resize(x, dsize=(256,256),interpolation=cv2.INTER_AREA)
    cv2.waitKey()
    cv2.destroyAllWindows()
    print(res)
    return res





