import requests
from bs4 import BeautifulSoup

URL = "https://www.example.com"
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

titles = soup.find_all("h2", class_="title")
for title in titles:
    print(title.get_text())
