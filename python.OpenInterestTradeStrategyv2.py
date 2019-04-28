# -*- coding: utf-8 -*-


"""
Open Interest Trading Rules

i)When price UP and OI UP > BUY

ii)Price Crosses Yesterday High and OI INCREASES then BUY

ii)When price DOWN and OI UP > SELL Short)
"""
from bs4 import BeautifulSoup    
import urllib3 as url
import time
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

f=open ("D:\\x\\dev\\output.html","r")
data=f.read()
f.close()
#
#Above file has 
#Listo f optio chains as per expiry date drop down
#
#div class="Fl(start) Pend(18px) option-contract-control drop-down-selector" data-reactid="4"><select class="Fz(s)" data-reactid="5">
#       <option selected="" value="1551398400" data-reactid="6">March 1, 2019</option><option value="1552003200" data-reactid="7">March 8, 2019</option>
#       <option value="1552608000" data-reactid="8">March 15, 2019</option><option value="1553212800" data-reactid="9">March 22, 2019</option>
#        <option value="1553817600" data-reactid="10">March 29, 2019</option><option value="1554422400" data-reactid="11">April 5, 2019</option>
#        
#

soup = BeautifulSoup(data,"lxml")
divs = soup.find_all("table", {"class":"calls table-bordered W(100%) Pos(r) Bd(0) Pt(0) list-options"})
#
#select = soup.find('select', class_="Fz(s)")
#for value in select.stripped_strings:
#    print (value)

#for option in soup.find_all('option'):
for option in soup.find('select', class_="Fz(s)"):
    print ("value: " + option['value'] + " Text: "+ option.text)

    
def get_stock_price(name):
    #http = url.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=cert.where())
    http = url.PoolManager()
    html_doc = http.request('GET', 'https://finance.yahoo.com/quote/' + name + '?p=' + name)
    soup = BeautifulSoup(html_doc.data, 'html.parser')
    return soup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text()

lastprice=get_stock_price("AMZN")


for div in divs:
    row = ''
    rows = div.findAll('tr')
    for row in rows:
        td=row.find_all('td')
        rowtext = [i.text for i in td]
        #rowtext.append(strftime("%H%M", gmtime()))
        #rowtext.append(strftime("%m%d%Y", gmtime()))
        rowtext.append(time.strftime("%H%M", time.localtime()))
        rowtext.append(lastprice)
        rowtext.append(time.strftime("%m/%d/%Y",time.localtime()))
        print (rowtext[0])

   

       #row.split

        #if(row.text.find("PHONE") > -1):

        #   print(row.text)



