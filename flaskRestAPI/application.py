from __future__ import division

from flask import Flask, url_for
from flask import request
import requests
from flask_cors import CORS
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
from PIL import Image
from io import BytesIO
import json


import speech_recognition as sr
import sys
import os
import copy
import json
# obtain path to "english.wav" in the same folder as this script
from os import path


app = Flask(__name__)
CORS(app)


@app.route('/xax')
def api_root():
    return 'Welcome'


@app.route('/messages', methods=['POST'])
def api_messages():
    if 'audience_image' in request.files:
        f = request.files['audience_image']
        f.save(f.filename)

        # Replace <Subscription Key> with your valid subscription key.
        subscription_key = "3c2d9e603a9246aea14124b134560391"
        assert subscription_key

        # You must use the same region in your REST call as you used to get your
        # subscription keys. For example, if you got your subscription keys from
        # westus, replace "westcentralus" in the URI below with "westus".
        #
        # Free trial subscription keys are generated in the westcentralus region.
        # If you use a free trial subscription key, you shouldn't need to change
        # this region.
        face_api_url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/detect'
        # Set image_url to the URL of an image that you want to analyze.
        image_url = f.filename
        print(f.filename)
        headers = {'Content-Type': 'application/octet-stream',
                   'Ocp-Apim-Subscription-Key': subscription_key}
        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
            'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
        }
        data = open(image_url, 'rb')
        response = requests.post(face_api_url, params=params,
                                 headers=headers, data=data)
        faces = response.json()

        # print(faces)

        # Emotion scores initialized
        anger = 0.00
        contempt = 0.00
        disgust = 0.00
        fear = 0.00
        happiness = 0.00
        neutral = 0.00
        sadness = 0.00
        surprise = 0.00
        total = 0.00

        # Smile count; pos is smiling & neg is non-smiling
        smile_count_pos = 0
        smile_count_neg = 0

        # Gender
        male_count = 0
        female_count = 0

        # Average age
        avg_age_intermediate = 0

        #Occlusion -- false is not covered; true is covered
        eye_false = 0
        eye_true = 0
        mouth_false = 0
        mouth_true = 0
        forehead_false = 0
        forehead_true = 0

        e_list = [anger, contempt, disgust, fear,
                  happiness, neutral, sadness, surprise]

        for i in range(len(faces)):
            indiv_json_data = faces[i]
            item_dict = indiv_json_data['faceAttributes']
            smile = indiv_json_data['faceAttributes']['smile']
            emotion = indiv_json_data['faceAttributes']['emotion']
            gender = indiv_json_data['faceAttributes']['gender']
            age = indiv_json_data['faceAttributes']['age']
            eye_occlusion = indiv_json_data['faceAttributes']['occlusion']['eyeOccluded']
            mouth_occlusion = indiv_json_data['faceAttributes']['occlusion']['mouthOccluded']
            forehead_occlusion = indiv_json_data['faceAttributes']['occlusion']['foreheadOccluded']

            anger += emotion['anger']
            contempt += emotion['contempt']
            disgust += emotion['disgust']
            fear += emotion['fear']
            happiness += emotion['happiness']
            neutral += emotion['neutral']
            sadness += emotion['sadness']
            surprise += emotion['surprise']

            if smile <= 0.5:
                smile_count_neg += 1
            else:
                smile_count_pos += 1

            if gender == 'female':
                female_count += 1
            else:
                male_count += 1

            avg_age_intermediate += age

            if eye_occlusion == False:
                eye_false += 1
            else:
                eye_true += 1

            if mouth_occlusion == False:
                mouth_false += 1
            else:
                mouth_true += 1

            if forehead_occlusion == False:
                forehead_false += 1
            else:
                forehead_true += 1

        total = (anger + contempt + disgust + fear +
                 happiness + neutral + sadness + surprise)
        if(total == 0):
            total = 1

        anger_pct = round(anger / total * 100)
        contempt_pct = round(contempt / total * 100)
        disgust_pct = round(disgust / total * 100)
        fear_pct = round(fear / total * 100)
        happiness_pct = round(happiness / total * 100)
        neutral_pct = round(neutral / total * 100)
        sadness_pct = round(sadness / total * 100)
        surprise_pct = round(surprise / total * 100)

        smiles_incrowd_pct = round((smile_count_pos / total) * 100)

        male_pct = round((male_count / total) * 100)
        female_pct = round((female_count / total) * 100)

        avg_age = round(avg_age_intermediate / total)

        eye_covered_pct = round((eye_true / total) * 100)
        mouth_covered_pct = round((mouth_true / total) * 100)
        forehead_covered_pct = round((mouth_true / total) * 100)
        engagement_metric = (1 - (eye_covered_pct * 0.8 + mouth_covered_pct *
                                  0.03 + forehead_covered_pct * 0.12) * 0.95) * 100

        data1 = {}
        data1['total_ppl'] = total
        data1['anger'] = anger_pct
        data1['contempt'] = contempt_pct
        data1['disgust'] = disgust_pct
        data1['fear'] = fear_pct
        data1['happiness'] = happiness_pct
        data1['neutral'] = neutral_pct
        data1['sadness'] = sadness_pct
        data1['surprise'] = surprise_pct
        data1['smiles_incrowd_pct'] = smiles_incrowd_pct
        data1['males_incrowd_pct'] = male_pct
        data1['avg_age_incrowd'] = avg_age
        data1['forehead_covered_pct'] = forehead_covered_pct
        data1['eye_covered_pct'] = eye_covered_pct
        data1['mouth_covered_pct'] = mouth_covered_pct
        data1['engagement_pct'] = engagement_metric

        json_data = json.dumps(data1)

        return json_data
        return "@@@IMAGE PROCESSED@@@ \n\r"

    else:
        return "Error has occured"


@app.route('/audio', methods=['POST'])
def api_audio():
    if request.method == 'POST':
        # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")
        # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "girl_filler1.wav")
        AUDIO_FILE = path.join(path.dirname(
            path.realpath(__file__)), "filler-dave.wav")

        # use audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        # STT Microsoft Bing Voice Recognition
        BING_KEY = "2e41739b91bf4b6e84ad1aa4e9a6030d"

        # STT and preprocessing
        raw = r.recognize_bing(audio, key=BING_KEY)
        print(raw)
        """ 
        text = raw.split()
        text = [k.lower() for k in text]
        print(text)

        text_non_replaced = copy.deepcopy(text) """
        return "ECHO: POSTED\n"


if __name__ == '__main__':
    app.run()
