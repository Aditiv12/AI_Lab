#chatbot
def chatbot():
    print("Hello! I'm a chatbot. How can I assist you? /t Type exit if you want to stop the chatbot")
    while True:
        user_input = input("You: ").lower()
        if user_input in ['hello', 'hi', 'hey']:
            print("Chatbot: Hi there!")
        elif user_input == "how are you?":
            print("Chatbot:I'm just a program, so I dont have feelings but thank you asking")
        elif user_input == "what is your name?":
            print("Chatbot:I'm a chatbot")
        elif "weather" in user_input:
            print("Chatbot:I'm sorry, I'm not equipped to provide weather updates")
        elif user_input == "bye":
            print("Chatbot: Bye! Have a good day.")
        elif user_input == "exit":
            print("Chatbot: Goodbye")
            break
        else:
            print("Chatbot: I'm sorry. I didn't understand that")

chatbot()
