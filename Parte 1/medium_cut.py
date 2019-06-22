import numpy as np
import matplotlib.pyplot as plt

import argparse
import cv2



from math import floor
from scipy.spatial import distance
from itertools import product
from PIL import Image

def power_check(n):
    if n <= 0:
        return False
    else:
        return n & (n-1) == 0

parser = argparse.ArgumentParser(description='Get file directory')
parser.add_argument('file', help='file directory', type=str)
parser.add_argument('num_color', help='number of division of color', type=int)
args = parser.parse_args()

if not (power_check(args.num_color)):
    print("Número informado não é potencia de 2")
    exit()

img = cv2.imread(args.file)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
width, height = img.shape[:2]
r, g, b = cv2.split(img)

color_space = img.reshape(width*height, 3)
print(len(color_space))

r = list(r)
g = list(g)
b = list(b)

img_color = list(zip(r,g,b))




# print("r: ", r, "\ng: ", g, "\nb: ", b)

plt.imshow(img)
plt.show()

copyimage = img.copy()
