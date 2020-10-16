
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=IS_M_QUAR_ACC&STOCK_ID=2330'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
datastream = requests.get(url, headers = headers)
soup = BeautifulSoup(datastream.content,'lxml')
#print(soup)

for n in range(0, 80):
    row_data1 = soup.select('#row' + str(n) + ' > td:nth-child(1) > nobr')

    # 取得最近一季的營業利益 and 取得最近一季的稅前利益
    if row_data1 == []:
        pass
    elif row_data1[0].text == '營業利益':
        now1a = soup.select('#row' + str(n) + ' > td:nth-child(3) > nobr')[0].text
        now1a = now1a.replace(',','')
        #print(now1a)
    elif row_data1[0].text == '稅前淨利':
        now1b = soup.select('#row' + str(n) + ' > td:nth-child(3) > nobr')[0].text
        now1b = now1b.replace(',','')
        #print(now1b)
    elif row_data1[0].text == '其他利益及損失':
        now1c = soup.select('#row' + str(n) + ' > td:nth-child(3) > nobr')[0].text
        now1c = now1c.replace(',','')
        #print(now1c)
    elif row_data1[0].text == '合併稅後淨利':
        now1d = soup.select('#row' + str(n) + ' > td:nth-child(3) > nobr')[0].text
        now1d = now1d.replace(',','')
        #print(now1d)

## ------------------------------------合格標準: 本業收入比例 > 80%------------------------------------
## 本業收入比率公式 = 近 1 季營業利益 / 近 1 季稅前利益
#income_ratio = (float(now1a) / float(now1b))*100
#print('Income Ratio: {:.2f}%'.format(income_ratio))

# ------------------------------------合格標準: 業外損失比率 < 20%------------------------------------

# 業外損失比率 = 近 1 季其他利益及損失 / 近 1 季稅後淨利
loss_ratio_outside_business = (float(now1c) / float(now1d))*100
print('Loss Ratio Outside Business: {:.2f}%'.format(loss_ratio_outside_business))



