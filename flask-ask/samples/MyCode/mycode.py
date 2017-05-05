import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

a = 0
b = 0
c = 0 
d = 0 


@ask.launch
def launch():
    speech_text = 'Welcome to the Alexa Coding, you can start saying your program now!'
    return question(speech_text).reprompt(speech_text).simple_card('MyCode', speech_text)


@ask.intent('AssignIntent', convert={'Variable':str, 'Value':int})
def assign(Variable, Value):
    speech_text = 'ok! ' + Variable + ' is assigned to ' + str(Value)
    exec("global "+ Variable)    
    exec(Variable + " = " + str(Value)) 
    print a 
    access()
    return question(speech_text).reprompt(speech_text).simple_card('MyCode', speech_text)

def access():
  	print "%d" % a 

@ask.intent('PrintIntent', convert={'Variable':str})
def print_variable(Variable): 
    exec ("temp=" + Variable )
    speech_text = Variable + " is " + str(temp) 
    print a 
    return question(speech_text).reprompt(speech_text).simple_card('MyCode', speech_text) 

@ask.intent('SaveAndCloseIntent', convert={'FileName':str})
def save_and_close(FileName):
	speech_text("save the program in the file") 
	return question(speech_text).reprompt(speech_text).simple_card('MyCode', speech_text)

@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say a statement!'
    return question(speech_text).reprompt(speech_text).simple_card('MyCode', speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
