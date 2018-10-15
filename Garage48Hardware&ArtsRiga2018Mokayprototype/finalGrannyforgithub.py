#!/usr/bin/python
###@Project for Garage48 Hardware & Arts Riga 2018. Mokay team. 


import RPi.GPIO as GPIO
import time
import nexmo
#import twilio
import requests

GPIO.setmode(GPIO.BCM)
chanA_list = [4,18,17]
client = nexmo.Client(key='test', secret='test')
GPIO.setup(chanA_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(04, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class SMSsender:

    def __init__(self):
        pass
    
    def sendingOutMessage(self, flag):
        if flag == "Green":
            message = 'I am good. Do not worry, be happy'
        elif flag == "Yellow":
            message = 'Please call me, I need to talk'
        elif flag == "Red":
            message = 'I need help, right now!!! Emergency'
   
        ##response = client.send_message({'from': 'num', 'to': 'num', 'text': 'Screw You'})
        response = client.send_message({'from': 'NEXMO', 'to': 'num', 'text': message})
        
        response = response['messages'][0]
        
        if response['status'] == '0':
            print( 'Sent message', response['message-id'])
            print ('Remaining balance is', response['remaining-balance'])
            ##write over here website post
        else:
            print ('Error:', response['error-text'])

class CallMaker:

    def __init__(self):
        pass

    def makingAPhoneCall(self):
        print("ooh")
        response = client.create_call({
            'to': [{'type': 'phone', 'number': 'num'}],
            'from': {'type': 'phone', 'number': 'NEXMO'},
            'answer_url': ['https://nexmo-community.github.io/ncco-examples/first_call_talk.json']})         

s = SMSsender()

#c = CallMaker()

#create an file called button.txt
#
#
while True:
    input_state_green=GPIO.input(4) 
    input_state_yellow=GPIO.input(18) 
    input_state_red=GPIO.input(17) 
    if(input_state_green==0):        #print(input_state_green)
        print("Green")
        #makingAPhoneCall()
        #sendingOutMessage()
        #s.sendingOutMessage("Green")
        time.sleep(1)
        #req = requests.get('http://test.developerforwebsites.com/button.php/')
        
    elif(input_state_yellow==0):
        #print(input_state_yellow)
        print("Yellow")
        #makingAPhoneCall()
        s.sendingOutMessage("Yellow")
        #sendingRequestToWebsite():
        req = requests.get('http://test.developerforwebsites.com/yes.php/')
        time.sleep(1)
        
        
    elif(input_state_red==0):
        #print(input_state_red)
        print("Red")
        s.sendingOutMessage("Red")
        #c.makingAPhoneCall()
        req = requests.get('http://test.developerforwebsites.com/button.php/')
        time.sleep(1)
    else:
        print("no button is pressed")
        time.sleep(0.3)
        
##Welcome@RTU
