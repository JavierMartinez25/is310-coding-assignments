import csv
import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()

def get_npc_page_links(url):
    try:
        response = scraper.get(url)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")

        return [
            {
                "link_text": link.get_text(),
                "link_href": link.get("href")
            }
            for link in links if link.get("href")
        ]

    except Exception as e:
        print(f"Error getting links from {url}: {e}")
        return []

def fetch_npcs(url):
    try:
        response = scraper.get(url)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        npcs = []
        links = soup.find_all("a")

        for link in links:
            href = link.get("href")
            text = link.get_text(strip=True)

            if href and text and href.startswith("/wiki/") and "Category:" not in href:
                npcs.append(link)

        npc_data = []

        for npc in npcs:
            print(f"Processing {npc.get_text()}...")

            npc_info = {
                "npc_name": npc.get_text(),
                "npc_link": npc.get("href")
            }

            full_npc_url = "https://terraria.fandom.com" + npc_info["npc_link"]
            npc_info["page_links"] = get_npc_page_links(full_npc_url)
            npc_info["page_links_count"] = len(npc_info["page_links"])

            npc_data.append(npc_info)

        return npc_data

    except Exception as e:
        print(f"Error in fetch_npcs: {e}")
        return []

npc_data = fetch_npcs("https://terraria.fandom.com/wiki/Category:NPC_NPCs")

with open("terraria_npcs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["npc_name", "npc_link", "page_links", "page_links_count"])

    for npc in npc_data:
        writer.writerow([
            npc["npc_name"],
            npc["npc_link"],
            npc["page_links"],
            npc["page_links_count"]
        ])

print("Done! Data saved to terraria_npcs.csv")