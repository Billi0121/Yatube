from pprint import pprint
import requests


url = f'https://www.swapi.tech/api/starships/'
response = requests.get(url).json()
pprint(response.get('results').get('name'))
