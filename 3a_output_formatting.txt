import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the Emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Headers with the emotion model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Check if the call was a success
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        emotion_dict['dominant_emotion'] = max(emotion_dict, key=emotion_dict.get)
        return emotion_dict
    else:
        return "An error occurred!"