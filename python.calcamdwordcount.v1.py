import re
import antigravity


def calc(x,y,*argv):
    for arg in argv:
        if arg == "add":
            return x+y
        if arg == "multiply":
            return x*y
    return "err"

print calc(2,4,"add")

def countwords(line):
    hash={}
    for words in line.split():
        hash[words] = hash.get(words,0)+1
    for key,value in hash.items():
        print ">>" + str(key) +":"+str(value)


countwords("This is a test string with test words and test words is a test")
import itertools as it

num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", num)
num.sort()
new_num = list(num for num,_ in it.groupby(num))
print("New List", new_num)


"""
import numpy as np
from sklearn.svm import SVC
from sklearn import datasets
import matplotlib.pyplot as plt
# dataset
X, y = datasets.make_classification(n_samples=10, n_features=2,n_redundant=0, n_classes=2, random_state=1, shuffle=False)

clf = SVC(kernel='rbf')
#, gamma=1)
clf.fit(X, y)
print "#Errors:"  
print np.sum(y != clf.predict(X))
clf.decision_function(X)
# Usefull internals:
# Array of support vectors
clf.support_vectors_
# indices of support vectors within original X
np.all(X[clf.support_,:] == clf.support_vectors_)
"""