import requests

# URL base de SWAPI
base_url = 'https://swapi.dev/api'

# Endpoint para planetas
planets_endpoint = f'{base_url}/planets'

# Parámetros de búsqueda para clima árido
params = {'search': 'arid'}

# Realizar la solicitud GET a SWAPI
response = requests.get(planets_endpoint, params=params)

if response.status_code == 200:
    data = response.json()
    results = data['results']
    count_films = sum(len(planet['films']) for planet in results)
    print(f'En {count_films} películas aparecen planetas cuyo clima es árido.')
else:
    print('Error al consultar SWAPI.')

# Endpoint para personas (personas = characters en inglés)
people_endpoint = f'{base_url}/people'

# Parámetros de búsqueda para especie Wookiee
params = {'search': 'Wookiee'}

# Realizar la solicitud GET a SWAPI
response = requests.get(people_endpoint, params=params)

if response.status_code == 200:
    data = response.json()
    count_wookies = len(data['results'])
    print(f'Hay {count_wookies} Wookies en toda la saga.')
else:
    print('Error al consultar SWAPI.')

# Endpoint para aeronaves (starships en inglés)
starships_endpoint = f'{base_url}/starships'

# Parámetros de búsqueda para la primera película
params = {'film': '1'}

# Realizar la solicitud GET a SWAPI
response = requests.get(starships_endpoint, params=params)

if response.status_code == 200:
    data = response.json()
    smallest_starship = min(data['results'], key=lambda x: x.get('length', 0))
    smallest_starship_name = smallest_starship['name']
    print(f'La aeronave más pequeña en la primera película es: {smallest_starship_name}')
else:
    print('Error al consultar SWAPI.')
