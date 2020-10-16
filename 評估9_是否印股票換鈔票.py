
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

url = 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?STEP=DATA&STOCK_ID=2330&RPT_CAT=BS_M_YEAR&QRY_TIME=20194'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
           'referer': 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=BS_M_QUAR&STOCK_ID=2330'}
datastream = requests.get(url, headers = headers)
soup = BeautifulSoup(datastream.content,'lxml')

for n in range(0, 80):
    row_data1 = soup.select('#row' + str(n) + ' > td:nth-child(1) > nobr')
    #print(row_data1)
    if row_data1 == []:
        pass
    elif row_data1[0].text == '股本合計':
        now1a = soup.select('#row' + str(n) + ' > td:nth-child(2) > nobr')[0].text
        now1a = now1a.replace(',','')
        print(now1a)
        now1b = soup.select('#row' + str(n) + ' > td:nth-child(12) > nobr')[0].text
        now1b = now1b.replace(',','')
        print(now1b)
    else:
        pass

now1a = float(now1a)
now1b = float(now1b)
result = ((now1a-now1b)/now1a)*100
if result < 20:
    print('股本膨脹比率: {:.2f}'.format(result))







































#url = 'https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2330'
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#datastream = requests.get(url, headers = headers)
#soup = BeautifulSoup(datastream.content,'lxml')

#datenow = datetime.datetime.now()
#yearnow = datenow.year
#str_yearnow = str(yearnow)

#soup = soup.find('div', attrs={'id':'divDetail'})
#soup = soup.find('table', attrs={'class':'solid_1_padding_4_0_tbl'})
#soup = soup.find_all('td')

#count = 0
#for q in range(yearnow, yearnow-8, -1):
#    #print(q)
#    for i in range(0, 600):
#        #print(soup[i].text)
#        if soup[i].text == str(q):
#            #print('i find ******************************************************')
#            #print(q)
#            print(str(q)+'年發放股利: '+soup[i+1].text)
#            if float(soup[i+1].text) > 0:
#                count = count + 1
#            break
#if count == 8:
#    print('符合條件: 連續'+str(count)+'年發放股利! Good!')
##-------------------------------------------------------------------------------------------


#url = 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=CF_M_QUAR_ACC&STOCK_ID=2330'
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#datastream = requests.get(url, headers = headers)
#soup = BeautifulSoup(datastream.content,'lxml')
##print(soup)

#for n in range(0, 80):
#    row_data1 = soup.select('#row' + str(n) + ' > td:nth-child(1)')
#    #print(row_data1)
#    if row_data1 == []:
#        pass
#    elif row_data1[0].text == '營業活動之淨現金流入(出)':
#        now1a = soup.select('#row' + str(n) + ' > td:nth-child(2) > nobr')[0].text
#        now1a = now1a.replace(',','')
#        #print(now1a)
#    elif row_data1[0].text == '投資活動之淨現金流入(出)':
#        now1b = soup.select('#row' + str(n) + ' > td:nth-child(2) > nobr')[0].text
#        now1b = now1b.replace(',','')
#        #print(now1b)

#now1a = float(now1a)
#now1b = float(now1b)
#FCF = now1a + now1b
#print("\n")
#print('營業活動現金流: {:.2f}'.format(now1a))
#print('自由活動現金流: {:.2f}'.format(FCF))
#if now1a and FCF > 0:
#    print('符合條件: 營業活動現金流 and 自由活動現金流 > 0, Good!')
##-------------------------------------------------------------------------------------------






















#for n in range(0, 80):
#    row_data1 = soup.select('#row' + str(n) + ' > td:nth-child(1)')
#    #print(row_data1)
#    if row_data1 == []:
#        pass
#    elif row_data1[0].text == str_yearnow:
        #now1a = soup.select('#row' + str(n) + ' > td:nth-child(2) > nobr')[0].text
        #now1a = now1a.replace(',','')
        #print(now1a)
        

#divDetail > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > nobr > b






#import requests
#from bs4 import BeautifulSoup
#import pandas as pd
#import datetime

#date = datetime.datetime.now()
#int_years = date.year-1
#str_years = str(date.year-1)

#url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=2330'
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#datastream = requests.get(url, headers = headers)
#soup = BeautifulSoup(datastream.content,'lxml')
##print(soup)

## -----------------------------------合格標準: 10 年裡至少要有 9 年EPS要 >0 -----------------------------------
#eps_count = 0
#for n in range(0, 5):
#        row_data = soup.select('#row' + str(n) + ' > td:nth-child(1) > nobr')   
#        if row_data[0].text == str_years:
#            for m in range(n, 11):
#                net_profit_after_tax = soup.select('#row' + str(m) + ' > td:nth-child(19) > nobr > a')[0].text
#                net_profit_after_tax = float(net_profit_after_tax.replace(',',''))
#                if net_profit_after_tax > 0:
#                    eps_count = eps_count + 1
#                    print(net_profit_after_tax)
#                else:
#                    print(net_profit_after_tax)
#if eps_count >= 9:
#    print('合格標準: 10 年裡至少有 9 年EPS > 0')


## -----------------------------------合格標準: 5 年裡至少ROE要 > 15% -----------------------------------
#roe_count = 0
#for i in range(0, 5):
#        row_data = soup.select('#row' + str(i) + ' > td:nth-child(1) > nobr')   
#        #print(row_data[0].text)
#        if row_data[0].text == str_years:
#            for j in range(i, 6):
#                net_profit_after_tax = soup.select('#row' + str(j) + ' > td:nth-child(17) > nobr > a')[0].text
#                #print(net_profit_after_tax)
#                net_profit_after_tax = float(net_profit_after_tax.replace(',',''))
#                if net_profit_after_tax > 15:
#                    roe_count = roe_count + 1
#                    print(net_profit_after_tax)
#                else:
#                    print(net_profit_after_tax)
#if roe_count >= 4:
#    print('合格標準: 5 年裡至少有 4 年EPS > 15%')
