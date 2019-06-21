import numpy as np
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
copyimage = img.copy()
