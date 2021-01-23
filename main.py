import os
from os import listdir
import sys
sys.path.append('/home/niranth/Desktop/projects/datasets/cmu')
path = '/home/niranth/Desktop/projects/datasets/cmu'
import numpy as np
import cv2
import glob
import scipy.io
runs = listdir(path+'/train')

for i in runs:
	print(i)
	for seq_name in listdir(path+'/train/'+i):
		print(seq_name)
		for k in listdir(path+'/train/'+i+'/'+seq_name):
			print(k)
			for file in glob.glob('*info.mat'):
				print(file)
				import pdb; pdb.set_trace()
				path_main = path+'/train/'+i+'/'+seq_name+'/'
				mat = scipy.io.loadmat(path_main + file)
				video_path = path_main + mat['sequence']+'.mp4'
				cap = cv2.VideoCapture(video_path)
				success = 1
				count = 0 
				while success: 
					success, image = cap.read() 
					cv2.imwrite("/home/niranth/Desktop/projects/datasets/surreal/images/"+mat['sequence']+'_'+str(count)+".jpg" % count, image)
					count += 1

				break
			break
		break
	break


			# cap = cv2.VideoCapture(0)

			# fourcc = cv2.VideoWriter_fourcc(*'XVID')
			# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

			# while(cap.isOpened()):
			#     ret, frame = cap.read()
			#     if ret==True: