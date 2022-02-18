import cv2 as cv
import numpy as np
import os
import time
import json
import multiprocessing as mp

SIGNS_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resources\\signs"
ICONS_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resources\\icons"
JSON_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resources\\json"
PROCESSED_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\images_generated"
CURR_PATH = PROCESSED_PATH + "\\RESULTS_" + str(int(time.time()))

def overlay_icons(imgfile):
	icon_list= os.listdir(ICONS_PATH)
	img = cv.imread(SIGNS_PATH + "\\" + imgfile)
	for icon in icon_list:
		ic_img = cv.imread(ICONS_PATH + "\\" + icon)

def process_image(imgfile):
	print("Processing {} ...".format(imgfile))
	img = cv.imread(SIGNS_PATH + "\\" + imgfile)
	res = img.shape

	try:
		os.mkdir(CURR_PATH)
	except FileExistsError as e:
		print("Directory already exists")

	colors = json.loads(open(JSON_PATH + "\\colors.json").read())

	count = 0
	for c in colors["bg"]:
		temp_img = np.copy(img)
		print("Changing bg color to (r, g, b) = {}".format(c))	

		for x_pos in  range(0, res[0]):
			for y_pos in range(0, res[1]):
				if temp_img[x_pos][y_pos][0] > 240 and temp_img[x_pos][y_pos][0] > 240 and temp_img[x_pos][y_pos][0] > 240:
					temp_img[x_pos][y_pos][0] = c["b"]
					temp_img[x_pos][y_pos][1] = c["g"]
					temp_img[x_pos][y_pos][2] = c["r"]

		gen_path = CURR_PATH + "\\IMG_" + str(int(time.time())) + ".jpg"
		cv.imwrite(gen_path, temp_img)

def main():
	imglist = os.listdir(SIGNS_PATH)

	try:
		os.mkdir(PROCESSED_PATH)
	except FileExistsError as e:
		print("Directory already exists")

	print("Results will be available in: {}".format(CURR_PATH))
	for imgfile in imglist:
		process_image(imgfile)
		overlay_icons(imgfile)
		print("---------------------------------------------------------") 

main()