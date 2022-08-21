import requests
import json


parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
data = response.json()
# print(type(data))
# print(json.dumps(data, indent=4))
question_data = data['results']
# print(json.dumps(question_data, indent=4))

