from selenium import webdriver                         # import web driver
from selenium.webdriver.common.by import By           # import by locator
from selenium.webdriver.common.keys import Keys     #  import button click handler
#Bot
TOKEN = '******************************************'

#SELENIUM
# Driver settings
options = webdriver.ChromeOptions()

# Adding User-Agent in options
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
# Фоновый режим
options.add_argument("--headless") 
#Disabling web driver mode
options.add_argument("--disable-blink-features=AutomationControlled")
# Disabling cerficiate errors
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-certificate-errors')

# Подавление Getting Default Adapter failed
options.add_experimental_option("excludeSwitches", ["enable-logging"])
