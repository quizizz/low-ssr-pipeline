import requests
import json
from headers import get_headers
url = "https://dev.quizizz.com/_aiserver/main/public/v1/quiz-generator/convert-questions"

payload = json.dumps({
  "uid": "6763fa91561186233e7674d7",
  "questions": [
    {
      "structure": {
        "settings": {
          "hasCorrectAnswer": True,
          "fibDataType": "string",
          "canSubmitCustomResponse": False,
          "doesOptionHaveMultipleTargets": False
        },
        "hasMath": False,
        "query": {
          "type": "text",
          "hasMath": False,
          "math": {
            "latex": []
          },
          "answerTime": 0,
          "media": [],
          "text": "What type of correlation (association)?<br>The outside temperature and the amount of layers you wear.&nbsp;"
        },
        "options": [
          {
            "type": "text",
            "hasMath": False,
            "math": {
              "latex": [],
              "template": None
            },
            "answerTime": 0,
            "id": "581ca49ed970d41d27f7ec80",
            "text": "Positive correlation",
            "media": [],
            "_id": "581ca49ed970d41d27f7ec80"
          },
          {
            "type": "text",
            "hasMath": False,
            "math": {
              "latex": [],
              "template": None
            },
            "answerTime": 0,
            "id": "581ca49ed970d41d27f7ec81",
            "text": "Negative correlation",
            "media": [],
            "_id": "581ca49ed970d41d27f7ec81"
          },
          {
            "type": "text",
            "hasMath": False,
            "math": {
              "latex": [],
              "template": None
            },
            "answerTime": 0,
            "id": "581ca49ed970d41d27f7ec82",
            "text": "No correlation",
            "media": [],
            "_id": "581ca49ed970d41d27f7ec82"
          }
        ],
        "explain": None,
        "hints": [],
        "kind": "MCQ",
        "answer": 1,
        "marks": {
          "correct": 1,
          "incorrect": 0
        }
      },
      "standards": [],
      "topics": [],
      "isSuperParent": False,
      "standardIds": [],
      "aiGenerated": False,
      "__v": 349,
      "teleportFrom": None,
      "cloned": False,
      "ver": 2,
      "parent": None,
      "_id": "581ca49ed970d41d27f7ec88",
      "createdAt": "2016-11-04T15:09:18.354Z",
      "updated": "2024-04-15T00:24:19.142Z",
      "time": 60000,
      "type": "MCQ",
      "published": True,
      "aiCreateMeta": {
        "taggedTopic": "Statistics",
        "taggedSubtopics": [
          "Correlation"
        ]
      }
    }
  ],
  "action": "replace",
  "subaction": "convertToSimilarQuestion",
  "quizId": "6763fa78c6481fe771a6047b",
  "versionId": "5c3d27ae2579f6001ad7f6c6",
  "params": {
    "language": "English",
    "subjects": [
      "Mathematics"
    ],
    "grades": [
      8,
      8
    ],
    "currentQuestionQuery": "",
    "currentQuestionAnswerExplanation": ""
  },
  "meta": {
    "source": "question_enhance"
  }
})

def get_similar_question(question_object, quiz_id, version_id):
    payload = json.dumps({
        "uid": "6763fa91561186233e7674d7",
        "questions": [
            question_object
        ],
        "action": "replace",
        "subaction": "convertToSimilarQuestion",
        "quizId": quiz_id,
        "versionId": version_id,
        "params": {
            "language": "English",
            "subjects": [
            "Mathematics"
            ],
            "grades": [],
            "currentQuestionQuery": "",
            "currentQuestionAnswerExplanation": ""
        },
        "meta": {
            "source": "question_enhance"
        }
    })
    response = requests.request("POST", url, headers=get_headers(), data=payload)
    return response.json()