import numpy as np
import math
import cv2
import argparse

COLOR_SPACE = 255
RED = []
GREEN = []
BLUE = []


parser = argparse.ArgumentParser(description='Get file directory')
parser.add_argument('file', help='file directory', type=str)
parser.add_argument('num_div', help='number of division', type=int)
args = parser.parse_args()


def partition_mul(n):
    div = []
    d = 2
    while n > 1:
    	if n%d == 0:
    		n = n/d
    		div.append(d)
    	else:
    		d += 1
    while len(div) > 3:
        temp = div[0]*div[1]
        del div[0]
        del div[0]
        div.append(temp)
        div.sort()
    if(len(num) < 3 and len(num) >= 2):
        num.append(1)
    elif (len(num)<=1 and len(num)>=0):
        num.append(1)
        num.append(1)
    return div


def distance_color():
    a = 0

img = cv2.imread(args.file, 1)
num = []
num = partition_mul(args.num_div)

print(num)

RED.append(COLOR_SPACE//(num[0]+1))
GREEN.append(COLOR_SPACE//(num[1]+1))
BLUE.append(COLOR_SPACE//num[2]+1)

for i, j in enumerate(num):
    

print(RED)
# cv2.imshow('imagem', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
