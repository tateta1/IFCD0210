import requests
from pprint import pprint

# url = "https://github.com/jalfonsosuarez/IFCD0210/blob/main/UF1846/000_indice.ipynb"
# url="https://github.com/jalfonsosuarez/IFCD0210/blob/109ba374af718e0729a18194e7be3b92d720bdd9/UF1846/000_indice.ipynb"
# url = "https://pokeapi.co/api/v2/pokemon/ditto"
# url = "http://127.0.0.1:5000/editar/7"
url = "http://127.0.0.1:5000/users/1"

resp = requests.get(url)
pprint(resp.json())

