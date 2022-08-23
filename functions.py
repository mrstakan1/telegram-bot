import requests, lxml
from bs4 import BeautifulSoup

def get_ip_info(ip):
    line = ''
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        data = {
            '[IP]': response.get('query'),
            '[COUNTRY]': response.get('country'),
            '[CITY]': response.get('regionName'),
            '[ZIP]': response.get('zip')
        }
        for k, v in data.items():
            line+= f"<b>{k}: {v}</b>\n"
        return line
    except requests.exceptions.ConnectionError:
        print('<b>[X] Ошибка со стороны сервера</b>')
        return False

def get_crypto_news():
    URL = "https://www.rbc.ru/crypto/tags/?tag=%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0"
    HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.3.822 Yowser/2.5 Safari/537.36"
    }
    result = []
    response = requests.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')

    news_list = soup.find_all('div', class_="item item_image-mob js-tag-item")
    for new in news_list:
        pre_result = {}

        pre_result["link"] = new.find('div', class_="item__wrap l-col-center").find("a", class_="item__link").get('href')
        pre_result["title"] = new.find('div', class_="item__wrap l-col-center").find('span', class_="item__title-wrap").find('span', class_="item__title rm-cm-item-text").text.strip()

        result.append(pre_result)
    return result[:5]

def get_crypto_price(ticker):
    ticker = ticker.lower()
    try:
        req = requests.get(f"https://yobit.net/api/3/ticker/{ticker}_usd")
        response = req.json()
        sell_price = response[f"{ticker}_usd"]["sell"]
        return sell_price
    except Exception as exception:
        print(exception)
        return False

def get_video(search):
    pass