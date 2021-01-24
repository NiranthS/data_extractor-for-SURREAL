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
main_count = 0
anno = []
for i in runs:
	print(i)
	for seq_name in listdir(path+'/train/'+i):
		print(seq_name)
		for k in listdir(path+'/train/'+i+'/'+seq_name):
			# print(k)
			for file in glob.glob(path+'/train/'+i+'/'+seq_name+'/'+'*info.mat'):
				# print(file)
				import pdb; pdb.set_trace()
				path_main = path+'/train/'+i+'/'+seq_name+'/'
				mat = scipy.io.loadmat(file)
				video_path = path_main + mat['sequence'][0]+'.mp4'
				cap = cv2.VideoCapture(video_path)
				success = 1
				count = 0
				json_line = mat

				while success: 
					success, image = cap.read() 
					if success == 0:
						break

					cv2.imwrite("/home/niranth/Desktop/projects/datasets/surreal/images/"+i+'_'+mat['sequence'][0]+'_'+str(count)+".jpg" , image)
					json_line['img_paths'] = i+'_'+mat['sequence'][0]+'_'+str(count)+".jpg"
					json_line['self_joints'] = []
					for jt in range(24):
						json_line['self_joints'].append([json_line['joints2D'][0, jt, count], json_line['joints2D'][1, jt, count], 1.0])
					json_line['isValidation'] = 0.0
					json_line['numOtherPeople'] = 0.0
					json_line['people_index'] = 0.0
					json_line['img_width'] = 320.0
					json_line['img_height'] = 240.0
					json_line['scale_provided'] = 0.9
					json_line['objpos'] = [160.0, 120.0]
					json_line['pose_parameters'] = json_line['pose'][:,count].tolist()
					json_line['shape_parameters'] = json_line['shape'][:,count].tolist()
					del json_line['__header__']
					del json_line['__version__']
					del json_line['__globals__']

					anno.append(json_line)

					count += 1
				main_count += count
				break
			break
		break
	break

import json

with open('/home/niranth/Desktop/projects/datasets/surreal/annotations_surreal.json', 'w') as f:
	json.dump(anno,f)
			# cap = cv2.VideoCapture(0)

			# fourcc = cv2.VideoWriter_fourcc(*'XVID')
			# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

			# while(cap.isOpened()):
			#     ret, frame = cap.read()
			#     if ret==True: