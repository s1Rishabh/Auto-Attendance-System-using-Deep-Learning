import sys
import cognitive_face as CF
from global_variables import personGroupId # the file that has been created by me 
import sqlite3


#this function will be used to add the new person which is not available in the database
#how would you verify whether the student is already registered or not 
#here we are using -  Azure Cognitive Services Face API - to detect faces and extract various facial landmarks such as position of eyes , nose and more
#then we can use the images to re-identify them 
Base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0' # default endpoint when use free 
CF.BaseUrl.set(Base_url)
Key= '20c5c11712244ba4b340ac8bf949b8ef' # subscription key needed 
CF.Key.set(Key)    # command is given as python3 create_person.py user13.  - argvlist ('create_person.py','user13')
if len(sys.argv) is not 1:  # sys.srgv is list in python that contains command line arguments passed to the scripts, u can use indexing also 
   res=CF.person.create(personGroupId,str(sys.argv[1]))  # 'personId': '24c31156-85e0-4328-ae94-62157687f7f0' - providing a dictionary added to the DB
   print(res)                                            # for particular student entry 
   extractId=str(sys.argv[1])[-2:]   # extracting the roll number like - 2016UIT2579 - then 79 
   #print(extractId)
   connect=sqlite3.connect("face-database.db")
   cmd="select * from students where ID="+extractId
   cursor=connect.execute(cmd) # it gives the details of student with corresponding id
   isRecordExist=0
   #row=cursor.fetchone()
   #print(row)
   #print(extractId)
   for row in cursor:
   	  isRecordExist=1
   if isRecordExist==1 : # if it exist then need to update its details. We need to create is unique personID only if it is already existed in student DB
      #print("yes")
      connect.execute("update students set personId = ? where ID = ?",(res['personId'], extractId))
   connect.commit()
   connect.close()
   print("Person ID successfully added to the database")




