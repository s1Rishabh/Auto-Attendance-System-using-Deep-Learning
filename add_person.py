import sys
import cv2  #computer vision library 
import numpy as np
import sqlite3  #database server 
import dlib    #DLib is a C++ library/toolkit that contains machine learning algorithms, including computer vision
import os  # os module helps to interact with operating system on which python is running
           # helps to interact with file systems 

def InsertOrUpdate(ID, Name, Roll) :                                            # this function is for database
    connect = sqlite3.connect("face-database.db",timeout=10)                               # connecting to the database
    cmd = "select * from students where ID = " + ID                             # selecting the row of an id into consideration
    cursor = connect.execute(cmd)                                               #executing the command and saving results in cursor 
    isRecordExist = 0
    for row in cursor:  #the cursor will have only one row                      # checking wheather the id exist or not
        isRecordExist = 1
    #print(isRecordExist)
    if (isRecordExist == 1):                                                    # updating name and roll no
        connect.execute("update students set Name = ? where ID = ?",(Name, ID)) # executing these two commands
        connect.execute("update students set Roll = ? where ID = ?",(Roll, ID))
    else:                                                                       # insering a new student data
        connect.execute("insert into students(ID,Name,Roll) values(?, ?, ?)",(ID,Name,Roll))
    connect.commit()                                                            # commiting into the database
    connect.close()    
#-------------------------------------------------------------------------------------------------------------#
Name = input("Enter the student's Name: ")  #raw_input changed to simply input in python3 
Roll = input("Enter the student's Roll: ") # this would be string 
# raw_input stores the input as it is presented 
ID = Roll[-2:]  # last two digits of the string are captured
InsertOrUpdate(ID,Name,Roll)  # till now we have updated or inserted new entry
#-------------------------------------------------------------------------------------------------------------#
folderName = "user" + ID  #remember ID is an string - string concatenation      # creating the person or user folder
folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "database/"+folderName) #where to create folder
# os.path.realpath(__file__) -- /Users/adityaatri/Desktop/Projects/attendance_system/add_person.py     #returned the path of the file name 
# os.path.dirname(os.path.realpath(__file__)) /Users/adityaatri/Desktop/Projects/attendance_system/
# os.path.join(Address1+Address2) --- /attendance_system/database/user79

if not os.path.exists(folderPath):  # if there is no such path exist - it means it will automatically creates 'database' folder for me
    os.makedirs(folderPath)

# face detection is used through the dlib
count_faces=0
size = 4
webcam = cv2.VideoCapture(0) #Use camera 0 - external camera 
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
while True:
    (rval, im) = webcam.read()
    im=cv2.flip(im,1,0) #Flip to act as a mirror

    # Resize the image to speed up detection
    mini = cv2.resize(im,(im.shape[1]//size, im.shape[0]//size))

    # detect MultiScale / faces 
    faces = classifier.detectMultiScale(mini)
    # Draw rectangles around each face
    for f in faces:
        count_faces+=1
        (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
        cv2.rectangle(im, (x, y), (x + w, y + h),(0,255,0),thickness=4)
        #Save just the rectangle faces in SubRecFaces
        sub_face = im[y:y+h, x:x+w]
        cv2.imwrite(folderPath + "/User." + ID + "_" + str(count_faces) + ".jpg", sub_face)

    # Show the image
    #cv2.imshow('Web_Cam_Capture', im)
    if(count_faces >= 20):
         break 
webcam.release()                                                                   # turning the webcam off
cv2.destroyAllWindows()








