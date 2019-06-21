import numpy as np
import argparse

from math import floor
from scipy.spatial import distance
from itertools import product
from PIL import Image

parser = argparse.ArgumentParser(description='Get file directory')
parser.add_argument('file', help='file directory', type=str)
parser.add_argument('num_color', help='number of division of color', type=int)
args = parser.parse_args()



img = cv2.imread(args.file)
