
import sys
import os
from flask import Flask, request
from Auth import verify_token
from flask_cors import CORS
from bot import bot
from pymongo import MongoClient
from bson.json_util import dumps
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './')))


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

MONGODB_URL = "mongodb+srv://mukeshpilane:123mukesh@cluster0.83vr0ru.mongodb.net/?retryWrites=true&w=majority" or "mongodb://localhost:27017"
client = MongoClient(MONGODB_URL)
db = client["chatbot"]
# cursor = mysql.connection.cursor()

@app.route("/verify", methods = ['GET', 'POST', 'DELETE'])      
@verify_token
def googleSigin(userData):
    user_collection = db['users']
    user = user_collection.find_one({"userId": userData.get('sub')})  
    if user is None:
        user_collection.insert_one({"userId": userData.get('sub')})
    return {"uinfo": userData}


@app.route("/messages", methods = ['GET', 'POST', 'DELETE'])     
@verify_token 
def Botresponse(userData):
     token = request.headers.get('Authorization')
     uinfo = userData
     message_collection = db['messages']
     uid = userData.get('sub')
     if(request.method == 'POST'):
               content_type = request.headers.get('Content-Type')
               if (content_type == 'application/json'):
                    data = request.json
                    botResponse = bot(data["message"])
                    message_collection.insert_one({"userId":uid,"message": data["message"], "botResponse":botResponse})
                    return botResponse
               else:
                    return 'Content-Type not supported!'
     if(request.method == 'GET'):
          data = message_collection.find({"userId":uid})
          return dumps(data), 200
          
    



               
if __name__=="__main__":
    app.run(debug=True)