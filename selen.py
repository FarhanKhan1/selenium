from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("login_URL")
content = driver.page_source
driver.maximize_window()
print(driver.title)
username = driver.find_element(By.ID, 'login-form-username')
password = driver.find_element(By.ID, 'login-form-password')

driver.find_element(By.ID, 'login-form-submit').click()
print(driver.get_cookies())

for key, value in KEYS.items():
    
    try:
        time.sleep(3)
        driver.get('to_be_visited_URL')
        content = driver.page_source
        searchBox = driver.find_element(By.ID, 'project-filter-text')
        searchBox.send_keys(value)
        content = driver.page_source

    
    except:
        print(f"Downloading {key} file has been failed!!!")
        continue
# time.sleep(10)
# content = driver.page_source
# with open('content.html', 'w') as file:
    # file.write(content)

time.sleep(1000)

