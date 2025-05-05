import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '**************'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульон",
    "photo_id": 979
}
body_change = {
    "pokemon_id": "307806",
    "name": "Кампот",
    "photo_id": 2
}

body_caught = {
    "pokemon_id": "307806"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create,)
print (response.status_code)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change,)
print (response_change.status_code)

response_change = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_change,)
print (response_change.status_code)
