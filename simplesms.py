# Create a django application that sends SMS text messages using the Twilio Python API
#
# Create a webpage with a form prompting the user for a phone number and a message body.
#
# POST the users data to your django application and inside the view, read from the POST dictionary,
# and send the message via the Twiio API.
#
# https://www.twilio.com/docs/quickstart/python/sms
#
# Respond to the browser with a success message and display it to the user.
#
# Be sure to make a new virtualenv and git repository for your project.
#
# Here are thw Twilio Keys:
#
# Token: 4626c66ff2e18445ca7ef5a38fd141b1
# SID: ACa6626c00b99aa57af0a035719b24da89
#
# Here is an example of a call to twilio.
#
# from twilio.rest import TwilioRestClient
#
# account_sid = "ACa6626c00b99aa57af0a035719b24da89"
# auth_token = "4626c66ff2e18445ca7ef5a38fd141b1"
# client = TwilioRestClient(account_sid, auth_token)
# number = []
#
# #numbers = ['+18456331959','+19714099425', '+13606245615', '+15037063889', '+15037810745', '+19712371510', '+15037379611']
# day_numbers = ['+18067860264','+19713209937', '+15039808649', '+15038884575', '+19724153532', '+19724156381']
#
# for number in day_numbers:
#     message = client.messages.create(to=number, from_="+14243512633", body="Look Up!")
#     print("Sent to {}".format(number))
#
# ### Advanced
#
# Handle any number of individual messages and phone numbers on the webpage.
# Parse the response in the view, and send all messages to thier respective recipients.
#
# ### Super Advanced
#
# Make a django "SMSMessage" Model, and keep a history of the messages sent.
# Using built in Django Auth, allow uers to sign in and view a history of thier messaging.
# import requests
# from twilio.rest import TwilioRestClient
def display_message():
    print("=============================")
    print("****   Simple SMS   ****")
    print("=============================")
    print("****MESSAGE TO TWILIO****")
    print("=============================")
    print("****   Simple SMS   ****")
    print("=============================")
display_message()

from twilio.rest import Client

account_sid = "ACa6626c00b99aa57af0a035719b24da89"
auth_token = "4626c66ff2e18445ca7ef5a38fd141b1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Fuck this shit", to='+14049179455', from_='+14049945296')

print(message.sid)
