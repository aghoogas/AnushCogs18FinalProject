import string
import random
import nltk

"""copied fom A3"""
def end_chat(input_list):
    output = False 
    if 'quit' in input_list:
        return True
    return output

"""copied from A3"""
def selector(input_list,check_list,return_list):
    output = None
    for elt in input_list:
        if elt in check_list:
            output = random.choice(return_list)
            break
    return output
GREETINGS_INPUT = ['hi','hello']
GREETINGS_OUTPUT = ['Hi there!', 'Hello, stranger!', 'Hello!']
YES_LIST= [ 'yes', 'ya', 'sure', 'ok', 'yea' , 'yep', 'yup', 'YAAAAAS','totally','totes','sure', 'you bet', 'yeah', 'yes please']


def rate_happiness(message):
    """Takes happiness rate and returns appropriate response question, based on how happy they are."""
    sad_rate = ['Aw, I\'m so sorry to hear that. Would you like some help?', 
                'Im so sorry to hear that, would you like me to point you to some resources?'] 
    neutral_rate = ['Alright, not bad! Do you wanna see a resource that could help improve your quality of life?' , 
                    'Im glad to see youre doing okay, do you wanna know how to potentially be happier overall?']
    happy_rate = ['yay, do u wanna see something cute',
                  'haha, can i show u something cute?']
    
    rate = 'ok'
  
    if '0' == message or '1' == message or '2' == message or '3' == message or '4' == message:
        rate = random.choice(sad_rate)
    elif '5' == message or '6' == message or '7' == message or '8' == message:
        rate = random.choice(neutral_rate)
    elif '9' == message or '10' == message:
        rate = random.choice(happy_rate) 
    return rate, message


def rate_response(rate, message):
    """If they say yes to question from rate_happiness, returns appropriate UCSD resource based on how happy they are."""
    print('OUTPUT:', rate)
    want_help = input('INPUT:\t')
    yes_bool = False
    for yes_elt in YES_LIST: 
        """Checks if input is in YES_LIST to see if resource should be returned."""
        if want_help == yes_elt: 
            yes_bool = True
            break
   
    if '0' == message:
        if yes_bool==True:
            return 'Call this number for UCSD\'s Crisis Hotline. Stay strong! 858-534-3755'
        else:
            return 'Okay, consider calling 858-534-3755 if you want to talk later. Have a beautiful day!'
    if '1'  == message or '2' == message or '3' == message or '4' == message:
        if yes_bool==True:
            return 'Click this link! https://wellness.ucsd.edu/CAPS/Pages/default.aspx'
        else:
            return 'Alright, well I hope things start to look up for you!'
    elif '5' == message or '6' == message or '7' == message or '8' == message:
        if yes_bool==True:
            return 'Click this link! https://wellness.ucsd.edu/zone/Pages/default.aspx'
        else:
            return 'Okay, well I hope you have a wonderful day!'
    elif '9' == message or '10' == message:
        if yes_bool==True:
            return 'Click this link! https://gph.is/2ycyxlO'
        else:
            return 'Okay byyyyyyye!'
    return 'I didn\'t quite get that. Could you give me a number 0 through 10?' 


"""Some code is from A3"""
def ucsd_feelings_chat():
    
    chat = True
    help_given = False
    while chat:

        """Get a message from the user. Code from A3"""
        message = input('INPUT :\t').lower()
        out_message = None


        if end_chat(message):
            """Checks for an end msg. Code from A3"""
            out_message = 'Bye!'
            chat = False
            
        if not out_message:
            """Asks UCSD Student if they would like to talk about their feelings"""
            output = []
            output.append(selector(message, GREETINGS_INPUT, GREETINGS_OUTPUT))
            output = ['Hello Triton! Do you wanna talk about your feelings, yes or no?']
            """Checks if response to previous question is in YES_LIST, to see if bot should ask next question."""
            yes_bool = False
            for yes_elt in YES_LIST: 
                if message == yes_elt: 
                    yes_bool = True
                    break
                    
            if yes_bool == True:
                """Asks UCSD Student to rate how happy they are on a scale from 0-10"""
                rate_msg = 'On a scale from 0 to 10, how happy are you? 0 is the saddest, 10 is the happiest.' 
                print('OUTPUT:', rate_msg) 
                
                validNum = False
                while not validNum:
                    """Checks if response to previous question is valid. If not, asks for input again."""
                    message = input('INPUT:\t')
                    NUM_LIST = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                    for num in NUM_LIST:
                        if message == num: 
                            validNum = True
                            break
                    if not validNum:
                        print('OUTPUT: I didn\'t quite get that. Could you give me a number 0 through 10?')
                        
                rate = rate_happiness(message)
                resource = rate_response(rate[0], rate[1])
                print('OUTPUT:', resource)
                help_given = True
                break
                
            elif message =='no':
                """Returns output if student doesn't want to talk about feelings"""
                chat = False
                output = ['Okay, sorry I couldn\'t help you. Have a nice day!']
        
            options = list(filter(None, output))
            if options:
                out_message = random.choice(options)
        if not help_given:
            print('OUTPUT:', out_message)