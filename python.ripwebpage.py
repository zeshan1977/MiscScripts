# -*- coding: utf-8 -*-
"""
 Created on Thu Aug 23 13:14:09 2018
  @author: zesham2
"""
from bs4 import BeautifulSoup
import requests
import pprint
import time
from time import gmtime, strftime
import pandas as pd
import urllib3 as url
import sys
import re
 
"""
sArgument=0
#try:
#     if sys.argv[1]:
#         sArgument=sys.argv[1]
#except:
#     print "Usage: " + sys.argv[0] + "URL"
#     exit
#   print "Arguement " + sArgument
#if sArgument:
#     print "Running for:" +  sArgument
#else:
#     print "Usage: " + sys.argv[0] + "URL"
#     exit

searchObj=""
searchObj=re.search(r'http',sArgument,re.I)
    #r  = requests.get("https://finance.yahoo.com/quote/AMZN/options?p=AMZN&date=1555545600&straddle=false",verify=False)
"""    
sArgument="https://finance.yahoo.com/quote/AMZN/options?p=AMZN&date=1555545600&straddle=false"
r  = requests.get(sArgument,verify=False)
data = r.text
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
         print rowtext[0]
    
        #row.split
         #if(row.text.find("PHONE") > -1):
         #   print(row.text)
    
