import cognitive_face as CF
from global_variables import personGroupId
import sys
# [{'personId': '1e11bb9e-a187-4755-a53d-cb51d52ef62c', 'persistedFaceIds': [], 'name': 'user57', 'userData': None}]
#  here only person is added to persongroupID..not personID is given , 'persistedFaceIDs' will be added after when add_person_faces.py is executed 
Base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0' # default endpoint when use free 
CF.BaseUrl.set(Base_url)
Key= '20c5c11712244ba4b340ac8bf949b8ef'
CF.Key.set(Key)

personGroups = CF.person_group.lists()
print(CF.person.lists(personGroupId)) 
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print(personGroupId + " already exists.")
        sys.exit()

res = CF.person_group.create(personGroupId) # if not created then i need to create the new group id 