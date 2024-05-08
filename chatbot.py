#chatbot 
import random
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm good, thank you!", "Doing well, thanks!", "I'm fine, how about you?"],
    "what's your name?": ["I'm a chatbot.", "You can call me Chatbot.", "I'm your friendly chatbot!"],
    "bye": ["Goodbye!", "Bye bye!", "See you later!"],
    "default": ["I'm sorry, I don't understand.", "Could you please repeat that?", "I'm not sure what you mean."]
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    response = responses.get(user_input, responses["default"])
    return random.choice(response)

# Main loop
print("Chatbot: Hi! I'm Chatbot. How can I help you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
