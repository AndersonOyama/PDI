import argparse
import cv2
import numpy as np



def slow_mode(width, height, mask, img):
    output = cv2.copy(img)
    for i in range(1,width-1,1):
        for j in range(1,height-1,1):
            print("")
    return




parser = argparse.ArgumentParser(description='Get file directory')
parser.add_argument('file', help='file directory', type=str)
parser.add_argument('run_type', help='Select the mode to run. 1 = Slow ,2 = Fast', type=int)
args = parser.parse_args()

img = cv2.imread(args.file,1)
img = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_CONSTANT,value=[0,0,0])
width, height = img.shape[:2]
with open('mask.txt', 'r') as f:
    mask = [[float(num) for num in line.split(',')] for line in f]
print(list(mask))
if (mask[2][2] == None):
    print("Tamanho da mascara maior que 3x3")



if (args.run_type == 1):
    slow_mode(width, height, mask, img)
