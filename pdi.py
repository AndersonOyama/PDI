import numpy as np
import argparse

from math import floor
from scipy.spatial import distance
from itertools import product
from PIL import Image

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

    if(len(div) < 3 and len(div) >= 2):
        div.append(1)
    elif (len(div) < 2 and len(div) >= 1):
        div.append(1)
        div.append(1)
    elif (len(div) <= 0):
        div.append(1)
        div.append(1)
        div.append(1)
    return div


def distance_cal(color_spec, color):
    dst = float('inf')
    coordenate_color = 1
    for i, val in enumerate(color_spec):
        temp = distance.euclidean(val, color)
        if (dst > temp):
            dst = temp
            coordenate_color = i
    return color_spec[coordenate_color]

#DEFINIÇÃO DOS PONTOS DE CADA COR.
def color_def(value, n):
    color_div = []
    for i in range (0,n):
        color_div.append(floor((i+1)*value))
    return color_div


im = Image.open(args.file)
pix = im.load()

num = []
coordenates = []
num = partition_mul()

RED = color_def(abs(COLOR_SPACE/(num[0]+1)), num[0]) #a
GREEN = color_def(abs(COLOR_SPACE/(num[1]+1)), num[1]) #b
BLUE = color_def(abs(COLOR_SPACE/(num[2]+1)), num[2]) #c


coordenates = list(product(RED, GREEN, BLUE, repeat = 1))

weigh = im.size[0]
height = im.size[1]


for x in range(0, weigh):
    for y in range(0, height):

        pix[x,y] = distance_cal(coordenates, pix[x,y])

im.show()
nome_output = args.file.replace(".", "_colored.")
im.save(nome_output)


# cv2.imshow('imagem', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
