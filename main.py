import os
from os import listdir
import sys
sys.path.append('/home/niranth/Desktop/projects/datasets/cmu')

runs = listdir('train')

for i in runs:
	print(i)