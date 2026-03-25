import csv
import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()

def get_page_links(url):
    try:
        response = scraper.get(url)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        content = soup.find("div", class_="mw-parser-output")
        links = content.find_all("a") if content else []

        return [
            {
                "weapon_name": link.get_text(strip=True),
                "weapon_link": link.get("href")
            }
            for link in links
            if link.get("href") and link.get_text(strip=True)
        ]

    except Exception as e:
        print(f"Error getting links from {url}: {e}")
        return []

page_data = get_page_links("https://terraria.fandom.com/wiki/Weapons")

with open("terraria_weapons_links.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["weapon_name", "weapon_link"])

    for link in page_data:
        writer.writerow([
            link["weapon_name"],
            link["weapon_link"]
        ])

print("Done! Data saved to terraria_weapons_links.csv")