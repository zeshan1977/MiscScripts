import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error,r2_score
 
#Load Te Dataset
prices = datasets.load_boston()

#Use only one feature for this testing
prices_X=prices.data[:,np.newaxis,2]

#Split the data into traiing and testing data sets
prices_X_train=prices_X[:-20]
prices_X_test=prices_X[-20:]

#Split the targets into traiing and testing data sets
prices_Y_train=prices.target[:-20]
prices_Y_test= prices.target[-20:]

#create lin regressiomodel object
regres=linear_model.LinearRegression()

#Train the model using trainngdata sets
regres.fit(prices_X_train, prices_Y_train)


#Make predictions using th testing datatset
prices_Y_pred=regres.predict(prices_X_test)




#create a supportvectormacvhnie bject
svm_regres=linear_model.SupportVectorMachine()

#Train the model using trainngdata sets
svm_regres.fit(prices_X_train, prices_Y_train)


#Make predictions using th testing datatset
svm_prices_Y_pred=regres.predict(prices_X_test)