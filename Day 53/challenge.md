#### Day 53: Automated Data Entry Job
**Challenge:** Create a bot that automates data entry tasks using Selenium WebDriver.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "path_to_chrome_driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.example.com/data-entry")

time.sleep(5)
entries = [
    {"name": "John Doe", "email": "john@example.com", "phone": "1234567890"},
    {"name": "Jane Smith", "email": "jane@example.com", "phone": "0987654321"}
]

for entry in entries:
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.NAME, "email")
    phone_input = driver.find_element(By.NAME, "phone")
    
    name_input.send_keys(entry["name"])
    email_input.send_keys(entry["email"])
    phone_input.send_keys(entry["phone"])
    
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    time.sleep(2)

driver.quit()
```


