import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://www.amazon.com/dp/B08X4VQ1Y1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

target_price = 200.0

if price_as_float < target_price:
    MY_EMAIL = "your_email@example.com"
    MY_PASSWORD = "your_password"
    with smtplib.SMTP("smtp.example.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!

The price of the product is now {price}. Check the link: {URL}"
        )
