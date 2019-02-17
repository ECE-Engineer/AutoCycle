import os
import constants
import numpy as np
from scipy import misc, ndimage
import os

ORIGINAL = 'dataset-original'
BRAND_NEW = 'dataset-resized'
FILE_NAME = 'test_img'

cwd = os.getcwd()
img_path = cwd + '/' + FILE_NAME + '.jpg'

def single_img_resize(image):
    if len(image) > 4 and image[-4:] == '.jpg':
         pic = misc.imread(image)
         dim1 = len(pic)
         dim2 = len(pic[0])
         if dim1 > dim2:
             pic = np.rot90(pic)
         picResized = resize(pic,constants.DIM1, constants.DIM2)
         misc.imsave(image, picResized)

def resize(image, dim1, dim2):
	return misc.imresize(image, (dim1, dim2))

def resize_all_in_dir():
	prepath = os.path.join(os.getcwd(), original)
	glassDir = os.path.join(prepath, 'glass')
	paperDir = os.path.join(prepath, 'paper')
	cardboardDir = os.path.join(prepath, 'cardboard')
	plasticDir = os.path.join(prepath, 'plastic')
	metalDir = os.path.join(prepath, 'metal')
	trashDir = os.path.join(prepath, 'trash')

	destPath = os.path.join(os.getcwd(), brand_new)
	try: 
		os.makedirs(destPath)
	except OSError:
		if not os.path.isdir(destPath):
			raise

	#GLASS
	file_walk(glassDir, os.path.join(destPath, 'glass'))

	#PAPER
	file_walk(paperDir, os.path.join(destPath, 'paper'))

	#CARDBOARD
	file_walk(cardboardDir, os.path.join(destPath, 'cardboard'))

	#PLASTIC
	file_walk(plasticDir, os.path.join(destPath, 'plastic'))

	#METAL
	file_walk(metalDir, os.path.join(destPath, 'metal'))

	#TRASH
	file_walk(trashDir, os.path.join(destPath, 'trash'))  

def file_walk(directory, destPath):
	try: 
		os.makedirs(destPath)
	except OSError:
		if not os.path.isdir(destPath):
			raise

	for subdir, dirs, files in os.walk(directory):
		for file in files:
			if len(file) <= 4 or file[-4:] != '.jpg':
				continue

			pic = misc.imread(os.path.join(subdir, file))
			dim1 = len(pic)
			dim2 = len(pic[0])
			if dim1 > dim2:
				pic = np.rot90(pic)

			picResized = resize(pic,constants.DIM1, constants.DIM2)
			misc.imsave(os.path.join(destPath, file), picResized)
