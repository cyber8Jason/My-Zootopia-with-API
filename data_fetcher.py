import requests
import os
from dotenv import load_dotenv


API_URL = "https://api.api-ninjas.com/v1/animals?name="
load_dotenv()
API_KEY = os.getenv("API_KEY")


def fetch_data(name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  response = requests.get(API_URL + name, headers={'X-Api-Key': API_KEY})
  if response.status_code == requests.codes.ok:
    return response.json()
  else:
    print("❌ Error:", response.status_code, response.text)
    return []