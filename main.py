import os
from os import listdir
import sys
sys.path.append('/home/niranth/Desktop/projects/datasets/cmu')
path = '/home/niranth/Desktop/projects/datasets/cmu'
import numpy as np
import cv2
import glob
import scipy.io
import pickle
runs = listdir(path+'/train')
main_count = 0
anno = []

# for i in runs:
# 	# print(i)
import pdb; pdb.set_trace()
# 	for seq_name in listdir(path+'/train/'+i):
		
# 		# import pdb; pdb.set_trace()
# 		# for k in listdir(path+'/train/'+i+'/'+seq_name):
# 		# 	# print(k)
# 		for file in glob.glob(path+'/train/'+i+'/'+seq_name+'/'+'*info.mat'):
# 			# print(file)
# 			# import pdb; pdb.set_trace()
# 			path_main = path+'/train/'+i+'/'+seq_name+'/'
# 			mat = scipy.io.loadmat(file)
# 			video_path = path_main + mat['sequence'][0]+'.mp4'
# 			cap = cv2.VideoCapture(video_path)
# 			success = 1
# 			count = 0
# 			# json_line = mat
# 			# del json_line['__globals__']
# 			# del json_line['__version__']
# 			# del json_line['__header__']
# 			while success: 
# 				success, image = cap.read() 
# 				if success == 0:
# 					break

# 				main_count += 1
# 				print(main_count)

				# count += 1
			# main_count += count
		# import pickle
		# with open("/home/niranth/Desktop/projects/datasets/surreal/annotations_surreal.pickle", "wb") as fp:
		# 	pickle.dump(anno, fp)
file_num = 0
for i in runs:
	print(i)
	for seq_name in listdir(path+'/train/'+i):
		print(i)
		print(seq_name)
		# for k in listdir(path+'/train/'+i+'/'+seq_name):
		# 	# print(k)
		file_num+=1
		for file in glob.glob(path+'/train/'+i+'/'+seq_name+'/'+'*info.mat'):
			# print(file)
			# import pdb; pdb.set_trace()
			path_main = path+'/train/'+i+'/'+seq_name+'/'
			mat = scipy.io.loadmat(file)
			video_path = path_main + mat['sequence'][0]+'.mp4'
			cap = cv2.VideoCapture(video_path)
			success = 1
			count = 0
			json_line = mat
			del json_line['__globals__']
			del json_line['__version__']
			del json_line['__header__']
			while success: 
				success, image = cap.read() 
				if success == 0:
					break
				if count<3 or count % 20 == 0:
					cv2.imwrite("/home/niranth/Desktop/projects/datasets/surreal/images2/"+i+'_'+mat['sequence'][0]+'_'+str(count)+".jpg" , image)
					json_line['img_paths'] = i+'_'+mat['sequence'][0]+'_'+str(count)+".jpg"
					json_line['self_joints'] = []

					for jt in range(24):
						if len(json_line['joints2D'].shape) < 3:
							json_line['self_joints'].append([json_line['joints2D'][0, jt], json_line['joints2D'][1, jt], 1.0])
						else:
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
					for key in json_line.keys():
						print(type(json_line[key]) == 'numpy.ndarray')

					anno.append(json_line)

				count += 1
			main_count += count
			# print((main_count*100)/5342090)
		print((main_count*100)/5342090)
		if file_num%120 == 0:
			print('saving...')
			
			with open("/home/niranth/Desktop/projects/datasets/surreal/annotations_surreal2.pickle", "wb") as fp:
				pickle.dump(anno, fp)
			file_num=0
	print('run end saving...')
			
	with open("/home/niranth/Desktop/projects/datasets/surreal/annotations_surreal2.pickle", "wb") as fp:
		pickle.dump(anno, fp)
	file_num=0
# import json
# 
# with open('/home/niranth/Desktop/projects/datasets/surreal/annotations_surreal.json', 'w') as f:
# 	json.dump(anno,f)
# scipy.io.savemat("/home/niranth/Desktop/projects/datasets/surreal/annotations_surreal.mat", mdic)

# import pickle
# with open("/home/niranth/Desktop/projects/datasets/surreal/annotations_surreal2.pickle", "wb") as fp:
# 	pickle.dump(anno, fp)
			# cap = cv2.VideoCapture(0)

			# fourcc = cv2.VideoWriter_fourcc(*'XVID')
			# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

			# while(cap.isOpened()):
			#     ret, frame = cap.read()
			#     if ret==True: