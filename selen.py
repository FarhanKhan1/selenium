from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Keys = ['VER','USVP','TWM','TTHETRANTELEM','TE','TBI','TALKMD','TALKEHR','SHMRK','SF','SE','RPM','RPA',
# 'ROI','RCM','RAIN', 'QA','PST','PS','PMO','PM','PLAT','PERF'
# ]

KEYS = {'Websoft':'MTBCWEB',
'RBS':'MTBCRBS',
'Database':'MTBCOP',
'UI/UX':'MTBCMHEAL',
'MTBC-DEVOPS':'MTBCDEV',
'Datascience':'MTBCDAT',
'Business Intelligence':'MTBCBI'
}
driver.get("https://jira.carecloud.com/login.jsp")
content = driver.page_source
driver.maximize_window()
print(driver.title)
username = driver.find_element(By.ID, 'login-form-username')
password = driver.find_element(By.ID, 'login-form-password')
username.send_keys("fkhan")
password.send_keys("loginjira@123")
driver.find_element(By.ID, 'login-form-submit').click()
print(driver.get_cookies())

for key, value in KEYS.items():
    
    try:
        time.sleep(3)
        driver.get('https://jira.carecloud.com/secure/BrowseProjects.jspa?selectedCategory=all&selectedProjectType=all')
        content = driver.page_source
        searchBox = driver.find_element(By.ID, 'project-filter-text')
        searchBox.send_keys(value)
        content = driver.page_source
        time.sleep(5)
        driver.find_element(By.LINK_TEXT,key).click()
        time.sleep(2)
        icon_report = driver.find_element(By.CLASS_NAME, 'agile-icon-report')
        icon_report.find_element(By.XPATH, '..').click()
        time.sleep(7)
        driver.find_element(By.LINK_TEXT,'Sprint Report').click()
        time.sleep(10)
        driver.find_element(By.CLASS_NAME,'aui-iconfont-more').click()
        time.sleep(4)
        driver.find_element(By.ID,'sprint-view-in-issuenav').click()
        time.sleep(4)
        driver.find_element(By.ID,'AJS_DROPDOWN__83').click()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,'CSV (All fields)').click()
        time.sleep(5)
        driver.find_element(By.ID,'csv-export-dialog-export-button').click()
        time.sleep(3)
    
    except:
        print(f"Downloading {key} file has been failed!!!")
        continue
# time.sleep(10)
# content = driver.page_source
# with open('content.html', 'w') as file:
    # file.write(content)

time.sleep(1000)


#from selenium import webdriver
#import os
#set chromedriver.exe path
#driver = webdriver.Chrome(executable_path= os.getcwd() + '/chromedriver')
#url launch
#driver.get("https://www.tutorialspoint.com/questions/index.php")
#get page title
#print('Page title: ' + driver.title)
#quit browser
#driver.quit()
#from selenium import webdriver
#import time
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get('https://www.tutorialspoint.com/index.htm')
#print('Page title: ' + driver.title)
#time.sleep(10)

