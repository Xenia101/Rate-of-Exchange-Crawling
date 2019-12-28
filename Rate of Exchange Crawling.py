from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np

ex_time_list  = []
exchange_list = []

for page_num in range(1,2):
    URL = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW&page={}".format(page_num)
    html = urlopen(URL).read()
    soup = BeautifulSoup(html, "html.parser")

    for x in range(len(soup.find_all(class_="num"))):
        if x%2 is 0:
            exchange_list.append(float(soup.find_all(class_="num")[x].text.replace(',','')))
        print(soup.find_all(class_="date")[x].text)
        
exchange_list = np.array(exchange_list)
ex_time_list = np.array(ex_time_list)
print(exchange_list)
print(ex_time_list)
