# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import json
import requests
import regex

#file html must save in 'templates' folder

app = Flask(__name__)

@app.route('/')
def index():
    #print('REQUEST OK')
    #return render_template('index.html')
    return 'hello'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4)


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
