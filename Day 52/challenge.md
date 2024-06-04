#### Day 52: Instagram Follower Bot
**Challenge:** Create a bot that automatically follows users on Instagram.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "path_to_chrome_driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.instagram.com/")

time.sleep(5)
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("your_username")
password.send_keys("your_password")
password.send_keys(Keys.ENTER)

time.sleep(5)
not_now = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
not_now.click()

time.sleep(5)
not_now_2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
not_now_2.click()

time.sleep(5)
search = driver.find_element_by_css_selector("input[placeholder='Search']")
search.send_keys("pythonprogramming")
time.sleep(5)
search.send_keys(Keys.ENTER)
time.sleep(5)
search.send_keys(Keys.ENTER)

time.sleep(5)
follow_buttons = driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")
for button in follow_buttons:
    button.click()
    time.sleep(2)

driver.quit()
```


