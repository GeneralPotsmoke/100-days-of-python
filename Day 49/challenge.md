#### Day 49: Automating Job Applications on LinkedIn
**Challenge:** Create a program that automates the job application process on LinkedIn using Selenium WebDriver.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "path_to_chrome_driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/")

# Login
username = driver.find_element(By.ID, "session_key")
password = driver.find_element(By.ID, "session_password")
username.send_keys("your_email@example.com")
password.send_keys("your_password")
password.send_keys(Keys.ENTER)

time.sleep(5)

# Search for jobs
search_jobs = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__text-input")
search_jobs.send_keys("Software Engineer")
search_jobs.send_keys(Keys.ENTER)

time.sleep(5)

# Apply for jobs
job_listings = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
for job in job_listings:
    job.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(2)
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        submit_button.click()
    except:
        continue

driver.quit()
```


