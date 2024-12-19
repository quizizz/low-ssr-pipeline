import requests
import json

url = "https://quizizz.com/_aiserver/main/public/v1/quiz-generator/topic-subtopic/get-questions-v2"

payload = json.dumps({
  "subject": "Mathematics",
  "subtopic": "angle-angle similarity",
  "topic": "angles",
  "language": "English",
  "from": 0,
  "size": 25
})
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en;q=0.9',
  'baggage': 'sentry-environment=production,sentry-release=887e0ccd107881687562e2b7a34e14985f9824d9,sentry-public_key=f4055af1be6347b5a3b645683a6b50ff,sentry-trace_id=458dbc29aadc4a0cb8cdd4be87522481,sentry-sample_rate=0.05,sentry-transaction=admin-quiz-quizId-edit,sentry-sampled=false',
  'content-type': 'application/json',
  'cookie': 'QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_VERSION=v2; country=GB; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_NAME=main_main; quizizz_uid=e2c55c9a-c86a-4127-abc4-b279ac914ee7; _csrf=IcPRIHJnHntteaP6y4t29Ye5; __zlcmid=1PBnEn9UigfbxrY; locale=en; featureUpdatedTime=2024-12-18%2B05%253A46%253A26.971%2B%252B0000%2BUTC; nps_in_progress=2024-12-18T07:03:34.705Z; suid=336831e2-f567-4f23-b284-34c85ab32763; q-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5pc2hhbnQuYmhhbnNhbGlAcXVpeml6ei5jb20iLCJpYXQiOjE3MzQ1MDU1MDgsImV4cCI6MTczNDUzNDMwOH0.1IRI2JKLYLwJvn-dYHKS-BYHEPDutGIwRVukHrQ_VpI; _sid=crQnVCVFgRoRLJ85-WLfsE8GDizvvdLELt2GKC0E_MifIe236c-SeoJFly40_cic562I14R_bsLOyEUknwPZvcN2bzrVTcra_e8s5mz3tH0-_OzWEVAlVLCBCd5RVX_WJK0wbSkyA9VrG2_Mn_Nx1QKjkT74PA.LyQ1W2gkZcNx1eVYTus1_w.cVRBKGOdt-cqfm9U; featureHash=ed6d6177f183fee60cffd36996c3707c63e91cf1147042962e9e207440dedb21; ab.storage.deviceId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A7de8e1cc-1799-0fca-3932-0ea67ab29ea8%7Ce%3Aundefined%7Cc%3A1721993393586%7Cl%3A1734505527208; ab.storage.userId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3A5be42b02c0c02e001b283c57%7Ce%3Aundefined%7Cc%3A1734505527207%7Cl%3A1734505527208; x-csrf-token=d1r2sC0n-pMmFR_-x2Ca-kRbTrnJsrr1HOlE; ab.storage.sessionId.fda15891-26c0-43f0-aa55-6f8d885d4a4c=g%3Ae9b7a56d-201a-cdea-295b-4fc1096e5a00%7Ce%3A1734512768267%7Cc%3A1734505527207%7Cl%3A1734505568267; featureUUID=a2db163e-965f-473a-85f2-36cf105fc1c7; QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_NAME=main_main; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_VERSION=v2; _sid=01-YanyVSqekzeB1Dc-kFJq9p7Jzymj1dfLW8zoqKv8GvR_UpCxLTtyTOjkUtIMJexeKq6XrRPDB7Gwbb7ScFAAcWdGRsGWEH45ne4K8pk7pTcVp_J2LU0tKBgqQ5eu-EAwDogvU4VcRZHrVSv5EySPdtdaeXg.ky4LAxdqKU8I_ksKumlBJQ.wLZ6KwZ_iImhB0g6; featureHash=c0dc0c41fbd321e481bd1f5e9a27e4b06bfadf0fbf0bb73761801368709a76ec; featureUUID=0ae7aa3d-0ced-4c2d-a773-4ed6ef96fa34; featureUpdatedTime=2024-12-19%2B12%253A35%253A39.406%2B%252B0000%2BUTC; quizizz_uid=b8f87fe3-7e55-4c9d-9e2b-fbcff9d3b980; suid=18cb11b9-3fb4-45dc-9146-797807497c8c; x-csrf-token=5K1cCISo-zNTbGEpwJZMpC7RWzzeMv1nQ3iM',
  'origin': 'https://quizizz.com',
  'priority': 'u=1, i',
  'referer': 'https://quizizz.com/admin/quiz/67627467edba56cc29127171/edit',
  'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'sentry-trace': '458dbc29aadc4a0cb8cdd4be87522481-84c37dc5502f421a-0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
  'x-amzn-trace-id': 'Root=1-6762746c-6d73f9e4ed69dc78192a74ba;Parent=7e9e34fee973566f;Sampled=1',
  'x-component-type': 'adminv3',
  'x-csrf-token': 'd1r2sC0n-pMmFR_-x2Ca-kRbTrnJsrr1HOlE',
  'x-q-request-context-path': 'QuizPage',
  'x-q-traceid': 'Root=1-6762746c-6d73f9e4ed69dc78192a74ba;Parent=7e9e34fee973566f;Sampled=1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
