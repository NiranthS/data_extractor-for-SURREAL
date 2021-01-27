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

import json
runs = listdir(path+'/train')
main_count = 0
anno = []

# for i in runs:
# 	# print(i)
# import pdb; pdb.set_trace()
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
img_count = 0
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
			del mat['__globals__']
			del mat['__version__']
			del mat['__header__']

			while success: 
				success, image = cap.read() 
				
				if count<2:
					cv2.imwrite("/home/niranth/Desktop/projects/datasets/surreal/images2/"+i+'_'+mat['sequence'][0]+'_'+str(count)+".jpg" , image)
					json_line = mat.copy()
					json_line['img_paths'] = i+'_'+mat['sequence'][0]+'_'+str(count)+".jpg"
					json_line['self_joints'] = []
					# pdb.set_trace()
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
					# for key in json_line.keys():
					# 	print(type(json_line[key]), key )
						# if key == 'shape':
						# 	break

					anno.append(json_line)
					json_line['sequence'] = json_line['sequence'].tolist()
					json_line['clipNo'] = json_line['clipNo'].tolist()
					json_line['source'] = json_line['source'].tolist()
					json_line['bg'] = json_line['bg'].tolist()
					json_line['gender'] = json_line['gender'].tolist()
					json_line['light'] = json_line['light'].tolist()
					json_line['stride'] = json_line['stride'].tolist()
					json_line['camDist'] = json_line['camDist'].tolist()
					json_line['camLoc'] = json_line['camLoc'].tolist()
					json_line['joints2D'] = json_line['joints2D'].tolist()
					json_line['joints3D'] = json_line['joints3D'].tolist()
					json_line['pose'] = json_line['pose'].tolist()
					json_line['zrot'] = json_line['zrot'].tolist()
					json_line['cloth'] = json_line['cloth'].tolist()
					json_line['shape'] = json_line['shape'].tolist()
					json_line['img_paths'] = list(json_line['img_paths'])

					# for key in json_line.keys():
					# 	print(type(json_line[key]), key )

					img_count += 1

				if success == 0:
					count -= 1
					cv2.imwrite("/home/niranth/Desktop/projects/datasets/surreal/images2/"+i+'_'+mat['sequence'][0]+'_'+str(count)+".jpg" , img_copy)
					json_line = mat.copy()
					json_line['img_paths'] = i+'_'+mat['sequence'][0]+'_'+str(count)+".jpg"
					json_line['self_joints'] = []
					# pdb.set_trace()
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
					# for key in json_line.keys():
					# 	print(type(json_line[key]), key )
						# if key == 'shape':
						# 	break

					anno.append(json_line)
					json_line['sequence'] = json_line['sequence'].tolist()
					json_line['clipNo'] = json_line['clipNo'].tolist()
					json_line['source'] = json_line['source'].tolist()
					json_line['bg'] = json_line['bg'].tolist()
					json_line['gender'] = json_line['gender'].tolist()
					json_line['light'] = json_line['light'].tolist()
					json_line['stride'] = json_line['stride'].tolist()
					json_line['camDist'] = json_line['camDist'].tolist()
					json_line['camLoc'] = json_line['camLoc'].tolist()
					json_line['joints2D'] = json_line['joints2D'].tolist()
					json_line['joints3D'] = json_line['joints3D'].tolist()
					json_line['pose'] = json_line['pose'].tolist()
					json_line['zrot'] = json_line['zrot'].tolist()
					json_line['cloth'] = json_line['cloth'].tolist()
					json_line['shape'] = json_line['shape'].tolist()
					json_line['img_paths'] = list(json_line['img_paths'])


					break
				img_copy = image
				count += 1
			main_count += count
			print((main_count*100)/5342090)
		# # import pdb; pdb.set_trace()
		# for key in anno[0]:
		# 	print(type(anno[0][key]), 'final')

		print((main_count*100)/5342090)
		if file_num%20 == 0:
			print(image_count)
			print('saving...')
			
			with open("/home/niranth/Desktop/projects/datasets/surreal/annotations_surreal2.json", "w") as fp:
				json.dump(anno, fp)
			file_num=0
	print('run end saving...')
			
	with open("/home/niranth/Desktop/projects/datasets/surreal/annotations_surreal2.json", "w") as fp:
		json.dump(anno, fp)
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