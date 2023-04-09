import random

# Define the responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hi! How can I help you?"],
    "how are you": ["I'm doing well, thank you for asking!", "I'm good, how about you?"],
    "what's your name": ["My name is Chatbot!", "I'm Chatbot, nice to meet you!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

# Define the function to handle user input and generate responses
def chatbot_response(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return "I'm sorry, I don't understand. Could you please rephrase that?"

# Start the chatbot
print("Welcome to the chatbot! Ask me a question or say hi.")
while True:
    user_input = input("> ")
    if user_input.lower() == "bye":
        print(chatbot_response(user_input))
        break
    else:
        print(chatbot_response(user_input))
