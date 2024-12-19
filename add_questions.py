import requests
import json

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
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en;q=0.5',
  'baggage': 'sentry-environment=production,sentry-release=35dfa77580394e9bd798c53ed342b33091104f74,sentry-public_key=f4055af1be6347b5a3b645683a6b50ff,sentry-trace_id=7df2f8179f5846ef8a4d8cdb94428b5b,sentry-sample_rate=0.05,sentry-transaction=admin-quiz-quizId-question-questionId-edit,sentry-sampled=false',
  'content-type': 'application/json',
  'cookie': 'QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_VERSION=v2; country=GB; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_NAME=main_main; quizizz_uid=e2c55c9a-c86a-4127-abc4-b279ac914ee7; _csrf=IcPRIHJnHntteaP6y4t29Ye5; __zlcmid=1PBnEn9UigfbxrY; locale=en; featureUpdatedTime=2024-12-19%2B12%253A35%253A39.406%2B%252B0000%2BUTC; q-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5pc2hhbnQuYmhhbnNhbGlAcXVpeml6ei5jb20iLCJpYXQiOjE3MzQ2MTI5NjMsImV4cCI6MTczNDY0MTc2M30.83YVwzdmayym6CK3_OxjijGgW94CjOo2JvX9w2Azuh4; _sid=gTSt5gBK1GkuKeqM9uhjvYUh09t2gYc1pzpp69O0ZkxmF_qciG9q2HgaSxM3SuuBFxtwDlmjUySc16G-HkEcFP6iNe8RJl457hbhtM5dfjlzI5OJpEZYnyJH9SbfvupIlgtYudaNjbitTJhhcrlxTlfgZPeobQ.TpVCDlTt6cjpkPqCZxtmtA.sF0OkcDLK9fUonXf; x-csrf-token=XkTFo697-YajP_Wn_slyBUkclFKVNrs_AMRg; ab.storage.deviceId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A7de8e1cc-1799-0fca-3932-0ea67ab29ea8%7Ce%3Aundefined%7Cc%3A1721993393586%7Cl%3A1734612969588; ab.storage.userId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A5be42b02c0c02e001b283c57%7Ce%3Aundefined%7Cc%3A1734612969587%7Cl%3A1734612969589; nps_in_progress=2024-12-19T12:56:09.876Z; ab.storage.sessionId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A374381ec-a79c-41af-d306-2c8738fc4098%7Ce%3A1734620181643%7Cc%3A1734612969588%7Cl%3A1734612981643; featureHash=c0dc0c41fbd321e481bd1f5e9a27e4b06bfadf0fbf0bb73761801368709a76ec; featureUUID=f9679467-4052-47a4-8f70-974044ca423f; suid=140ebd5f-2905-41a9-b7b9-7056c2f772ce; QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_NAME=main_main; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_VERSION=v2; featureHash=1d7bdd719190c3cce07d8d92b02f4b200265f296593f4e85a28adfbed889c4a5; featureUUID=c2509cfb-c7fd-4dd3-ad28-477f04f52cb4; featureUpdatedTime=2024-12-19%2B06%253A23%253A50.832%2B%252B0000%2BUTC; quizizz_uid=412fa67c-d4b7-497a-87f1-b4f4bf61babb',
  'origin': 'https://quizizz.com',
  'priority': 'u=1, i',
  'referer': 'https://quizizz.com/admin/quiz/676417fc5290c54097d969a9/question/676417fc387e5057a41e5f00/edit',
  'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'sentry-trace': '7df2f8179f5846ef8a4d8cdb94428b5b-8db40d00c9e55e98-0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
  'x-amzn-trace-id': 'Root=1-676419cf-35f77ee1738e9816f3762257;Parent=26981d66a1bb8116;Sampled=1',
  'x-component-type': 'adminv3',
  'x-csrf-token': 'XkTFo697-YajP_Wn_slyBUkclFKVNrs_AMRg',
  'x-q-request-context-path': 'QuizPage',
  'x-q-traceid': 'Root=1-676419cf-35f77ee1738e9816f3762257;Parent=26981d66a1bb8116;Sampled=1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

def add_questions(quiz_id, draft_id, questions):
    for question in questions:
        payload = json.dumps({**question, "quizId": quiz_id})
        response = requests.request("POST", getUrl(draft_id), headers=headers, data=payload)
        print(response.text)