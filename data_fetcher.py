import requests


API_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = "iW1MsjidDZudxSWyk46tTg==ODsquybYVL1j077z"


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