from my_module.functions import end_chat, selector, rate_happiness, rate_response, ucsd_feelings_chat
def test_rate_happiness():
    message == "1"
    assert rate in ['Aw, I\'m so sorry to hear that. Would you like some help?', 'Im so sorry to hear that, would you like me to point you to some resources?']
    
def test_rate_response():
    assert rate_response() == None
    assert callable(rate_response)
    assert isinstance(rate_response(0), str)
    

def test_ucsd_feelings_chat(): 
    assert callable(ucsd_feelings_chat)
    assert ['Hello Triton! Do you wanna talk about your feelings, yes or no?'] in output
    