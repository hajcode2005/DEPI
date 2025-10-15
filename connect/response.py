def get_response(user_input):
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
        

    return random.choice(responses["default"]) 
def chatbot():
    print("chatbot :hi how can i help you")
    