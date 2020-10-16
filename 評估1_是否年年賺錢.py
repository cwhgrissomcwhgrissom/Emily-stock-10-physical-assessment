
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

date = datetime.datetime.now()
int_years = date.year-1
str_years = str(date.year-1)

url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=2301'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
datastream = requests.get(url, headers = headers)
soup = BeautifulSoup(datastream.content,'lxml')
#print(soup)

# -----------------------------------合格標準: 10 年裡至少要有 9 年EPS要 >0 -----------------------------------
eps_count = 0
for n in range(0, 5):
        row_data = soup.select('#row' + str(n) + ' > td:nth-child(1) > nobr')   
        if row_data[0].text == str_years:
            for m in range(n, 11):
                net_profit_after_tax = soup.select('#row' + str(m) + ' > td:nth-child(19) > nobr > a')[0].text
                net_profit_after_tax = float(net_profit_after_tax.replace(',',''))
                if net_profit_after_tax > 0:
                    eps_count = eps_count + 1
                    print(net_profit_after_tax)
                else:
                    print(net_profit_after_tax)
if eps_count >= 9:
    print('合格標準: 10 年裡至少有 9 年EPS > 0')


# -----------------------------------合格標準: 5 年裡至少ROE要 > 15% -----------------------------------
roe_count = 0
for i in range(0, 5):
        row_data = soup.select('#row' + str(i) + ' > td:nth-child(1) > nobr')   
        #print(row_data[0].text)
        if row_data[0].text == str_years:
            for j in range(i, 6):
                net_profit_after_tax = soup.select('#row' + str(j) + ' > td:nth-child(17) > nobr > a')[0].text
                #print(net_profit_after_tax)
                net_profit_after_tax = float(net_profit_after_tax.replace(',',''))
                if net_profit_after_tax > 15:
                    roe_count = roe_count + 1
                    print(net_profit_after_tax)
                else:
                    print(net_profit_after_tax)
if roe_count >= 4:
    print('合格標準: 5 年裡至少有 4 年EPS > 15%')