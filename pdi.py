import numpy as np
import math
import cv2
import argparse

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
        # print(temp)
        del div[0]
        del div[0]
        div.append(temp)
        div.sort()
        # print(len(div))
    return div






img = cv2.imread(args.file, 1)
num = []
num = partition_mul(args.num_div)
if(len(num) < 3 and len(num) >= 2):
    num.append(1)
elif (len(num)<=1 and len(num)>=0):
    num.append(1)
    num.append(1)
print(num)

# cv2.imshow('imagem', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
