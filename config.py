import requests
from dotenv import load_dotenv

load_dotenv()

def connect_to_api():
    endpoint = "https://opentdb.com/api.php"
    parameters = {
        "amount": 10,
        "type": "boolean"
    }
    response = requests.get(url=endpoint, params=parameters)
    response.raise_for_status()
    questions = response.json()
    return questions


