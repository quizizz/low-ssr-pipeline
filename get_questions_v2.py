import requests
import json
from headers import get_headers

url = "https://quizizz.com/_aiserver/main/public/v1/quiz-generator/topic-subtopic/get-questions-v2"

def get_questions( subtopic, topic, language = "English", subject = "Mathematics", from_es= 0, size = 25):
    payload = json.dumps({
        "subject": subject,
        "subtopic": subtopic,
        "topic": topic,
        "language": language,
        "from": from_es,
        "size": size
    })
    response = requests.request("POST", url, headers=get_headers(), data=payload)
    return response.json()