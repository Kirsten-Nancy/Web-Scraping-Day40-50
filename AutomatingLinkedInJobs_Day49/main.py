import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver_path = "C:\\Development\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=92000001&keywords=python%20developer&location=Remote")
driver.maximize_window()

initial = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sign in')))
initial.click()

username = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'session_key')))
username.send_keys('pynancy254@gmail.com')
password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'session_password')))
password.send_keys('+.&,5wHbfA)ucX%')

submit = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
submit.click()

jobs = driver.find_elements_by_class_name('jobs-search-results__list-item')

# left = driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[1]/div/div')
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", left)

for job in jobs:
    job.click()

    save_btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'jobs-save-button')))
    save_btn.click()

    right_rail = driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[2]/div')
    for _ in range(2):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", right_rail)
        time.sleep(2)


    time.sleep(1)
    follow_btn = driver.find_element_by_class_name('follow')

    follow_btn.click()
    time.sleep(2)
