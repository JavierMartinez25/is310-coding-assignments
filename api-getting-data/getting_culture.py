import json
import requests
import apikey

EUROPEANA_API_KEY = apikey.load("EUROPEANA_API_KEY")
RAWG_API_KEY = apikey.load("RAWG_API_KEY")

url = f"https://api.rawg.io/api/games?key={RAWG_API_KEY}"
response = requests.get(url)
print(response.status_code)
print(response.json())

url = f"https://api.rawg.io/api/games?key={RAWG_API_KEY}&search=Terraria"
response = requests.get(url)
print(response.status_code)
print(response.json())

chosen_game = response.json()["results"][0]
game_name = chosen_game["name"]
game_id = chosen_game["id"]

print(game_name)

detail_url = f"https://api.rawg.io/api/games/{game_id}?key={RAWG_API_KEY}"
detail_response = requests.get(detail_url)
print(detail_response.status_code)
print(detail_response.json())

euro_url = f"https://api.europeana.eu/record/v2/search.json?wskey={EUROPEANA_API_KEY}&query={game_name}"
euro_response = requests.get(euro_url)
euro_data = euro_response.json()

print(euro_data)

items = euro_data.get("items", [])

clean_items = []
for item in items:
    clean_item = {
        "id": item.get("id"),
        "title": item.get("title"),
        "type": item.get("type"),
        "dataProvider": item.get("dataProvider"),
        "country": item.get("country"),
        "rights": item.get("rights"),
        "edmPreview": item.get("edmPreview")
    }
    clean_items.append(clean_item)

output_data = {
    "selected_api": "rawg",
    "rawg_item": {
        "name": chosen_game.get("name"),
        "released": chosen_game.get("released"),
        "rating": chosen_game.get("rating"),
        "metacritic": chosen_game.get("metacritic")
    },
    "europeana_items": clean_items
}

with open("getting_culture.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4, ensure_ascii=False)

print("Saved to getting_culture.json")