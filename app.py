# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, make_response
import json
import requests
import regex

#file html must save in 'templates' folder

app = Flask(__name__)

@app.route('/')
def index():
    print('REQUEST OK')
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    #res = makeWebhookResult(req)
    #res = json.dumps(res, indent=4)
    res = req.get("queryResult").get("action")
    print(res)
    #r = make_response(res)
    #r.headers['Content-Type'] = 'application/json'
    #return r
    return

def makeWebhookResult(req):
    if req.get("result").get("action") != "get-stock-name" :
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    name = parameters.get("stock-name")
    #will put stock api result here
    stock = {'PTT':'I am PTT','SET':'SET is here' }
    speech =  "The Stock price of" + name + " is " + str(stock[name])
    print("Response: ")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "StockPrice"
    }

@app.route('/dialogflow', methods=['POST'])
def dialogflow():
    msg_in_json = requests.get_json()
    msg_in_str = json.dumps(msg_in_json)
    return 'OK', 200

def reply(text):
    Dialogflow_API = 'https://api.dialogflow.com/v1/query?v=20150910'
    headers = {
        'Authorization': DIALOGFLOW_API_KEY,
        'Content-Type': 'application/json'
        }
    body = json.dumps({
        "contexts": some_list_of_context,
        "lang": "th",
        "query": msgs,
        "sessionId": "12345",
        "timezone": "Asia/Bangkok"
        })
    msgs = 'hello'
    requests.post(Dialogflow_API,headers=headers, data=body)
    return


if __name__ == '__main__':
    app.run(debug=True)
