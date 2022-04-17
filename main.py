from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
EMAIL =  "YOUR LINKEDIN EMAIL"
PASSWORD = "YOUR LINKEDIN PASSWORD"

chrome_driver_path = "C:\\Users\\Hp EliteBook\\Desktop\\chrome Driver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(
    'https://www.linkedin.com/jobs/search/?f_WT=2&geoId=105365761&keywords=python%20%20developer&location=Nigeria')
sign_in_button = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()
email_label = driver.find_element_by_xpath('//*[@id="username"]')
email_label.send_keys(EMAIL)
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(PASSWORD)
log_in = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
log_in.click()
find_jobs = driver.find_elements_by_class_name('jobs-search-results__list-item')

job_list = [print("called") for job in find_jobs]
x = range(len(job_list))
for i in x:
    time.sleep(10)
    find_jobs[i].click()
    time.sleep(10)
    save_job = driver.find_element_by_class_name("jobs-save-button")
    save_job.click()




