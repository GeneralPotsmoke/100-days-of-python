#### Day 50: Automated Tinder Swiper
**Challenge:** Create a bot that swipes right on Tinder profiles using Selenium WebDriver.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "path_to_chrome_driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")

time.sleep(5)
login_button = driver.find_element(By.XPATH, '//*[@id="t-506329552"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()

time.sleep(5)
facebook_login = driver.find_element(By.XPATH, '//*[@id="t--1890934549"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_login.click()

# Switch to Facebook login window
base_window = driver.window_handles[0]
driver.switch_to.window(driver.window_handles[1])

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
email.send_keys("your_email@example.com")
password.send_keys("your_password")
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

time.sleep(5)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="t--1890934549"]/main/div/div/div/div[3]/button[1]')
allow_location_button.click()

time.sleep(5)
notifications_button = driver.find_element(By.XPATH, '//*[@id="t--1890934549"]/main/div/div/div/div[3]/button[2]')
notifications_button.click()

time.sleep(5)
cookies_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies_button.click()

# Swiping right
for _ in range(100):
    time.sleep(1)
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.send_keys(Keys.ARROW_RIGHT)

driver.quit()
```


