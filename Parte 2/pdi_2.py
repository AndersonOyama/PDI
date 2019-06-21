import argparse
import cv2
import numpy as np



def slow_mode():
    img = cv2.imread(args.file, 0)
    width, height = cv2.GetSize(img)


    for i in range(width):
        for j in range(height):
            




parser = argparse.ArgumentParser(description='Get file directory')
parser.add_argument('file', help='file directory', type=str)
parser.add_argument('run_type', help='Select the mode to run. 1 = Slow ,2 = Fast', type=int)
args = parser.parse_args()





if (args.run_type == 1):
    slow_mode()
