import requests
import json
from headers import get_headers
url = "https://quizizz.com/_quizserver/main/v2/quiz"

def creat_quiz(title = "Untitled", grade = ["4"] , subject = ["Mathematics"]):
    payload = json.dumps({
        "name": title,
        "subjects": subject,
        "grade": grade,
        "type": "quiz",
        "visibility": False
    })
    response = requests.request("POST", url, headers=get_headers(), data=payload)
    response_json = response.json()
    quiz_data = response_json["data"]["quiz"]
    return {
        "quiz_id": quiz_data["_id"],
        "draft_id": quiz_data["draftVersion"]
    }