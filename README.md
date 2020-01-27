# Rate of Exchange Crawling

[네이버 환율](https://finance.naver.com/marketindex/) Based Daily rate of Exchange Crawling

## 설치 방법
- 실행 환경 (테스트 환경)
  - Windows 10 or Ubuntu Linux
  - Python3.x
  
## 사용 방법

- 변수 세팅
```python
country = "USD"   # country you want
Max_page_num = 10 # page_number you want
```

- RUN
```
python Rate of Exchange Crawling.py
```

- OUPUT (.json and matplotlib Graph)
```json
{
	"2019.12.27": 1160.5,
	"2019.12.26": 1162.0,
	"2019.12.24": 1164.0,
	"2019.12.23": 1164.0,
	"2019.12.20": 1161.0,
	"2019.12.19": 1166.0,
	"2019.12.18": 1168.5,
	"2019.12.17": 1167.0,
	"2019.12.16": 1173.0,
	"2019.12.13": 1172.0,
	"2019.12.12": 1189.0,
	"2019.12.11": 1194.7,
	"2019.12.10": 1192.0,
	"2019.12.09": 1191.0,
	"2019.12.06": 1189.5,
 }
 ```
 <p align=center>
  <img src="https://github.com/Xenia101/Rate-of-Exchange-Crawling/blob/master/img/graph.PNG?raw=true">
 </p>
 
