import time

from selenium import webdriver
import os
options = webdriver.ChromeOptions()
CHROMEDRIVER_PATH = 'chromedriver.exe'
GOOGLE_CHROME_SHIM = os.getenv('GOOGLE_CHROME_SHIM',"chromedriver")

options.binary_location = "C:\\Users\\Sineth\\AppData\\Local\\Chromium\\Application\\chrome.exe"
options.add_argument("start-maximized")
options.add_argument('--disable-gpu')
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome( options=options)

browser.get('https://www.linkedin.com/in/vsineth/')

browser.execute_script("console.log('test')")

# Wait 60 seconds for the page to load and log in
time.sleep(60)

browser.execute_script("console.log('test')")
browser.execute_script("console.log(document.getElementsByTagName('a'))")
# browser.execute_script("document.getElementsByTagName('a')[2].click()")

# skills_div = browser.execute_script("return (function(){return document.getElementsByClassName('pv-profile-section__card-heading')[0].innerHTML});")
skills_div = browser.execute_script("return (function(){try{return document.getElementsByClassName('pv-profile-section__card-heading')[0].innerHTML;} catch(e){return 'exep';}})()")
print(skills_div)
