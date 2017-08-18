#! python3

# Chapter 16 Project Just Text Me Module
# Defines the textmyself() function that texts a message passed to it
# as a string.

from twilio.rest import TwilioRestClient

accountSID = 'ACxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+15558675309'
twilioNumber = '+15558675309'

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
