import requests
import json
from headers import get_headers

url = "https://quizizz.com/_quizserver/main/v2/version/676417fc5290c54097d969aa/question"

def getUrl(draft_id):
    return f"https://quizizz.com/_quizserver/main/v2/version/{draft_id}/question"

payload = json.dumps({
  "_id": "676417fc387e5057a41e5f00",
  "type": "MCQ",
  "time": 30000,
  "structure": {
    "kind": "MCQ",
    "options": [
      {
        "_id": "676417fd387e5057a41e5f21",
        "math": {
          "latex": [],
          "template": None
        },
        "type": "text",
        "hasMath": False,
        "media": [],
        "text": "Everything is fine, thanks!"
      },
      {
        "_id": "676417fd387e5057a41e5f22",
        "math": {
          "latex": [],
          "template": None
        },
        "type": "text",
        "hasMath": False,
        "media": [],
        "text": "I'm busy with work right now."
      },
      {
        "_id": "676417fd387e5057a41e5f23",
        "math": {
          "latex": [],
          "template": None
        },
        "type": "text",
        "hasMath": False,
        "media": [],
        "text": "Not much, how about you?"
      },
      {
        "_id": "676417fd387e5057a41e5f24",
        "math": {
          "latex": [],
          "template": None
        },
        "type": "text",
        "hasMath": False,
        "media": [],
        "text": "Just the usual, nothing special."
      }
    ],
    "settings": {
      "hasCorrectAnswer": True,
      "fibDataType": "string",
      "canSubmitCustomResponse": False,
      "doesOptionHaveMultipleTargets": False
    },
    "marks": {
      "correct": 1,
      "incorrect": 0
    },
    "query": {
      "answerTime": -1,
      "math": {
        "latex": [],
        "template": None
      },
      "type": None,
      "hasMath": False,
      "media": [],
      "text": "<p>whats up</p>",
      "_id": "676417fd387e5057a41e5f25"
    },
    "explain": {
      "math": {
        "latex": [],
        "template": None
      },
      "type": "",
      "hasMath": False,
      "media": [],
      "text": ""
    },
    "theme": {
      "titleFontFamily": "Quicksand",
      "fontFamily": "Quicksand",
      "fontColor": {
        "text": "#5D2057"
      },
      "background": {
        "color": "#FFFFFF",
        "image": "",
        "video": ""
      },
      "shape": {
        "largeShapeColor": "#F2F2F2",
        "smallShapeColor": "#9A4292"
      }
    },
    "graphs": [],
    "hints": [],
    "order": "asc",
    "hasMath": False,
    "answer": 2,
    "media": {},
    "elements": []
  },
  "index": 1,
  "startedAt": "",
  "v": 0,
  "clones": [],
  "published": False,
  "deleted": False,
  "isSuperParent": False,
  "metaData": {},
  "topics": [],
  "standards": [],
  "marksUpdated": False,
  "state": "",
  "metadata": {},
  "aiGenerated": True,
  "quizId": "676417fc5290c54097d969a9",
  "aiMeta": {
    "events": [
      {
        "eventName": "generate-options"
      }
    ]
  }
})


def add_questions(quiz_id, draft_id, questions):
    for question in questions:
        question_data = question.copy()
        if 'teleportFrom' in question_data:
            del question_data['teleportFrom']
        payload = json.dumps({**question_data, "quizId": quiz_id})
        response = requests.request("POST", getUrl(draft_id), headers=get_headers(), data=payload)
        print(response.text)