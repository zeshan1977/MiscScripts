
#import pandas.io.data as web
import pandas_datareader as web
	
all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
	try:
	        all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2003', '1/1/2013')
		price = DataFrame({tic: data['Adj Close']
                   for tic, data in all_data.iteritems()})
		volume = DataFrame({tic: data['Volume']
                    for tic, data in all_data.iteritems()})
	except:
		print "Can't find :", ticker

