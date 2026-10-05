import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    input_json = json.dumps({
        "raw_document": {
            "text": text_to_analyze
        }
    })

    response = requests.post(url, headers=headers, data=input_json)
    data = json.loads(response.text)
    
    predictions = data['emotionPredictions']
    
    anger_score = 0
    disgust_score = 0
    fear_score = 0
    joy_score = 0
    sadness_score = 0

    for item in predictions:
        scores_data = item['emotion']
        anger_score = scores_data.get('anger', 0)
        disgust_score = scores_data.get('disgust', 0)
        fear_score = scores_data.get('fear', 0)
        joy_score = scores_data.get('joy', 0)
        sadness_score = scores_data.get('sadness', 0)

    scores_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(scores_dict, key=scores_dict.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

if __name__ == "__main__":
    print(emotion_detector("I am so happy I am doing this"))




