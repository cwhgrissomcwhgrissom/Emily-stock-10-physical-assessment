import requests
from bs4 import BeautifulSoup
import datetime

url = 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?STEP=DATA&STOCK_ID=2330&RPT_CAT=BS_M_YEAR&QRY_TIME=20194'
headers = {'user-agent':'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.108 safari/537.36',
           'referer': 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=BS_M_QUAR&STOCK_ID=2330'}
list_req = requests.post(url, headers=headers)
print(list_req)
soup = BeautifulSoup(list_req.content, 'lxml')
#print(soup)

for n in range(0, 80):
    row_data1 = soup.select('#row' + str(n) + ' > td:nth-child(1) > nobr')
    if row_data1 == []:
        pass
    else:
        if row_data1[0].text == '應收帳款':
            a1 = soup.select('#row' + str(n) + ' > td:nth-child(2) > nobr')[0].text
            a1 = a1.replace(',','')
            #print(a1)
        elif row_data1[0].text == '存貨':
            a2 = soup.select('#row' + str(n) + ' > td:nth-child(2) > nobr')[0].text
            a2 = a2.replace(',','')
            #print(a2)
        else:
            pass

url = 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?STEP=DATA&STOCK_ID=2330&RPT_CAT=IS_M_YEAR&QRY_TIME=20194'
headers = {'user-agent':'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.108 safari/537.36',
           'referer': 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=BS_M_QUAR&STOCK_ID=2330'}
list_req = requests.post(url, headers=headers)
print(list_req)
soup = BeautifulSoup(list_req.content, 'lxml')
#print(soup)

for n in range(0, 30):
    row_data1 = soup.select('#row' + str(n) + ' > td:nth-child(1) > nobr')
    if row_data1 == []:
        pass
    else:
        if row_data1[0].text == '營業收入':
            a3 = soup.select('#row' + str(n) + ' > td:nth-child(2) > nobr')[0].text
            a3 = a3.replace(',','')
            print(n)
            print(a3)


a1 = float(a1)
a2 = float(a2)
a3 = float(a3)

result = ((a1+a2)/a3)*100
#print('營收灌水比例: ' + str(result))
print('營收灌水比例: {:.2f}%'.format(result))


















##print('')
##print('體質評估: 採IFRS後的財報, 計算出盈再率')
##print('1. 盈再率＜40%，即為低再盈率，通常是體質不錯的好公司。')
##print('2. 盈再率＞80%，偏高，不適合投資。')
##print('3. 盈再率＞200%，極可能是潛在地雷股（公司遭掏空），如已下市的電子公司博達、陞技，爆發財務危機前就有此徵兆。')
##print('------------------------------------------------------------------------------------------------------------------')

#import requests
#from bs4 import BeautifulSoup
#import datetime

#url = 'https://goodinfo.tw/stockinfo/stockfindetail.asp?step=data&stock_id=2330&rpt_cat=bs_m_year&qry_time=20194'
#headers = {'user-agent':'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.108 safari/537.36',
#           'referer': 'https://goodinfo.tw/stockinfo/stockfindetail.asp?rpt_cat=bs_m_quar&stock_id=2330'}
#list_req = requests.post(url, headers=headers)
#print(list_req)
#soup = BeautifulSoup(list_req.content, 'lxml')
##print(soup)

#def get_sum_of_4years_eps():

#    date = datetime.datetime.now()
#    int_years = date.year-1
#    str_years = str(date.year-1)
#    #print(str_years)

#    url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=2330'
#    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#    datastream = requests.get(url, headers = headers)
#    soup = BeautifulSoup(datastream.content,'lxml')
#    #print(soup)

#    for n in range(0, 5):
#        row_data = soup.select('#row' + str(n) + ' > td:nth-child(1) > nobr')   
#        if row_data[0].text == str_years:
#            net_profit_after_tax_2019 = soup.select('#row' + str(n) + '> td:nth-child(12) > nobr > a')[0].text
#            net_profit_after_tax_2018 = soup.select('#row' + str(n+1) + '> td:nth-child(12) > nobr > a')[0].text
#            net_profit_after_tax_2017 = soup.select('#row' + str(n+2) + '> td:nth-child(12) > nobr > a')[0].text
#            net_profit_after_tax_2016 = soup.select('#row' + str(n+3) + '> td:nth-child(12) > nobr > a')[0].text

#            net_profit_after_tax_2019 = net_profit_after_tax_2019.replace(',','')
#            net_profit_after_tax_2018 = net_profit_after_tax_2018.replace(',','')
#            net_profit_after_tax_2017 = net_profit_after_tax_2017.replace(',','')
#            net_profit_after_tax_2016 = net_profit_after_tax_2016.replace(',','')

#            #print(net_profit_after_tax_2019)
#            #print(net_profit_after_tax_2018)
#            #print(net_profit_after_tax_2017)
#            #print(net_profit_after_tax_2016)
#        else:
#            pass

#    sum = float(net_profit_after_tax_2019)+float(net_profit_after_tax_2018)+float(net_profit_after_tax_2017)+float(net_profit_after_tax_2016)
#    #print(sum)
#    return sum

#for n in range(0, 80):
#    row_data1 = soup.select('#row' + str(n) + ' > td:nth-child(1) > nobr')
#    if row_data1 == []:
#        pass
#    else:
#        if row_data1[0].text == '固定資產合計':
#            now = soup.select('#row' + str(n) + ' > td:nth-child(2) > nobr')[0].text
#            now = now.replace(',','')
#            #print(now)
#            pre4 = soup.select('#row' + str(n) + ' > td:nth-child(10) > nobr')[0].text
#            pre4 = pre4.replace(',','')
#            #print(pre4)
#        if row_data1[0].text == '長期投資合計':
#            now1 = soup.select('#row' + str(n) + ' > td:nth-child(2) > nobr')[0].text
#            now1 = now1.replace(',','')
#            #print(now1)
#            pre41 = soup.select('#row' + str(n) + ' > td:nth-child(10) > nobr')[0].text
#            pre41 = pre41.replace(',','')
#            #print(pre41)

#calresult = (float(now)+float(now1))-(float(pre4)+float(pre41))  
##print(calresult)
##print(get_sum_of_4years_eps())
#Reinvestment_Rate = calresult/get_sum_of_4years_eps()*100
##print(Reinvestment_Rate)
#print('Reinvestment_Rate: {:.2f}%'.format(Reinvestment_Rate))

##Notice:
##---------------------------------------------------------------
##row_data = soup.select('#row16 > td:nth-child(1) > nobr')
##print(row_data)
##if row_data == []:
##    print('************************')
##else:
##    print('pass empty')
##---------------------------------------------------------------