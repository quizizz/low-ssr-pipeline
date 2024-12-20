import requests
import json

url = "https://quizizz.com/_aiserver/main/public/v1/quiz-generator/convert-questions"

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

similar_question_headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en;q=0.5',
  'baggage': 'sentry-environment=production,sentry-release=c8fab3ee114aeb6fde9ff6ab79898a569a6a0c4b,sentry-public_key=f4055af1be6347b5a3b645683a6b50ff,sentry-trace_id=d71068fb35f4436fbe02495a88c889e1,sentry-sample_rate=0.05,sentry-transaction=admin-quiz-quizId-edit,sentry-sampled=false',
  'content-type': 'application/json',
  'cookie': 'QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_VERSION=v2; country=GB; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_NAME=main_main; quizizz_uid=e2c55c9a-c86a-4127-abc4-b279ac914ee7; _csrf=IcPRIHJnHntteaP6y4t29Ye5; __zlcmid=1PBnEn9UigfbxrY; locale=en; q-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5pc2hhbnQuYmhhbnNhbGlAcXVpeml6ei5jb20iLCJpYXQiOjE3MzQ2ODM2MjIsImV4cCI6MTczNDcxMjQyMn0.DZnTEN7nzsUzHnFRn1tbvC9rpzj0L4LBJ5TwgjBSdRY; _sid=LdvJH2zpo-OxSsYf9XAUkYWqzTvbVDQ41cpBaoY2MX666WodZs2-pwYG7F82yBVeV5ype4AwzmphycjCbXndSEQapAJqRPpMhedQ-Z6Y9cg0V_8IBvVf6Z4RA-nJvRlrGpmPE_8ea7yAM5efCohNL_8EMSD2Iw.4y1WFgyx6sXEs9QJaK7frg.y00wRofPs3rh-d9D; ab.storage.deviceId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A7de8e1cc-1799-0fca-3932-0ea67ab29ea8%7Ce%3Aundefined%7Cc%3A1721993393586%7Cl%3A1734690230644; ab.storage.userId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A5be42b02c0c02e001b283c57%7Ce%3Aundefined%7Cc%3A1734690230642%7Cl%3A1734690230644; featureUpdatedTime=2024-12-20%2B10%253A38%253A29.704%2B%252B0000%2BUTC; nps_in_progress=2024-12-20T10:45:34.708Z; suid=48598e6c-0aaf-4dfa-a205-250a274edc73; featureHash=d3584d162a7528a45190c47115385addf02834bdc843dbb4448524b78d5b4f86; x-csrf-token=yHpowoFW-DOnzVnxMP_I7Sp8r_WTcGu0WWm4; ab.storage.sessionId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A3c69d8eb-72eb-6a65-43d7-621a4d0c5af8%7Ce%3A1734698754021%7Cc%3A1734690230643%7Cl%3A1734691554021; featureUUID=a5e230ff-5052-47e9-a595-4c218a3bdbb9; QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_NAME=main_main; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_VERSION=v2; _sid=01-YanyVSqekzeB1Dc-kFJq9p7Jzymj1dfLW8zoqKv8GvR_UpCxLTtyTOjkUtIMJexeKq6XrRPDB7Gwbb7ScFAAcWdGRsGWEH45ne4K8pk7pTcVp_J2LU0tKBgqQ5eu-EAwDogvU4VcRZHrVSv5EySPdtdaeXg.ky4LAxdqKU8I_ksKumlBJQ.wLZ6KwZ_iImhB0g6; featureHash=c0dc0c41fbd321e481bd1f5e9a27e4b06bfadf0fbf0bb73761801368709a76ec; featureUUID=0ae7aa3d-0ced-4c2d-a773-4ed6ef96fa34; featureUpdatedTime=2024-12-19%2B12%253A35%253A39.406%2B%252B0000%2BUTC; quizizz_uid=b8f87fe3-7e55-4c9d-9e2b-fbcff9d3b980; x-csrf-token=5K1cCISo-zNTbGEpwJZMpC7RWzzeMv1nQ3iM',
  'origin': 'https://quizizz.com',
  'priority': 'u=1, i',
  'referer': 'https://quizizz.com/admin/quiz/67654ae97a5eb738c052e777/edit',
  'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'sentry-trace': 'd71068fb35f4436fbe02495a88c889e1-9078e3a19841de1d-0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
  'x-amzn-trace-id': 'Root=1-67654afb-dc72b43e1c5760df4bde955a;Parent=cc76c7debf1822d0;Sampled=1',
  'x-component-type': 'adminv3',
  'x-csrf-token': 'yHpowoFW-DOnzVnxMP_I7Sp8r_WTcGu0WWm4',
  'x-q-request-context-path': 'QuizPage',
  'x-q-traceid': 'Root=1-67654afb-dc72b43e1c5760df4bde955a;Parent=cc76c7debf1822d0;Sampled=1'
}

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
    response = requests.request("POST", url, headers=similar_question_headers, data=payload)
    return response.json()