import cv2
import dlib
import os
import sys
import sqlite3

#cam = cv2.VideoCapture(1)
detector = dlib.get_frontal_face_detector()
# argument passed like this - python3 detect.py ./pics/test1.jpg
if len(sys.argv) is not 1:
	img = cv2.imread(str(sys.argv[1]))
	dets = detector(img, 1) # it gives two tuples for every face detected containing extreme coordinates 
	print(dets)
	if not os.path.exists('./Cropped_faces'):  # create a directory where all the detected faces pics will be stored 
		os.makedirs('./Cropped_faces')
	print ("detected = " + str(len(dets)))  # determing the total number of faces detected 
	for i, d in enumerate(dets):
   		cv2.imwrite('./Cropped_faces/face' + str(i + 1) + '.jpg', img[d.top():d.bottom(), d.left():d.right()]) 
   		                                                                # d will contains the tupples of that face
# the attendance photo provided will be saved in the pics folder, from there faces will be cropped using dlib and then saved to cropped_faces directory
