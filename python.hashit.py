import fileinput
import sys
import pandas as pd
import pprint

file="P:\dev\pythonway\optionAnalyzer\\cleaner.v1\\amzOPTIONaNALYSIs.3.csv"

file="foo.csv"

def sum_t(x):
     # Compare the value with previous value
     m = x > x.shift()
     # If all of them are increasing then return Up
     if m.sum() == len(m)-1:
         return 'UP'
     # if all of them are decreasing then return Down
     elif m.sum() == 0:
         return 'DOWN'
     # else return flat
     else:
         return 'FLAT'
     
dpd2=pd.read_csv(file,header=3)
dpd2.columns= ['Contract_Name','Last_Trade_Date','Strike','Last_Price', 'Bid', 'Ask','Change','%Change','Volume','Open_Interest','Implied_Volatility','Time_of_day','Underlying_Price','Date']
 #print dpd2['Open_Interest']
 #dpd2['Open_Interest']=dpd2['Open_Interest'].str.replace(",",".").astype(float)
 #dpd2['Contract_Name']=dpd2['Contract_Name'].str.replace(",",".").astype(str)
dpd2['Underlying_Price']=dpd2['Underlying_Price'].astype(float)
print dpd2.dtypes
  
dpd3=dpd2.sort_values(['Open_Interest'])
  #Below works
 #dpd4= dpd3.groupby('Contract_Name')['Open_Interest'].sum()
 #dpd5= dpd3.groupby('Contract_Name')['Open_Interest'].apply(sum_t)
 #Generate new Col as contract_Date a concatenation of the contract_name and the date
dpd3['Contract_Date']=dpd2['Contract_Name'].map(str) +"_"+dpd2['Date'].map(str)
 #dpd4= dpd3.groupby('Contract_Date')['Open_Interest'].sum()
 #dpd5= dpd3.groupby('Contract_Date')['Open_Interest'].apply(sum_t)
 #dpd6= dpd3.groupby('Contract_Date')['Underlying_Price'].apply(sum_t)
dpd4= dpd3.groupby('Contract_Name')['Open_Interest'].sum()
dpd5= dpd3.groupby('Contract_Name')['Open_Interest'].apply(sum_t)
   #grouped_df = df.groupby('A')
  #for key, item in grouped_df:
  #   print(grouped_df.get_group(key), "\n\n")
    
for key, item in dpd5.iteritems():
     print key + "-->"+ item
    
 #pprint.pprint(dpd5)
 #print contracts_trend.dtypes

#def extractOptionName(scontractname):
#    return "foo"
   
