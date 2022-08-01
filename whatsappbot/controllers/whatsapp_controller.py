#import http
import json
import os
import requests
import time
import urllib.request
import urllib.parse
import urllib.error

#create class to access the whatsapp api
class WhatsappController:
    #constructor
    def __init__(self):
        self.url = "https://api.whatsapp.com/v1/messages"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + os.environ['WHATSAPP_TOKEN']
        }
        self.data = {
            "to": os.environ['WHATSAPP_TO'],
            "type": "text",
            "text": "Hello World!"
        }
        self.response = requests.post(self.url, headers=self.headers, data=json.dumps(self.data))
        self.response_json = self.response.json()
        self.message_id = self.response_json['message_id']
        self.message_status = self.response_json['status']
       
    #method to send message
    def send_message(self):
        self.response = requests.post(self.url, headers=self.headers, data=json.dumps(self.data))
        self.response_json = self.response.json()
        self.message_id = self.response_json['message_id']
        self.message_status = self.response_json['status']
        return self.message_id, self.message_status