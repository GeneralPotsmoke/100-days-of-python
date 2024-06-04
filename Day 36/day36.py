import requests
import smtplib
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_password"

stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}"
news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}"

def get_stock_data():
    response = requests.get(stock_url)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    return data_list

def get_news():
    response = requests.get(news_url)
    response.raise_for_status()
    articles = response.json()["articles"]
    return articles[:3]

stock_data = get_stock_data()
yesterday_closing = float(stock_data[0]["4. close"])
day_before_yesterday_closing = float(stock_data[1]["4. close"])
price_diff = abs(yesterday_closing - day_before_yesterday_closing)
percent_diff = (price_diff / day_before_yesterday_closing) * 100

if percent_diff > 5:
    news = get_news()
    with smtplib.SMTP("smtp.example.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        for article in news:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Stock Alert!

Headline: {article['title']}
Brief: {article['description']}"
            )
