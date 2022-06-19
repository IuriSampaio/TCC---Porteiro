import face_recognition as fr
import requests
import json
import base64
import imageio
from PIL import Image
from io import BytesIO
# from engine import reconhece_face

def reconhece_face(foto):
    print(type(foto))
    # im = Image.open(B;ytesIO(base64.b64encode(url_foto)))
    # im.save('image.png', 'PNG')
#    _foto = fr.load_image_file(foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos_from_sn():

  def getImages(image_sn):
    response = imageio.imread(base_url +'/'+ image_sn['sys_name'])
    
    recogneted_image = reconhece_face(response)
    
    if (recogneted_image[0]):
      return recogneted_image[1][0]

  def getNames(image_sn):
    return image_sn['sys_name'].split('.')[0]
  
  base_url = 'https://dev97007.service-now.com'
  url = '/api/now/table/db_image?sysparm_query=category%3Dpy'
  user = 'api.api'
  pwd = 'Api12345'
  headers = {"Content-Type":"application/json","Accept":"application/json"}

  response = requests.get(base_url+url, auth=(user, pwd), headers=headers )
  if response.status_code != 200: 
      #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
      exit()

  data = response.json()
  
  def getImageFromResult(result):
    response = requests.get(base_url +'/api/now/attachment/'+result['image']+'/file', auth=(user, pwd), headers=headers)
    if response.status_code != 200:
      exit()

    print(response.text)
    recogneted_image = reconhece_face(response.text)
    
    if (recogneted_image[0]):
      return recogneted_image[1][0]

  # rostos =  map(getImageFromResult,data['result'])
  print(data)
  rostos = list(map(getImages,data['result']))
  nomes = list(map(getNames,data['result']))

  return rostos, nomes
