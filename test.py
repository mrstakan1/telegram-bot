# import time                                            # Импортируем модуль time

# from selenium import webdriver                         # Импортируем Веб Драйвер
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys        # Импортируем обработчик нажатия кнопок


# # Ссылка на обрабатываемую страницу
# url = "https://www.youtube.com/results?search_query=DA"

# # Настройки драйвера
# options = webdriver.ChromeOptions()

# # Добавляем User-Agent в настройки
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
# options.add_argument("--headless") #- фоновый режим
# # Отключаем режим Веб Драйвера
# options.add_argument("--disable-blink-features=AutomationControlled")

# # Подавление Getting Default Adapter failed
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

# # Создание Веб Драйвера
# driver = webdriver.Chrome(
#     executable_path="C:\\VS_PROJ\\TeleBot\\chromedriver.exe",   # Указываем путь до драйвера
#     options=options   # Устанавливаем настройки
#     )


# try:
#     result_dict = {
#         }

#     driver.get(url=url)

#     videos = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]')
#     for i in range(10):

#     print(asd)
#     #/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/yt-interaction
#     #/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[3]
#     # driver.find_element_by_id('contents').find_elements()
#     # # CERAMIC = driver.find_element_by_class_name("front_ceramic")
#     # # CERAMOGRANIT = driver.find_element_by_class_name("front_keramogranit")
#     # # CLINKER = driver.find_element_by_class_name("front_klinker")
#     # # MOZAIKA = driver.find_element_by_class_name("front_mozaika")

#     # # print("[+] Working on ceramic...")

#     # # CERAMIC.click()
#     # # time.sleep(1)

#     # cards = []
#     # iter = 1
#     # while iter != 20:
#     #     temp = driver.find_elements_by_class_name("collection")
#     #     cards = [el for el in temp]

#     #     driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

#     #     print(f"[{iter}] iteration")
#     #     iter += 1
#     #     time.sleep(0.5)

#     # set(cards)

#     # for card in cards:
#     #     temp_dict = {}
#     #     temp_dict["Название"] = card.find_element_by_class_name("collection_name").find_element_by_tag_name("a").text.strip()






# except Exception as Ex:          # Проверка на ошибки
#     print(Ex)                    # Вывод ошибок

# finally:
#     driver.close()               # Закрытие вкладки
#     driver.quit()                # Выключение драйвера










# '''--------------------------------> INFO <-------------------------------------'''

# # password_input.send_keys(Keys.ENTER) - Нажимаем Enter
# # driver.save_screenshot("1.png") - Сохраняет скриншот экрана под названием 1.png
# # driver.refresh() - Обновляем страницу браузера
# # options.add_argument("--headless") - фоновый режим