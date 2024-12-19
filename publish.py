import requests
import json

url = "https://quizizz.com/_quizserver/main/v2/quiz/67641d7383d668a320e6aedf/version/67641d7383d668a320e6aee0/publish"

payload = json.dumps({
  "premiumUse": False
})
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en;q=0.5',
  'baggage': 'sentry-environment=production,sentry-release=35dfa77580394e9bd798c53ed342b33091104f74,sentry-public_key=f4055af1be6347b5a3b645683a6b50ff,sentry-trace_id=184af1ebc5ce462894ce1c6e70cbe5f7,sentry-sample_rate=0.05,sentry-transaction=admin-quiz-quizId-edit,sentry-sampled=false',
  'content-type': 'application/json',
  'cookie': 'QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_VERSION=v2; country=GB; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_NAME=main_main; quizizz_uid=e2c55c9a-c86a-4127-abc4-b279ac914ee7; _csrf=IcPRIHJnHntteaP6y4t29Ye5; __zlcmid=1PBnEn9UigfbxrY; locale=en; q-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5pc2hhbnQuYmhhbnNhbGlAcXVpeml6ei5jb20iLCJpYXQiOjE3MzQ2MTI5NjMsImV4cCI6MTczNDY0MTc2M30.83YVwzdmayym6CK3_OxjijGgW94CjOo2JvX9w2Azuh4; _sid=gTSt5gBK1GkuKeqM9uhjvYUh09t2gYc1pzpp69O0ZkxmF_qciG9q2HgaSxM3SuuBFxtwDlmjUySc16G-HkEcFP6iNe8RJl457hbhtM5dfjlzI5OJpEZYnyJH9SbfvupIlgtYudaNjbitTJhhcrlxTlfgZPeobQ.TpVCDlTt6cjpkPqCZxtmtA.sF0OkcDLK9fUonXf; ab.storage.deviceId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A7de8e1cc-1799-0fca-3932-0ea67ab29ea8%7Ce%3Aundefined%7Cc%3A1721993393586%7Cl%3A1734612969588; ab.storage.userId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A5be42b02c0c02e001b283c57%7Ce%3Aundefined%7Cc%3A1734612969587%7Cl%3A1734612969589; featureHash=c0dc0c41fbd321e481bd1f5e9a27e4b06bfadf0fbf0bb73761801368709a76ec; suid=bd1c4639-cedc-43b7-8780-a61a89975f22; featureUpdatedTime=2024-12-19%2B12%253A35%253A39.406%2B%252B0000%2BUTC; x-csrf-token=kDnnvjcP-naqJhUf2UGJG5uIF89DmWLR5bU4; ab.storage.sessionId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A374381ec-a79c-41af-d306-2c8738fc4098%7Ce%3A1734621626891%7Cc%3A1734612969588%7Cl%3A1734614426891; featureUUID=2b465b57-82be-44d7-a520-d74afb34f07d; QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_NAME=main_main; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_VERSION=v2; _sid=01-YanyVSqekzeB1Dc-kFJq9p7Jzymj1dfLW8zoqKv8GvR_UpCxLTtyTOjkUtIMJexeKq6XrRPDB7Gwbb7ScFAAcWdGRsGWEH45ne4K8pk7pTcVp_J2LU0tKBgqQ5eu-EAwDogvU4VcRZHrVSv5EySPdtdaeXg.ky4LAxdqKU8I_ksKumlBJQ.wLZ6KwZ_iImhB0g6; featureHash=c0dc0c41fbd321e481bd1f5e9a27e4b06bfadf0fbf0bb73761801368709a76ec; featureUUID=0ae7aa3d-0ced-4c2d-a773-4ed6ef96fa34; featureUpdatedTime=2024-12-19%2B12%253A35%253A39.406%2B%252B0000%2BUTC; quizizz_uid=b8f87fe3-7e55-4c9d-9e2b-fbcff9d3b980; x-csrf-token=5K1cCISo-zNTbGEpwJZMpC7RWzzeMv1nQ3iM',
  'origin': 'https://quizizz.com',
  'priority': 'u=1, i',
  'referer': 'https://quizizz.com/admin/quiz/67641d7383d668a320e6aedf/edit?at=676419ced911a06b077c497a&MCQ_saved=true',
  'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'sentry-trace': '184af1ebc5ce462894ce1c6e70cbe5f7-856aaf07660d481f-0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
  'x-amzn-trace-id': 'Root=1-67641dcc-b52736803e579a9858203bc4;Parent=c3e81361b3b9aa96;Sampled=1',
  'x-component-type': 'adminv3',
  'x-csrf-token': 'kDnnvjcP-naqJhUf2UGJG5uIF89DmWLR5bU4',
  'x-q-request-context-path': 'QuizPage',
  'x-q-traceid': 'Root=1-67641dcc-b52736803e579a9858203bc4;Parent=c3e81361b3b9aa96;Sampled=1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

def publish_quiz(quiz_id, draft_id):
    url = f"https://quizizz.com/_quizserver/main/v2/quiz/{quiz_id}/version/{draft_id}/publish"
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()