import requests
import json

url = "https://quizizz.com/_aiserver/script/public/v1/questions/query-relevancy"

payload = json.dumps({
  "secret": "u8WliRRPEZwjYYiTNk2Hrwl75t8QbK",
  "questionIds": [
    "67641d80ac13c2992194ee52",
    "67641d808c935855b5773366",
    "67641d805809535ad13474c0"
  ],
  "query": "Multiplication of numbers"
})
relevancy_headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en;q=0.8',
  'content-type': 'application/json',
  'x-amzn-trace-id': 'Root=1-669a374b-a13e6b804298d356177c2738;Parent=6b7610129048cc76;Sampled=1',
  'x-q-traceid': 'Root=1-669a374b-a13e6b804298d356177c2738;Parent=6b7610129048cc76;Sampled=1',
  'x-q-user': '{"_id": "66951b7957f65fefcf777336"}',
  'Cookie': 'QUIZIZZ_EXP_LEVEL=live; QUIZIZZ_EXP_NAME=main_main; QUIZIZZ_EXP_SLOT=22; QUIZIZZ_EXP_VERSION=v2; _sid=01-YanyVSqekzeB1Dc-kFJq9p7Jzymj1dfLW8zoqKv8GvR_UpCxLTtyTOjkUtIMJexeKq6XrRPDB7Gwbb7ScFAAcWdGRsGWEH45ne4K8pk7pTcVp_J2LU0tKBgqQ5eu-EAwDogvU4VcRZHrVSv5EySPdtdaeXg.ky4LAxdqKU8I_ksKumlBJQ.wLZ6KwZ_iImhB0g6; featureHash=c0dc0c41fbd321e481bd1f5e9a27e4b06bfadf0fbf0bb73761801368709a76ec; featureUUID=0ae7aa3d-0ced-4c2d-a773-4ed6ef96fa34; featureUpdatedTime=2024-12-19%2B12%253A35%253A39.406%2B%252B0000%2BUTC; quizizz_uid=b8f87fe3-7e55-4c9d-9e2b-fbcff9d3b980; suid=d9595949-1d89-47fd-99a4-8afbd10d6f3c; x-csrf-token=5K1cCISo-zNTbGEpwJZMpC7RWzzeMv1nQ3iM'
}

def get_relevance(question_ids, query):
    payload = json.dumps({
        "secret": "u8WliRRPEZwjYYiTNk2Hrwl75t8QbK",
        "questionIds": question_ids,
        "query": query
    })
    response = requests.request("POST", url, headers=relevancy_headers, data=payload)
    result = response.json()
    return result['data']