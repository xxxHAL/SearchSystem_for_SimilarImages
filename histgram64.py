#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

def histogram(img):

	histogram = [0]
	height,width,channels = img.shape[:3]
	print("width: " + str(width))
	print("height: " + str(height))
	print("dtype: " + str(img.dtype))

	histogram = [0 for i in range(64)]

	for y in range(height):
	    for x in range(width):
	    	count = 0
	        blue = img.item(y,x,0)
	        green = img.item(y,x,1)
	        red = img.item(y,x,2)

	        bin = rgb2bin(red,green,blue);
	        histogram[bin] += 1
	return histogram

	#for i in range(len(histogram)):
		#print ('No.' + str(i))
		#print histogram[i]

def rgb2bin(red,green,blue):

	redno = red / 64
	greenno = green / 64
	blueno = blue / 64
	bin = 16 * redno + 4 * greenno + blueno
	return bin

def file(histFile,histogram):

	f = open(histFile,'w')
	#for i in range(64):
	for i in histogram:
		f.write(str(i))
		f.write("\n")
	f.close()

if __name__ == '__main__':

	argv = sys.argv
	imageFile = argv[1]
	histFile = argv[2]
	img = cv2.imread(imageFile,cv2.IMREAD_UNCHANGED)
	output = file(histFile,histogram(img))



