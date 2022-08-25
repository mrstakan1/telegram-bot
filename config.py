from selenium import webdriver                         # Импортируем Веб Драйвер
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     # Импортируем обработчик нажатия кнопок
#Bot
TOKEN = '5658028624:AAEHCBcaDE8ozuU1rXe0b9eyVnMYqHturxE'

#SELENIUM
# Настройки драйвера
options = webdriver.ChromeOptions()

# Добавляем User-Agent в настройки
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
# Фоновый режим
options.add_argument("--headless") 
# Отключаем режим Веб Драйвера
options.add_argument("--disable-blink-features=AutomationControlled")
#Отключаем ошибки сертификатов
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-certificate-errors')

# Подавление Getting Default Adapter failed
options.add_experimental_option("excludeSwitches", ["enable-logging"])