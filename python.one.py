from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

yf.pdr_override() # <== that's all it takes :-)
lStocks = ["Fb","AMZN","NFLX","GOOG"]

# download dataframe
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
