import requests
import json

url = "https://quizizz.com/_quizserver/main/v2/quiz"

create_quiz_payload = json.dumps({
  "name": "Untitled Quiz",
  "subjects": [],
  "grade": [],
  "type": "quiz",
  "visibility": False
})

create_quiz_headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en;q=0.5',
  'baggage': 'sentry-environment=production,sentry-release=35dfa77580394e9bd798c53ed342b33091104f74,sentry-public_key=f4055af1be6347b5a3b645683a6b50ff,sentry-trace_id=2ec1081d6aa74ed3a8de668bc11f38a4,sentry-sample_rate=0.05,sentry-transaction=admin,sentry-sampled=false',
  'content-type': 'application/json',
  'cookie': 'QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_VERSION=v2; country=GB; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_NAME=main_main; quizizz_uid=e2c55c9a-c86a-4127-abc4-b279ac914ee7; _csrf=IcPRIHJnHntteaP6y4t29Ye5; __zlcmid=1PBnEn9UigfbxrY; locale=en; suid=f71daa33-1bec-4e74-98e8-80a098eab7b2; featureUpdatedTime=2024-12-19%2B12%253A35%253A39.406%2B%252B0000%2BUTC; q-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5pc2hhbnQuYmhhbnNhbGlAcXVpeml6ei5jb20iLCJpYXQiOjE3MzQ2MTI5NjMsImV4cCI6MTczNDY0MTc2M30.83YVwzdmayym6CK3_OxjijGgW94CjOo2JvX9w2Azuh4; _sid=gTSt5gBK1GkuKeqM9uhjvYUh09t2gYc1pzpp69O0ZkxmF_qciG9q2HgaSxM3SuuBFxtwDlmjUySc16G-HkEcFP6iNe8RJl457hbhtM5dfjlzI5OJpEZYnyJH9SbfvupIlgtYudaNjbitTJhhcrlxTlfgZPeobQ.TpVCDlTt6cjpkPqCZxtmtA.sF0OkcDLK9fUonXf; x-csrf-token=XkTFo697-YajP_Wn_slyBUkclFKVNrs_AMRg; ab.storage.deviceId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A7de8e1cc-1799-0fca-3932-0ea67ab29ea8%7Ce%3Aundefined%7Cc%3A1721993393586%7Cl%3A1734612969588; ab.storage.userId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A5be42b02c0c02e001b283c57%7Ce%3Aundefined%7Cc%3A1734612969587%7Cl%3A1734612969589; featureHash=3c0b9e13e7da063374a9606b6ce95d541fab3fac2fcb79bcc3783914f009313c; featureUUID=02eb656e-198e-439a-a940-84b3126f4d60; nps_in_progress=2024-12-19T12:56:09.876Z; ab.storage.sessionId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A374381ec-a79c-41af-d306-2c8738fc4098%7Ce%3A1734620181643%7Cc%3A1734612969588%7Cl%3A1734612981643; QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_NAME=main_main; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_VERSION=v2; featureHash=1d7bdd719190c3cce07d8d92b02f4b200265f296593f4e85a28adfbed889c4a5; featureUUID=c2509cfb-c7fd-4dd3-ad28-477f04f52cb4; featureUpdatedTime=2024-12-19%2B06%253A23%253A50.832%2B%252B0000%2BUTC; quizizz_uid=412fa67c-d4b7-497a-87f1-b4f4bf61babb',
  'origin': 'https://quizizz.com',
  'priority': 'u=1, i',
  'referer': 'https://quizizz.com/admin?createUsingAI=true&forLesson=false',
  'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'sentry-trace': '2ec1081d6aa74ed3a8de668bc11f38a4-9db045b6090484f7-0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
  'x-amzn-trace-id': 'Root=1-676417fc-9efc12729af410e1a58e6448;Parent=8012939a23b7d369;Sampled=1',
  'x-component-type': 'adminv3',
  'x-csrf-token': 'XkTFo697-YajP_Wn_slyBUkclFKVNrs_AMRg',
  'x-q-request-context-path': 'FeaturedPage',
  'x-q-traceid': 'Root=1-676417fc-9efc12729af410e1a58e6448;Parent=8012939a23b7d369;Sampled=1'
}

def creat_quiz(title = "Untitled", grade = ["4"] , subject = ["Mathematics"]):
    payload = json.dumps({
        "name": title,
        "subjects": subject,
        "grade": grade,
        "type": "quiz",
        "visibility": False
    })
    response = requests.request("POST", url, headers=create_quiz_headers, data=payload)
    response_json = response.json()
    quiz_data = response_json["data"]["quiz"]
    return {
        "quiz_id": quiz_data["_id"],
        "draft_id": quiz_data["draftVersion"]
    }