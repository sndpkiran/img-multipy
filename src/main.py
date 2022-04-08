import cv2 as cv
import numpy as np
import os
import time
import json
from multiprocessing import Process

SIGNS_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resources\\signs"
ICONS_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resources\\icons"
BGS_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resources\\bg"
JSON_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resources\\json"
PROCESSED_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\images_generated"
CURR_PATH = PROCESSED_PATH + "\\RESULTS_" + str(int(time.time()))
GEN_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\images_generated\\RESULTS_1647818628"

def overlay(img, icon, x, y):
	temp_img = np.copy(img)
	i, j = x, y
	i_end, j_end = i + icon.shape[0], j + icon.shape[1]
	a, b = 0, 0
	print(icon.shape)
	print(i_end, j_end)

	while i < i_end:
		j = y
		b = 0
		while j < j_end:
			if icon[a][b][0] <= 8 and icon[a][b][1] <= 8 and icon[a][b][2] <= 8:
				temp_img[i][j][0] = icon[a][b][0]
				temp_img[i][j][1] = icon[a][b][1]
				temp_img[i][j][2] = icon[a][b][2]
			j += 1
			b += 1

		i += 1
		a += 1

	gen_path = CURR_PATH + "\\IMG_" + str(time.time()) + ".jpg"
	print(gen_path)
	cv.imwrite(gen_path, temp_img)

def overlay_icons(imgfile, offset_index):
	icon_list= os.listdir(ICONS_PATH)
	print(offset_index)
	img = cv.imread(GEN_PATH + "\\" + imgfile)

	icon_pos_json = json.load(open(JSON_PATH + "\\sl_offsets.json"))
	x_pos, y_pos = 0, 0
	# for pos in icon_pos_json["offsets"]:
	# 	if pos["sign"] == imgfile:
	# 		x_pos = pos["x_offset"]
	# 		y_pos = pos["y_offset"]

	x_pos, y_pos = icon_pos_json["offsets"][offset_index]["x_offset"], icon_pos_json["offsets"][offset_index]["y_offset"]
	for icon in icon_list:
		ic_img = cv.imread(ICONS_PATH + "\\" + icon)
		# print(icon)
		overlay(img, ic_img, x_pos, y_pos)

def change_bg(img, c, res):
	temp_img = np.copy(img)
	for x_pos in  range(0, res[0]):
		for y_pos in range(0, res[1]):
			if temp_img[x_pos][y_pos][0] == 0 and temp_img[x_pos][y_pos][0] == 0 and temp_img[x_pos][y_pos][0] == 0:
				temp_img[x_pos][y_pos][0] = c["b"]
				temp_img[x_pos][y_pos][1] = c["g"]
				temp_img[x_pos][y_pos][2] = c["r"]

	gen_path = CURR_PATH + "\\IMG_" + str(time.time()) + ".jpg"
	cv.imwrite(gen_path, temp_img)


def process_image(imgfile):
	print("Processing {} ...".format(imgfile))
	img = cv.imread(SIGNS_PATH + "\\" + imgfile)
	res = img.shape

	colors = json.loads(open(JSON_PATH + "\\colors.json").read())

	count = 0
	for c in colors["bg"]:
		print("Changing bg color to (r, g, b) = {}".format(c))
		# Process(target=change_bg,  args=(img, c, res,)).start()
		change_bg(img, c, res)

def overlay_sign_over_bg(imgfile):
	bg_list = os.listdir(BGS_PATH)
	temp_img = np.copy(cv.imread(SIGNS_PATH + "\\" + imgfile))
	res = temp_img.shape

	for bg in bg_list:
		temp_bg = np.copy(cv.imread(BGS_PATH + "\\" + bg))
		for i in range(res[0]):
			for j in range(res[1]):
				if temp_img[i][j][0] != 0 and temp_img[i][j][1] != 0 and temp_img[i][j][2] != 0:
					temp_bg[i][j][0] = temp_img[i][j][0]
					temp_bg[i][j][1] = temp_img[i][j][1]
					temp_bg[i][j][2] = temp_img[i][j][2]
		gen_path = CURR_PATH + "\\IMG_" + str(time.time()) + ".jpg"
		print("Saving ", gen_path)
		cv.imwrite(gen_path, temp_bg)

def main():
	imglist = os.listdir(SIGNS_PATH)

	try:
		os.mkdir(PROCESSED_PATH)
	except FileExistsError as e:
		print("Directory already exists")

	try:
		os.mkdir(CURR_PATH)
	except FileExistsError as e:
		print("Directory already exists")

	print("Results will be available in: {}".format(CURR_PATH))
	# for imgfile in imglist:
	# 	process_image(imgfile)
	# 	# Process(target=process_image, args=(imgfile,)).start()
	# 	print("---------------------------------------------------------")

	# for imgfile in imglist:
	# 	overlay_sign_over_bg(imgfile)
	# 	# Process(target=process_image, args=(imgfile,)).start()
	# 	print("---------------------------------------------------------")

	# gen_img_list = os.listdir(CURR_PATH)
	# gen_img_list = os.listdir(SIGNS_PATH)
	gen_img_list = os.listdir(GEN_PATH)
	count = 0
	for gen_img in  gen_img_list:
		overlay_icons(gen_img, (count//10))
		count += 1

if __name__ == '__main__':
	# freeze_support()
	main()