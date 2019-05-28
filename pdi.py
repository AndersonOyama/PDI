import numpy as np
import math
import cv2
import argparse

from math import floor
from itertools import product

COLOR_SPACE = 255
RED = []
GREEN = []
BLUE = []


parser = argparse.ArgumentParser(description='Get file directory')
parser.add_argument('file', help='file directory', type=str)
parser.add_argument('num_div', help='number of division', type=int)
args = parser.parse_args()

#ENCONTRA OS VALORES DECOMPOSTO DO SPECTRO DE CORES PASSADO
def partition_mul():
    div = []
    d = 2
    while args.num_div > 1:
    	if args.num_div%d == 0:
    		args.num_div = args.num_div/d
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

def distance_cal():
    return


#DEFINIÇÃO DOS PONTOS DE CADA COR.
def color_def(value, n):
    color_div = []
    for i in range (0,n):
        color_div.append(floor((i+1)*value))
    return color_div

img = cv2.imread(args.file, 1)
num = []
coordenates = []
num = partition_mul()


RED = color_def(abs(COLOR_SPACE/(num[0]+1)), num[0]) #a
GREEN = color_def(abs(COLOR_SPACE/(num[1]+1)), num[1]) #b
BLUE = color_def(abs(COLOR_SPACE/(num[2]+1)), num[2]) #c


coordenates = list(product(RED, BLUE, GREEN, repeat = 1))

img[np.where((img == [255,255,255]).all(axis=2))] = [0,0,0]
cv2.imwrite('temp.png', img)
# cv2.imshow('imagem', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
