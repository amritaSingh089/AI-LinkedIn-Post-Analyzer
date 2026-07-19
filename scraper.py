import requests
from bs4 import BeautifulSoup


def scrape_linkedin_post(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(separator=" ", strip=True)

    return text[:10000]