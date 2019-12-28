from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import json

# settings..
Max_time = '2019.11.15' # datatime you want
exchange_list = {}

def crawling(Max_time):
    iscontinue = True
    page_num = 0
    exchange_dict_edit = {}
    while iscontinue:
        URL = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW&page={}".format(page_num)
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

print(json.dumps(crawling(Max_time), sort_keys=True, indent=4))
