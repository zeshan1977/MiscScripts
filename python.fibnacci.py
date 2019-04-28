
def fib(n):
    newlist=list()
    newlist[0]=1
    newlist[1]=1
    i = 2
    for i in range(n):
        newlist[i]= newlist[i-2] + newlist[i-1]
    return newlist 

n = 9
newlist1=fib(n)
for inti in range(n):
    print (newlist1[inti])
