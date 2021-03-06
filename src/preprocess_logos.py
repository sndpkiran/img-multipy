import cv2 as cv
import numpy as np
import os
import time
import json

ICONS_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resources\\icons"
SIGNS_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resources\\signs"
JSON_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resources\\json"
PROCESSED_PATH = "C:\\Users\\sndpk\\Desktop\\img-multipy\\resized_logos"

def preprocess():
	resize_res = (1080, 1080)
	icon_list= os.listdir(SIGNS_PATH)

	try:
		os.mkdir(PROCESSED_PATH)
	except FileExistsError as e:
		print("Directory already exists")

	for icon in icon_list:
		ic_img = cv.imread(SIGNS_PATH + "\\" + icon)
		ic_resized = cv.resize(ic_img, resize_res, cv.INTER_LINEAR)
		cv.imwrite(PROCESSED_PATH + "\\" + icon.split(".")[0] + ".png", ic_resized)

preprocess()