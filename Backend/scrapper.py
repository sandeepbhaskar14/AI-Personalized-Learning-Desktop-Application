import requests
from bs4 import BeautifulSoup

def scrape_amazon_product(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }
    
    content = requests.get(url, headers=headers).content
    soup = BeautifulSoup(content, 'html.parser')
    
    title = soup.title.text
    price = soup.find(class_ = "a-price-whole").text
    
    if not title:
        title = 'No Title Found'
    if not price:
        price = None
    
    return {'title': title, 'price':price}


# url = 'https://www.amazon.in/Samsung-Smartphone-Titanium-Whitesilver-Included/dp/B0DSKL9MQ8/ref=sr_1_1_sspa?sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

# title = scrape_amazon_product(url)
# print(title)