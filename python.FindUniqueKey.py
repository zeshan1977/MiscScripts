
# input dictionary
d=[{"TheMatrix":"movies"},
   {"cwanygivenSunday": "sports"},
   {"KurtCobain": "music"},
   {"What": "music"},
   {"Bella":"music"}, 
   {"Bella":"movies"},
   {"Bella":"movies"},
   {"pop":"sports"},
   {"popp":"news"},
   {"pop":"sports"}]
"""
# fetch keys
b=[j[0] for i in d for j in i.items()]

# print output
for k in list(set(b)):
    print ({0}: {1}).format(k, b.count(k))

for myKey in d.keys():
    print "{0}: {1}".format(myKey, len(d[myKey])
"""

from collections import Counter
from itertools import chain

counts = Counter(chain.from_iterable(e.keys() for e in d))
print (counts)
