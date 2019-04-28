import json
import requests
import collections
from datetime import datetime
'''
url = 'http://www.reddit.com/r/all/top/.json'
#req = urllib.request.Request(url)

response=requests.get(url)
data=response.json()
data2=json.dumps(data,indent=2)

print (data2)
'''



'''
// "latest" endpoint - request the most recent exchange rate data

http://data.fixer.io/api/latest

    ? access_key = YOUR_ACCESS_KEY
    & base = GBP
    & symbols = USD,AUD,CAD,PLN,MXN

// M, click on the URL above to get the most recent exchange
// rates for USD, AUD, CAD, PLN and MXN


Step 3: Integrate into your application

This was barely scratching the surface of the fixer API. For specific integration guides and code examples, please have a look at the API's Documentation.

Should you require assistance of any kind, please get in touch at support@fixer.io.

'''
url2="http://data.fixer.io/api/latest?access_key=3264b4768ba6da5be2ec9ea2342b76c4"

response2=requests.get(url2)
currencydata=response2.json()
currdata=json.dumps(currencydata,indent=2)
print (" Time %s", datetime.now())
#print (currdata)

currdata3=json.loads(currdata)
print ("key", currdata3['rates'].keys())
print ("Val ",currdata3['rates'].values())

#for itemsk,itemsv in currdata3['rates'].items():
for itemsk,itemsv in currdata3['rates'].items():
   print (datetime.now(),"|",itemsk,"|",itemsv)
   ''' Now adding this information to a dATABASE
   Python MySQL Insert Into Table
Insert Into Table

To fill a table in MySQL, use the "INSERT INTO" statement.
Example

Insert a record in the "customers" table:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
Insert Multiple Rows

To insert multiple rows into a table, use the executemany() method.

The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:
Example

Fill the "customers" table with data:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
Get Inserted ID

You can get the id of the row you just inserted by asking the cursor object.

Note: If you insert more that one row, the id of the last inserted row is returned.
Example

Insert one row, and return the ID:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

    

##parsing response
#r = urllib.request.urlopen(req).read()
#content = json.loads(r.decode('utf-8'))
#print (json.dumps(content,indent=4,sort_keys=True))
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
