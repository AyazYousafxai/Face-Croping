from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN
import cv2
from imutils import paths  
import numpy as np
import os, errno
def extract_face(filename, required_size=(160, 160)):
	img=cv2.imread(filename)
	pixels = np.array(img)
	detector = MTCNN()
	results = detector.detect_faces(pixels)
	try:
        	x1, y1, width, height = results[0]['box']
        	# bug fix
        	x1, y1 = abs(x1), abs(y1)
        	x2, y2 = x1 + width, y1 + height
        	face = pixels[y1:y2, x1:x2]
        	image = Image.fromarray(face)
        	face_array = asarray(image)
        	return face_array
	except:
            pass

  
folders=list(paths.list_images('folderpath')) #path of images folder
count=0
crop='crop'
for i,filename in enumerate(folders):
    folder = filename.split(os.path.sep)[-2].split(".")[0]
    imageName = filename.split(os.path.sep)[-1].split(".")[0]
    try:
        os.makedirs(crop+'/'+folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    folder_path=crop+'/'+folder						
    face=extract_face(filename)
    try:
					count=count+1
					pathwrite=folder_path+'/'+imageName+'crop'+str(count)+'.jpg'
					cv2.imwrite(pathwrite,face)
					print('write',pathwrite)
    except:
					pass        
