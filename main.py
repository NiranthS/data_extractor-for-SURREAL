import os
from os import listdir
import sys
sys.path.append('/home/niranth/Desktop/projects/datasets/cmu')
path = '/home/niranth/Desktop/projects/datasets/cmu'
runs = listdir(path+'/train')

for i in runs:
	print(i)
	for j in listdir(path+'/train/'+i):
		print(j)