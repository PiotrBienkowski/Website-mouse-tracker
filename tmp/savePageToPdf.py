import time
import pdfkit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://tianacapital.com/")

body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.END)
time.sleep(5) 

pdfkit.from_string(driver.page_source, 'example.pdf', configuration=pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf'))

driver.quit()