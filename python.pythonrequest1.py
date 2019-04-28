import urllib.request
import json
import requests

url = 'http://www.reddit.com/r/all/top/.json'
req = urllib.request.Request(url)

#r=requests.get(url)


##parsing response
r = urllib.request.urlopen(req).read()
content = json.loads(r.decode('utf-8'))
print (json.dumps(content,indent=4,sort_keys=True))
#data=json.loads(content)
#print (json.dumps(data,indent=4,sort_keys=True))
#print (len(content['data']))







# counter = 0

##parcing json
####for item in cont['data']['children']:
####    counter += 1
####    counter += 1
####    print("Title:", item['data']['title'], "\nComments:", item['data']['num_comments'])
####    print("----")

##print formated
####print (json.dumps(cont, indent=4, sort_keys=True))
####print("Number of titles: ", counter)
