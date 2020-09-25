import sys
import os, time
import urllib # this library is used to open url links 
import cognitive_face as CF
import urllib
import sqlite3
from global_variables import personGroupId 


Base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0' # default endpoint when use free 
CF.BaseUrl.set(Base_url)
Key= '20c5c11712244ba4b340ac8bf949b8ef' # subscription key needed 
CF.Key.set(Key)

def get_person_id():
    person_id = ''
    extractId = str(sys.argv[1])[-2:]
    connect = sqlite3.connect("face-database.db")
    c = connect.cursor()
    cmd="select * from students where ID = "+extractId 
    c.execute(cmd)
    row = c.fetchone()
    print(rowa)
    person_id = row[3]
    connect.close()
    return person_id
    
get_person_id() 