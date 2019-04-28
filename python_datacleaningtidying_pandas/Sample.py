import pandas as pd
datadir="pydatadc_2018-tidy/data/"

df = pd.read_csv(datadir+'gapminder.tsv',sep='\t')
print (df.head())

print (df.columns)

#df.loc[df.year>=1960]
print (df.shape)
#filter col 
print (df.loc[df.year>=2000])
df1= df.loc[df.year>=2010,'country']
#df1= df.loc[df.year>=2010,df.country == "Togo"]

#https://www.youtube.com/watch?v=3ZWuPVWq7p4
#Data science in Python: pandas, seaborn, scikit-learn
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv',index_col=0)
print (data.head())
print (data.shape) # rows and col
"""
[200 rows x 6 columns]
      TV  radio  newspaper  sales
1  230.1   37.8       69.2   22.1
2   44.5   39.3       45.1   10.4
3   17.2   45.9       69.3    9.3
4  151.5   41.3       58.5   18.5
5  180.8   10.8       58.4   12.9
"""
"""
#Advertising dollars per channel and resulting sales 
#Predict Sales by 

import seaborn as sns

sns.pairplot(data,x_vars=['TV','radio','newspaper'],y_vars='sales',aspect=0.7,size=7)
sns.pairplot(data,x_vars=['TV','radio','newspaper'],y_vars='sales',aspect=1,size=7)
sns.pairplot(data,x_vars=['TV','radio','newspaper'],y_vars='sales',aspect=0.7,size=7,kind='reg')
"""

ufo=pd.read_csv('http://bit.ly/uforeports')
#print (ufo.head(10))
#print (ufo.shape)
print (ufo.loc[0:2,:])
print (ufo.loc[:,'Cty':'State'])
print (ufo.loc[ufo.City=='Oakland','State'])
print (ufo.describe)