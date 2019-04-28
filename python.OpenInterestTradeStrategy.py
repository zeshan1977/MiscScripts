# -*- coding: utf-8 -*-

import asyncio
from pyppeteer import launch
import os
from datetime import datetime
"""
import re
from bs4 import BeautifulSoup
import requests
import pprint
import time
from time import gmtime, strftime
import pandas as pd
import urllib3 as url
import sys
"""

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

asyncio.get_event_loop().run_until_complete(mainfunc())




"""
sArgument=0


try:
    if sys.argv[1]:
        sArgument=sys.argv[1]
except:
    print "Usage: " + sys.argv[0] + "URL"
    exit

print "Arguement " + sArgument
if sArgument:
    print "Running for:" +  sArgument
else:
    print "Usage: " + sys.argv[0] + "URL"
    exit
    
searchObj=""

searchObj=re.search(r'http',sArgument,re.I)

"""


#r  = requests.get("https://finance.yahoo.com/quote/AMZN/options?p=AMZN&date=1539907200&straddle=false",verify=False)


        
    
"""
soup = BeautifulSoup(data,"lxml")
divs = soup.find_all("table", {"class":"calls table-bordered W(100%) Pos(r) Bd(0) Pt(0) list-options"})

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
        rowtext.append(strftime("%H%M", time.localtime()))
        rowtext.append(lastprice)
        rowtext.append(strftime("%m/%d/%Y",time.localtime()))
        print (rowtext[0])

   

       #row.split

        #if(row.text.find("PHONE") > -1):

        #   print(row.text)



"""
