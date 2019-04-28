import re

def filter_string(item):
    res = re.search('\S+',item)
    if res:
       return 1
    return 0

def filter_list(l):
    for i in l:
        if filter_string(i):
            l.pop(i)
    return l

print filter_list([1,2,3,'forty five'])
