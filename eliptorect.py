# REFERENCE FROM https://github.com/ankanbansal/fddb-for-yolo/blob/master/convertEllipseToRect.py
# Thank to Author ankanbansal

import sys, os
import numpy as np
from math import *
import math
from PIL import Image
import cv2
import os


def filterCoordinate(c,m):
    if c < 0:
    	return 0
    elif c > m:
    	return m
    else:
    	return c

def convertEllipseToRect(ellipseFilename, cnt):
    
    with open(ellipseFilename) as f:
            lines = [line.rstrip('\n') for line in f]
    
    i = 0
    while i < len(lines):
        img_file = lines[i] + '.jpg'
        num_faces = int(lines[i+1])
        ip = os.path.isfile(img_file)   
        if(ip == True):
            out_img_file = 'FDDB_DATASET_IMAGES_GROUND_TRUTH/fddb_images/' + str(cnt) + '.jpg'
            out_gt_file = 'FDDB_DATASET_IMAGES_GROUND_TRUTH/ground_truth_rect/' + str(cnt) + '.txt'
            f = open(out_gt_file,'wb')
            cnt +=1
            img = Image.open(img_file)
            img_cv=cv2.imread(img_file)
            cv2.imwrite(out_img_file,img_cv)
            w = img.size[0]
            h = img.size[1]
            for j in range(num_faces):
                ellipse = lines[i+2+j].split()[0:5]
                a = float(ellipse[0])
                b = float(ellipse[1])
                angle = float(ellipse[2])
                centre_x = float(ellipse[3])
                centre_y = float(ellipse[4])
                
                tan_t = -(b/a)*tan(angle)
                t = atan(tan_t)
                x1 = centre_x + (a*cos(t)*cos(angle) - b*sin(t)*sin(angle))
                x2 = centre_x + (a*cos(t+pi)*cos(angle) - b*sin(t+pi)*sin(angle))
                x_max = filterCoordinate(max(x1,x2),w)
                x_min = filterCoordinate(min(x1,x2),w)
                
                if tan(angle) != 0:
                    tan_t = (b/a)*(1/tan(angle))
                else:
                    tan_t = (b/a)*(1/(tan(angle)+0.0001))
                t = atan(tan_t)
                y1 = centre_y + (b*sin(t)*cos(angle) + a*cos(t)*sin(angle))
                y2 = centre_y + (b*sin(t+pi)*cos(angle) + a*cos(t+pi)*sin(angle))
                y_max = filterCoordinate(max(y1,y2),h)
                y_min = filterCoordinate(min(y1,y2),h)
            
                text = 'face' + ' ' + str(x_min) + ' ' + str(y_min) + ' ' + str(x_max) + ' ' + str(y_max) + '\n'
                f.write(text)
        i = i + num_faces + 2
    f.close()
    return cnt

def main():
    cnt = 0
    for i in range(1,11):
        fileElliName="FDDB-fold-%02d-ellipseList.txt" %i
        fileRectName="FDDB-fold-%02d-rectList.txt" %i

        ellipseFilename = 'FDDB-folds/'+fileElliName
        
        cnt = convertEllipseToRect(ellipseFilename, cnt)
        print(fileElliName + ' completed')

if __name__=='__main__':
    main()
