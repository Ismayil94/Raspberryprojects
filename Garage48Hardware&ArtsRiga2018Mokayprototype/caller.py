from twilio.rest import TwilioRestClient

PHONE_NUMBER = 't'

DIAL_NUMBERS = 't'

TWIML_INSTRUCTIONS_URL = 'http//static.fullstackpython.com/phone-calls-python.xml'

ALT_URL = 'http://demo.twilio.com/docs/voice.xml'

client = TwilioRestClient('nn', 'nn')

def dial_numbers(numbers_list):

    print('Diaglog ' + DIAL_NUMBERS)
    
    print('from_ ' + PHONE_NUMBER)
    
    print('url ' + TWIML_INSTRUCTIONS_URL)
    
    print('method ' + DIAL_NUMBERS)
    
    client.calls.create(to=DIAL_NUMBERS, from_=PHONE_NUMBER, url=ALT_URL, method='GET')

if __name__ == '__main__':
    dial_numbers(DIAL_NUMBERS)
