from matplotlib import pyplot as plt
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# settings..
country = "USD"  # country you want
Max_page_num = 3 # page_number you want
exchange_list = {}

def crawling(Max_page_num):
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

        if page_num == Max_page_num:
            return exchange_dict_edit
       
        page_num += 1

def save_json(dic_data):
    with open('./json/sample.json', 'w', encoding='utf-8') as f:
        json.dump(dic_data, f, indent="\t")

if __name__ == "__main__":

    dic_data = crawling(Max_page_num)
    save_json(dic_data)

    X = [k.split('.')[1]+"/"+k.split('.')[2] for k in dic_data]
    Y = [v for v in dic_data.values()]

    plt.plot(list(reversed(X)), Y)
    plt.gca().invert_yaxis()
    plt.show()
