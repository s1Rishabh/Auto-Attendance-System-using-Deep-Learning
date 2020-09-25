import cognitive_face as CF
from global_variables import personGroupId


Base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0' # default endpoint when use free 
CF.BaseUrl.set(Base_url)
Key= '20c5c11712244ba4b340ac8bf949b8ef' # subscription key needed 
CF.Key.set(Key)
res = CF.person_group.get_status(personGroupId)
print(res)