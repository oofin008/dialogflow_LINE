# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, make_response
import json
import requests
import regex
from oil_price_api import ptt_result_API
#file html must save in 'templates' folder
oil_price = ptt_result_API()

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
    if req.get("result").get("actionIncomplete") == True :
        return {}
    res = makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "get-stock-name" :
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    name = parameters.get("stock-name")
    #will put stock api result here
    stock = {'PTT':oil_price,'SET':'SET is here' }
    speech =  "The Stock price of " + name + " is " + str(stock[name])
    print("Response: ")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "StockPrice"
    }


if __name__ == '__main__':
    app.run(debug=True)
