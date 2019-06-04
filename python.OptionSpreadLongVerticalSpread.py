# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:36:42 2019

@author: zee
"""

from bs4 import BeautifulSoup    
import urllib3 as url
import time
import datetime
import asyncio
from pyppeteer import launch
import os
from datetime import datetime

date_string = f'{datetime.now():%Y-%m-%d-%H:%M:%S%z}'
url.disable_warnings(url.exceptions.InsecureRequestWarning)

sStock ="FB"
fCurrentStockPrice="75.00"
fBuyLongStrike="70"
fBuyLongCallPrice="7.50"
fBreakEvenStockPriceBuyNakedCall=fStrike+fCallPrice # Current price has to go above this price for it to break even
dMultiplier=100
#buy above option and sell and OTM call option cheaper
fSellShortStike="80"
fSellShortCallPrice="2.5"

 



""" Commenting below  as it pulls data only : Mohammed Z 6/3/2019
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

urlsToGrab=[]
urlsToGrab2=[]
for option in soup.find('select', class_="Fz(s)"):
    print ("value: " + option['value'] + " Text: "+ option.text)
    urlsToGrab.append("https://finance.yahoo.com/quote/AMZN/options?p=AMZN&date="+ option['value'])
    urlsToGrab2.append(option.text)
    
data=""
async def mainfunc():
    browser = await launch()
    page = await browser.newPage()
    for urls,urlstext in zip (urlsToGrab,urlsToGrab2):
        await page.goto(urls)
        #print (await page.content())
        dir_path=os.path.dirname(os.path.realpath(__file__))
        dir_paths=str(dir_path)
        urlstext.replace(" ","")
        dir_paths=dir_paths + "\output."+urlstext+".html"
        print (dir_paths)
        #with open (dir_paths,"w") as f:
        #   f.write(await page.content())
#        await browser.close()   
        

asyncio.get_event_loop().run_until_complete(mainfunc())


    

"""
import asyncio
from pyppeteer import launch
import os
from datetime import datetime

date_string = f'{datetime.now():%Y-%m-%d-%H:%M:%S%z}'

async def mainfunc():
    browser = await launch()
    print ("Omuamua1:"+date_string)
    page = await browser.newPage()
    print ("Omuamua2:"+date_string)
    print ("Omuamua3:"+date_string)
    await page.goto('https://finance.yahoo.com/quote/AMZN/options?p=AMZN')
    print ("Omuamua4:"+date_string)
    #print (await page.content())
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print ("Omuamua5:"+date_string)
    dir_paths=str(dir_path)
    print ("Omuamua6:"+date_string)
    dir_paths = dir_paths + "\output."+date_string +".html"
    print ("Omuamua7:"+date_string)
    print ("writing out to:"+ dir_paths+" \n")
    print ("Omuamua8:"+date_string)
    with open (dir_paths,"w") as f:
        f.write(await page.content())
        print ("Omuamua9:"+date_string)
    await browser.close()
    data=""
    with open (dir_paths,"a") as f1:
        data=f1.read()

    print ("Omuamua10:"+date_string)



    
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



asyncio.get_event_loop().run_until_complete(mainfunc())
"""
