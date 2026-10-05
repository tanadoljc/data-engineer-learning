import requests

url = "https://pokeapi.co/api/v2/pokemon"
response = requests.get(url)

total_record = response.json()["count"]

print(f"Total record: {total_record}")

