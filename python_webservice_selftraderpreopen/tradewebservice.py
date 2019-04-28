from flask import Flask, jsonify,make_response,request,render_template
from flask_httpauth import HTTPBasicAuth
import datetime
#import trade
import random

auth = HTTPBasicAuth()








app = Flask(__name__)
sVERSION='v01'

class trade():
    def __init__(self,id,title,description,done):
        self.id=id
        self.title=title
        self.description=description
        self.done=True
    def printall(self):
        print (self.__dict__)
        


trades = [
    {
        'id': 1,
        'title': u'indexswap',
        'description': u'USDvsLIBOR', 
        'done': False
    },
    {
        'id': 2,
        'title': u'EuroDollarFuture',
        'description': u'ETD', 
        'done': True
    }
]

@app.route('/')
def IndexPage():
#    return "voyager is Hellbent on blowing past the HelioSphere|" + str(datetime.datetime.now())
     return render_template('index.html')


@app.route('/showSignUp')
def showSignUpPage():
#    return "voyager is Hellbent on blowing past the HelioSphere|" + str(datetime.datetime.now())
     return render_template('signup.html')

def listTradesNew():
   #return str(datetime.datetime.now()) + " | " + jsonify({'trades':trades})
   trade1 = trade(random.randint(10,99),"USDLIBOR","IndexBasisSwapOTC",True)
   trade2 = trade(random.randint(10,99),"USDLIBOR","IndexBasisSwapOTC",True)
   trade1.printall
   trade2.printall


@app.route("/trade/api/sVERSION/trades",methods =['GET'])
def listTrades():
    #return str(datetime.datetime.now()) + " | " + jsonify({'trades':trades})
    return jsonify({'trades':trades})

"""
@app.route("/trade/api/sVERSION/trades/<int:trade_id>",methods =['GET'])
def getTradeId(trade_id):
    tradeid=[trade for trade in trades if trade['id'] == trade_id]
    if len(tradeid) == 0:
       abort(404)
    return jsonify({'trades':trade1[0]})
"""  
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'not found'}),404)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
