from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import json

# settings..
country = "USD"
Max_time = '2019.11.15' # datatime you want
exchange_list = {}

def crawling(Max_time):
    page_num = 0
    exchange_dict_edit = {}
    while True:
        URL = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_{0}KRW&page={1}".format(country, page_num)
        html = urlopen(URL).read()
        soup = BeautifulSoup(html, "html.parser")

        data_exchange = []
        data_ex_time = []
        
        for x in range(len(soup.find_all(class_="num"))):
            if x%2 is 0:
                data_exchange.append(float(soup.find_all(class_="num")[x].text.replace(',','')))
                
        for x in range(len(soup.find_all(class_="date"))):
            data_ex_time.append(soup.find_all(class_="date")[x].text)

        for x in range(len(data_ex_time)):
            exchange_dict_edit[data_ex_time[x]] = data_exchange[x]

        if Max_time in data_ex_time:
            return exchange_dict_edit
       
        page_num += 1

def save_json():
    with open('./json/sample.json', 'w', encoding='utf-8') as f:
        json.dump(crawling(Max_time), f, indent="\t")

if __name__ == "__main__": 
    save_json()
