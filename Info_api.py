import requests
import firebase_admin
from firebase_admin import db
import datetime



def dbs():
    ab = firebase_admin.credentials.Certificate('firebase.json')
    app = firebase_admin.initialize_app(ab, {'databaseURL': "https://numberplate-e206f-default-rtdb.firebaseio.com/"})

    ref=db.reference('/')

    url = "https://app.nanonets.com/api/v2/OCR/FullText"

    files= {

      'file': open('scaned_img_0.jpg','rb')
    }

    headers = {}

    response = requests.request("POST", url, headers=headers, files=files, auth=requests.auth.HTTPBasicAuth('cdc89165-2b0c-11ee-a211-26a6b57f65b4', ''))

    data = response.json()['results'][0]['page_data'][0]['words'][0]['text']
    print(data)
    dateandtime = str(datetime.datetime.now())
    numberPlate = {
        'datetime': dateandtime 
    }
    # a=[123,123]
    ref.child(data).set(numberPlate)
    # ref.push(a)db()