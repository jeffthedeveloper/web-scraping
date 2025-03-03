import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('h1')  # Exemplo: capturar todos os títulos h1

# Exemplo de uso
url = 'https://www.example.com'
titles = scrape_website(url)
print(titles)
