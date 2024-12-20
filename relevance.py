import requests
import json

url = "http://localhost:8081/public/v1/questions/query-relevancy"

payload = json.dumps({
  "secret": "p0zu6nndI6gte6U98PtmM7P69nunct",
  "questionId": "5c9cb467c85585001be90e57",
  "query": "central inscribed and circumscribed angles in circles"
})
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en;q=0.8',
  'content-type': 'application/json',
  'x-amzn-trace-id': 'Root=1-669a374b-a13e6b804298d356177c2738;Parent=6b7610129048cc76;Sampled=1',
  'x-q-traceid': 'Root=1-669a374b-a13e6b804298d356177c2738;Parent=6b7610129048cc76;Sampled=1',
  'x-q-user': '{"_id": "66951b7957f65fefcf777336"}',
  'Cookie': 'quizizz_uid=8e905a27-fc32-4d80-8495-19e0e47a423c'
}

def get_relevance(question_id, query):
    url = "http://localhost:8081/public/v1/questions/query-relevancy"
    payload = json.dumps({
        "secret": "p0zu6nndI6gte6U98PtmM7P69nunct",
        "questionId": question_id,
        "query": query
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()