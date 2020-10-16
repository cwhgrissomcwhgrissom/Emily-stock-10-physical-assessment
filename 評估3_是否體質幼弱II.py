import requests
from bs4 import BeautifulSoup

url = 'https://goodinfo.tw/StockInfo/BasicInfo.asp?STOCK_ID=2301'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
datastream = requests.get(url, headers = headers)
soup = BeautifulSoup(datastream.content,'lxml')
#print(soup)

#soup = soup.select('body > table:nth-child(5) > tbody > tr > td:nth-child(3) > table.solid_1_padding_4_6_tbl > tbody > tr:nth-child(8) > td:nth-child(2) > nobr')
#soup = soup.select('body > table:nth-child(5) > tr > td:nth-child(3) > table.solid_1_padding_4_6_tbl > tr:nth-child(6) > td:nth-child(1) > nobr')

soup = soup.find('table', attrs={'class':'solid_1_padding_4_6_tbl'})
soup = soup.find_all('td')

for n in range(0, 80):
    if soup[n].text == '上市日期':
        data = soup[n].text
        print(data)
        break
    else: pass



























#soup = soup.find('table', attrs={'class':'solid_1_padding_4_6_tbl'})
#soup = soup.find_all('td')

#for n in range(0, 80):
#    if soup[n].text == '上市日期':
#        data = soup[n+1].text
#        #print(data)
#    elif soup[n].text == '資本額':
#        data1 = soup[n+1].text
#        #print(data1)
#        break

#data = list(data)
#date = []
#for i in range(0, 4):
#    date.append(data[i])
##print(date)
#str_date = "".join(date)
#int_date = int(str_date)
##print(int_date)
##print(type(int_date))
#datenow = datetime.datetime.now()
#yearnow = datenow.year
##print(yearnow)
##print(type(yearnow))
#if yearnow-int_date > 7:
#    print('上市時間: '+ str(yearnow-int_date))


#total_money = []
#data1 = list(data1)
#for j in range(0, 6):
#    if data[j] != '億':
#        total_money.append(data1[j])
#    else:
#        pass
##print(total_money)
#str_total_money = "".join(total_money)
#int_total_money = float(str_total_money)
#if int_total_money > 50:
#    print('資本額(億): ' + str(int_total_money))

## ------------------------------------------------------------------------------------------------------------------------------------------------------------

##import requests
##from bs4 import beautifulsoup
##import pandas as pd

#url = 'https://goodinfo.tw/stockinfo/stockfindetail.asp?rpt_cat=bs_m_quar&stock_id=2330'
#headers = {'user-agent':'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.108 safari/537.36'}
#datastream = requests.get(url, headers = headers)
#soup = BeautifulSoup(datastream.content,'lxml')
##print(soup)

#for n in range(55, 61):
#    #print(n)
#    row_data2 = soup.select('#row' + str(n) + ' > td:nth-child(1)')
#    #print(row_data1)

#    if row_data2 == []:
#        pass
#    elif row_data2[0].text == '每股淨值(元)':
#        now2a = soup.select('#row' + str(n) + ' > td:nth-child(2)')[0].text
#        now2a = now2a.replace(',','')
#        #print(now2a)

#if float(now2a) >= 15:
#    print('最近一季的淨值 > 15, good!!')


