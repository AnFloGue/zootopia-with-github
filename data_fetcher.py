import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    headers = {
        'X-Api-Key': API_KEY
    }
    response = requests.get(f"{BASE_URL}?name={animal_name}", headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return []
    else:
        return (response.status_code, response.json())