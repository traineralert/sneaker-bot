import requests
from bs4 import BeautifulSoup

OFFSPRING_URL = "https://www.offspring.co.uk/sale?brand=nike,jordan"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def fetch_offspring_sale():
    try:
        r = requests.get(OFFSPRING_URL, headers=HEADERS, timeout=15)
        r.raise_for_status()
    except Exception as e:
        print("Error fetching Offspring:", e)
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    products = soup.select(".product-tile")
    new_items = []

    for p in products:
        name_tag = p.select_one(".product-title a")
        if not name_tag:
            continue
        name = name_tag.text.strip()
        link = "https://www.offspring.co.uk" + name_tag["href"]
        new_items.append(f"{name} - {link}")

    return new_items

if __name__ == "__main__":
    items = fetch_offspring_sale()
    print("Found products:", len(items))
    for i in items:
        print(i)
