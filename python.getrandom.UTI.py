import random
import string
from collections import Counter

#random(seed=1)

def randomString(strLen=32):
    letters=list(string.ascii_uppercase)
    numbers=[1,2,3,4,5,6,7,8,9,0]
    letters.extend(numbers)
    #print (letters)
    return ''.join(str(random.choice(letters)) for i in range(strLen))

llist=list()
llist2=list()

for i in range(1000):
    i=i+1
    #print (randomString(32))
    llist.append(randomString(32))
    llist2.append("ABC")
    #llist.append(list(randomString(32)))
    

#print (Counter(llist).values())

def times_so_far_generator(lllist,list2):
    counter = Counter()
    for num in lllist:
        counter[num] += 1
        #yield counter[num]
    print (counter[num])
    
    counter1 = Counter()
    for num1 in list2:
        counter1[num1] += 1
        #yield counter[num]
    print (counter1[num1])
    
print (times_so_far_generator(llist,llist2))








