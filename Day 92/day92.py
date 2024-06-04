import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='item')

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Link'])
        for item in items:
            title = item.find('h2').text
            price = item.find('span', class_='price').text
            link = item.find('a')['href']
            writer.writerow([title, price, link])

url = 'https://example.com/items'
output_file = 'items.csv'
scrape_website(url, output_file)
