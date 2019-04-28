#!/bin/env python
"""

@author: zesham2
"""

#BP is Booking Paty
#BPLEI LEI of the booking Party
#CPSC Counterparty ShortCode
#CPLEI Counterparty LEI
#VPC Venue Product Code of the Traded contract
#ISIN the ISIN of the contract executed
#LOT The lot size of the trade
#BUCKET Spot or Other
#EEOTC  Yes or No
import pprint
from multiprocessing import Pool


ListofTradeFile = [\
#BP   :BPLEI: CPSC:CPLEI:VPC       :ISIN       :LOT:BUCKET:EEOTC
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45567:41:SPOT:EEOTCNo',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45567:-82:SPOT:EEOTCNo',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45567:18:SPOT:EEOTCNo',
'HyperionSystemBEL:LEIABC:CSFB:LEICSFB:VPC_COPPERFU:ISIN45567:32:SPOT:EEOTCNo',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45567:-51:SPOT:EEOTCNo',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN4467:77:SPOT:EEOTCNo',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_TINFU:ISIN453456:-86:OTHER:EEOTCNo',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45567:-77:SPOT:EEOTCNo',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45567:-4:SPOT:EEOTCyes',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45567:40:SPOT:EEOTCyes',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45589:40:OTHER:EEOTCyes',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45567:-21:SPOT:EEOTCNo',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_TINFU:ISIN41233676:36:OTHER:EEOTCNo',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45567:14:SPOT:EEOTCNo',
'HyperionSystemBEL:LEIABC:VOWGDE:LEITGHJI:VPC_TINFU:ISIN4123456:-78:OTHER:EEOTCNo',
'HyperionSystemBEL:LEIABC:DEUTCHEBAK:LEIDEF:VPC_LEADFU:ISIN45567:45:SPOT:EEOTCNo']


"""
BP booking party
CP couterparty
"""


ListofTradesBP={}
ListofTradesCP={}

for trade in ListofTradeFile:
    (bp,bplei,cp,cplei,vpc,isin,lotsqty,spotorother,eeotcflag)= trade.split(":")
    keyBP= bp +"_"+bplei +"_"+vpc+ "_" +isin+"_"+ spotorother+"_"+eeotcflag
    keyCP= cp +"_"+cplei +"_"+vpc+ "_" +isin+"_"+ spotorother+"_"+eeotcflag
    if keyBP not in ListofTradesBP:
          ListofTradesBP[keyBP]=list()
    ListofTradesBP[keyBP].append(lotsqty)
    if keyCP not in ListofTradesCP:
          ListofTradesCP[keyCP]=list()
    ListofTradesCP[keyCP].append(lotsqty)

#print "One",(ListofTradesBP)   
#print "Two",(ListofTradesCP)   

ListofTradesBP2={}
ListofTradesCP2={}


def calcBPBreakdown():
    qty=0
    for keyBP in ListofTradesBP:
        qty=ListofTradesBP[keyBP]
        qtyTwo=0
        qtyies=0
        for qtyies in qty:
            qtyTwo += int(qtyies)
        ListofTradesBP2[keyBP]=qtyTwo

def calcCPBreakdown():
    qty=0
    for keyCP in ListofTradesCP:
        qty=ListofTradesCP[keyCP]
        qtyTwo=0
        qtyies=0
        for qtyies in qty:
            qtyTwo += int(qtyies)
        ListofTradesCP2[keyCP]=qtyTwo

#calcBPBreakdown()
#calcCPBreakdown()



pool = Pool()
result1 = pool.apply_async(calcBPBreakdown)    # evaluate "solve1(A)" asynchronously
result2 = pool.apply_async(calcCPBreakdown)    # evaluate "solve2(B)" asynchronously
answer1 = result1.get(timeout=10)
answer2 = result2.get(timeout=10)

if __name__ == '__main__':
    freeze_support()

pp=pprint.PrettyPrinter(width=1)

print "\n\n>>>>>>Monitoring: BookingParty "
pp.pprint(ListofTradesBP2)

print "\n\n >>>>>>> \n\n\n >>>>>>>>> Reporting: BookingParty \n",
pp.pprint(ListofTradesBP2)
print "\n\n >>>>>>>>>Reporting: Client \n", 
pp.pprint(ListofTradesCP2)
#for trades in ListofTradeFile :
 #   trades.partition(":")
    
#LofT_file_kv = [(keyBP.split(":")[0], value) 
 #                  for keyBP, value in (elem.split(":")[0] for elem in ListofTradeFile)]
