from flask import Flask, jsonify,make_response,request,render_template
from flask_httpauth import HTTPBasicAuth

from datetime import datetime,timedelta
#import trade
import random
import pymongo
import string


auth = HTTPBasicAuth()


app = Flask(__name__)
sVERSION='v01'
class Person():
    def __init__(self,id,
        firstName,
		lastName,
		personCity, 
		personprov_state,
		personzip_postcode,
		#recNum = recNum
		dobDate,
		gender,
		telnumber,
		email, 
		listVisitDate):
		
        self.id=id
        self.firstName=firstName
        self.lastName=lastName
        self.personCity=personCity
        self.personprov_state=personprov_state
        self.personzip_postcode=personzip_postcode
        self.dobDate=dobDate
        self.gender=gender
        self.telnumber=telnumber
        self.email=email
        self.listVisitDate=listVisitDate
              
    def printall(self):
        print (self.__dict__ )
        
        
    def fillupPerson():
      return



#random.seed(a=None,version=4)

randFirstNameList=["Damari","Layton","Ezequiel","Asher","Finnegan","Lee" ]
randLastNameList=["Liam","Raphael","Misael","Kareem","Rafael","Bryan"]
randPersonCityList=["Brampton","Oakville","Mississauga"]

randPostCodefirst=["L"]                    
randPostCodeSecond=["5","6","7"]
randPostCodethird=list(string.ascii_uppercase)
randPostCodefour=["1","2","4"]                    
randPostCodefive=list(string.ascii_uppercase)
randPostCodesix=["3","4","5"]                    

randProvState=["ON"]
autoinc=1
autoincrementrecNum=[]
randdobDate=["1977-12-25","1979-11-3","2006-3-14","2011-01-05","2013-11-01","2012-04-02"]
randomgender=["M","F"]
randtelnumber=["212-279-0440","416-839-4479","416-838-5238"]
randemail=["foo@bar.com","mohammed@msn.com","Gunny@mcrn.hamourabi.com","Diylan@foobar.com"]


todaysDate=datetime.now()
todaysDate=todaysDate.date()

lvd =  todaysDate+timedelta(days=random.choice([-1,-2,-3,-4,-5]))
lvd1 = todaysDate+timedelta(days=-8)
lvd2 = todaysDate+timedelta(days=-10)
lvd3 = todaysDate+timedelta(days=-20)
lvd4 = todaysDate+timedelta(days=-35)
lvd5 = todaysDate+timedelta(days=-54)
lvd6 = todaysDate+timedelta(days=-300)
lastVisitDate=[todaysDate,lvd,lvd1,lvd2,lvd3,lvd4,lvd5,lvd6]
firstVisitDate=[lvd6]

walkin=["Y","N"]
randclinicName=["well Medica","shopppers drug mart","Unity pharmacy","Rexall","Pharmasave"]
randclinicCity=["Brampton","Oakville","Mississauga"]
randclinicprov_state=["ON"]
randinsurnacePolicyNumber=["","1245CNRB3456","23333","45677"]
insuranceAmountBilled=["0","400","300"]
cashAmountBilled=["0","348","90"]
randmiscValuePipeSeperated=[ "DistanceFromPostcodeinKM:10","DistanceFromPostcodeinKM:11","DistanceFromPostcodeinKM:15","DistanceFromPostcodeinKM:20"] # from post code for brampton wellmedica
#L6W0A7
#db.customters.find({$or:[{condtionname1:"value"},{condutiona2:"value2"}])
#db.customters.find({$age:{$lt:40}});



def generateFirstName():
    return random.choice(randFirstNameList)
def generateLastName():
    return random.choice(randLastNameList)
def generatePersonCityList():
    return random.choice(randPersonCityList)
def generatePostCode():
    postCode1=random.choice(randPostCodefirst)        
    postCode2=random.choice(randPostCodeSecond)        
    postCode3=random.choice(randPostCodethird)
    postCode4=random.choice(randPostCodefour)
    postCode5=random.choice(randPostCodefive)
    postCode6=random.choice(randPostCodesix)
    return postCode1+postCode2+postCode3+postCode4+postCode5+postCode6
def generateRandProvCode():
    return random.choice(randProvState)
def generateAutoInc():
    return str(autoinc+1)
def generateRandDOB():
    return str(random.choice(randdobDate))
def generateRandGen():
    return random.choice(randomgender)
def generateRandTel():
    return random.choice(randtelnumber)
def generateRandEmail():
    return random.choice(randemail)
def generateRandLVD():
    return str(random.choice(lastVisitDate))    
def generateRandFVD():
    return str(random.choice(firstVisitDate)) 
def generateWalkin():
    return random.choice(walkin)
def generaterandclinicName():            
    return random.choice(randclinicName)            
def generaterandclinicCity():            
    return str(random.choice(randclinicCity))            
def generaterandclinicprov_state():      
    return random.choice(randclinicprov_state)    
def generaterandinsurnacePolicyNumber(): 
    return random.choice(randinsurnacePolicyNumber)
def generateinsuranceAmountBilled():     
    return random.choice(insuranceAmountBilled)    
def generatecashAmountBilled():          
    return random.choice(cashAmountBilled)         
def generaterandmiscValuePipeSeperated():
    strr=random.choice(randmiscValuePipeSeperated)
    strrr=strr.split(':')
    return str(strrr[1])

serveraccessstr="localhost:8080/create?"



for i in range(10):
     #print (">>>>>>>>>")
     randGender=generateRandGen()
     randVal=generaterandmiscValuePipeSeperated()
     randVal="DistanceFromPostcodeinKM:"+randVal #DFP distance from postcode
     #print (type(randGender))
     #print (type(randVal))
     print (serveraccessstr+
            "firstName="+ generateFirstName() +
             "&lastName=" + generateLastName() 
            +"&personCity="+                    generatePersonCityList()
            +"&personprov_state="+              generatePostCode()
            +"&personzip_postcode="+            generateRandProvCode()
            +"&recNum="+                        generateAutoInc()
            +"&dobDate="+                       generateRandDOB()
            +"&gender="+                        randGender
            +"&telnumber="+                     generateRandTel()
            +"&email="+                         generateRandEmail()
            +"&lastVisitDate="+                 generateRandLVD()
            +"&firstVisitDate="+                generateRandFVD()
            +"&walkin="+                        generateWalkin()
            +"&clinicName="+                    generaterandclinicName()            
            +"&clinicCity="+                    generaterandclinicCity() 
            +"&clinicprov_state="+              generaterandclinicprov_state()
            +"&cliniczip_postcode="+            generatePostCode()
            +"&insurnacePolicyNumber="+         generaterandinsurnacePolicyNumber()
            +"&insuranceAmountBilled="+         generateinsuranceAmountBilled()     
            +"&cashAmountBilled="+              generatecashAmountBilled()         
            +"&miscValuePipeSeperated="+randVal)


@app.route('/')
def IndexPage():
     return "voyager is Hellbent on blowing past the HelioSphere|" + str(datetime.datetime.now())
     #return render_template('index.html')


