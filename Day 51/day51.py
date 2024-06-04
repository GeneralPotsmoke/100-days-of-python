from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from

 twilio.rest import Client

chrome_driver_path = "path_to_chrome_driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Check internet speed
driver.get("https://www.speedtest.net/")
time.sleep(5)
go_button = driver.find_element_by_css_selector(".start-button a")
go_button.click()
time.sleep(60)
download_speed = float(driver.find_element_by_css_selector(".download-speed").text)
upload_speed = float(driver.find_element_by_css_selector(".upload-speed").text)

# Tweet if speed is below threshold
if download_speed < 100 or upload_speed < 50:
    driver.get("https://twitter.com/login")
    time.sleep(5)
    email = driver.find_element_by_name("session[username_or_email]")
    password = driver.find_element_by_name("session[password]")
    email.send_keys(TWITTER_EMAIL)
    password.send_keys(TWITTER_PASSWORD)
    password.send_keys(Keys.ENTER)
    time.sleep(5)
    tweet_compose = driver.find_element_by_css_selector("br[data-text='true']")
    tweet = f"Hey Internet Provider, why is my internet speed {download_speed}down/{upload_speed}up when I pay for 100down/50up?"
    tweet_compose.send_keys(tweet)
    tweet_compose.send_keys(Keys.CONTROL, Keys.ENTER)

# Send SMS alert
client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
    body=f"Internet speed is below threshold: {download_speed}down/{upload_speed}up.",
    from_='+1234567890',
    to='+0987654321'
)

driver.quit()
