#### Day 48: Selenium Webdriver and Game Playing Bot
**Challenge:** Create a bot that plays an online game using Selenium WebDriver.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "path_to_chrome_driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        for item in items:
            item.click()
        timeout = time.time() + 5

    if time.time() > five_min:
        break
```


