from pandas_datareader import data as pdr 
import datetime as dt
import fix_yahoo_finance as yf
import numpy as np
import fix_yahoo_finance as yf

"""
What is VAR= "Maximum loss over a specified timeframe(1/252/days"
1.) Gather stock data and calculate periodic returns (Including the average return of each asset).

2.) Generate a covariance matrix based upon the periodic returns.

3.) Calculate the portfolio mean and standard deviation based upon the defined weights in each asset and amount invested in the portfolio.

4.) Calculate the inverse of the normal cumulative distribution with a specified probability, standard deviation, and mean.

5.) Estimate the value at risk for the portfolio by subtracting the initial investment from the calculation in step 4
"""

"""
consider a portfolio that includes only one security, stock ABC. Suppose $500,000 is invested in stock ABC. The standard deviation over 252 days,
or one trading year, of stock ABC is 7%. 
Following the normal distribution, the 95% confidence level has a z-score(How far awayi A Z-score is a numerical measurement of 
a value's relationship to the mean in a group of values. If a Z-score is 0, it represents the score as identical to the mean score)
of 1.645. 
The value at risk in this portfolio is $57,575 ($500000*1.645*.07). 
Therefore, with 95% confidence, the maximum loss will not exceed $57,575 in a given trading year.

The value at risk of a portfolio with two securities can be determined by first calculating the portfolio's volatility. 
Multiply the square of the first asset's weight by the square of the first asset's standard deviation and
Add it to the square of the second asset's weight multiplied by the square of the second asset's standard deviation. 
Add that value to two, multiplied by the weights of the first and second assets by the correlation coefficient between the two assets, 
multiplied by asset one's standard deviation and asset two's standard deviation. 
Then multiply the square root of that value by the z-score and the portfolio value.

FRTB: clear differentiation between banking and trading books, and to raise the bar for internal models.
"""
yf.pdr_override() # <== that's all it takes :-)

lStocks=['FB','AMZN','NFLX','GOOG','AAPL']


#Weights in each stock
weights = np.array([.2, .2, .2, .2, .2])
 
#initial investment
initial_investment = 100000
 
#Override API
yf.pdr_override() 
 

# download Panel
print "Start Time: " + str(dt.datetime.now())

#data = pdr.get_data_yahoo(lStocks, start="2018-01-01", end="2018-09-30")["Close"]
data = pdr.get_data_yahoo(lStocks, start="2018-01-01", end="2018-09-30")["Open","Close"]

print "End Time: " +str(dt.datetime.now())
 #Calculate periodic returns)
returns = data.pct_change()
 

#Generate Var-Cov matrix
cov_matrix = returns.cov()
 
#Calculate mean returns for each stock
avg_rets = returns.mean()
 
#Calculate Portfolio Mean
port_mean = avg_rets.dot(weights)
 
#Calculate Portfolio SHyperionSystemEV
port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))
 
#Mean Investment
mean_investment = (1+port_mean) * initial_investment
             
#Standard Deviation Investment
stdev_investment = initial_investment * port_stdev
 
#Cutoff Point 
conf_level0 = 0.001
conf_level1 = 0.01
conf_level2 = 0.05
 
from scipy.stats import norm
 
cutoff0 = norm.ppf(conf_level0, mean_investment, stdev_investment)
cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)
cutoff2 = norm.ppf(conf_level2, mean_investment, stdev_investment)
 
#Calculate PDF (If Desired)
#print(norm.cdf(cutoff0, mean_investment, stdev_investment))
 
#Calculate 1 Day VaR at different confidence intervals 
var_1d0 = initial_investment - cutoff0
var_1d1 = initial_investment - cutoff1
var_1d2 = initial_investment - cutoff2
 
#-------------------------Optional--------------------------#
#Calculate n Day VaR in loop
num_days = 100
for x in range(1, num_days):    
    #print(str(x) + " day VaR at 99.99% confidence level: " + str(np.round(var_1d0 * np.sqrt(x),2)))
    print " "+str(x) + " day VaR at 99.99% confidence level: " + str(np.round(var_1d0 * np.sqrt(x),2))
    
#Plot Results On Bar Chart
import matplotlib.pyplot as plt
import pandas as pd
 
data = {'99.99%': np.round(var_1d0,2), '99%': np.round(var_1d1, 2), '95%': np.round(var_1d2, 2)}
df = pd.DataFrame(data,index=[0]) 
 
df.plot(kind = 'bar')
plt.suptitle('Portfolio VaR', fontsize=20)
plt.ylabel('VaR ($)', fontsize=16)
plt.show()  
