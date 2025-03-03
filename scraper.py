import requests
from bs4 import BeautifulSoup
import csv

# URL do site que será scrapado
url = 'https://example.com'

# Função para realizar o scraping
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrando os dados de interesse
    data = []
    for item in soup.find_all('div', class_='item'):
        title = item.find('h2').text
        description = item.find('p').text
        data.append([title, description])
    
    return data

# Salvando os dados em um arquivo CSV
def save_to_csv(data, filename='scraped_data.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Description'])
        writer.writerows(data)

if __name__ == ""__main__"":
    data = scrape_website(url)
    save_to_csv(data)
    print(""Data scraped and saved successfully!"")