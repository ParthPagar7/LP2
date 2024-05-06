import random

# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking!"],
    "what is your name": ["I'm just a humble chatbot!", "I'm ChatBot, nice to meet you!"],
    "who created you": ["I was created by OpenAI.", "My creator is a team of talented developers ."],
    "default": ["I'm sorry, I didn't understand that.", "Could you please repeat that?", "I'm not sure what you mean."]
}


# Define states for the chatbot
class ChatState:
    INIT = 0
    CONVERSATION = 1


def chatbot_response(message, state):
    """
    Generate a response from the chatbot based on the user's message and the current state.
    """
    message = message.lower()

    if state == ChatState.INIT:
        return random.choice(responses["hi"]), ChatState.CONVERSATION
    elif state == ChatState.CONVERSATION:
        if "bye" in message:
            return random.choice(responses["bye"]), ChatState.INIT
        else:
            for key in responses:
                if key in message:
                    return random.choice(responses[key]), ChatState.CONVERSATION
            return random.choice(responses["default"]), ChatState.CONVERSATION


def main():
    print("Welcome to the ChatBot!")
    state = ChatState.INIT

    while True:
        user_input = input("You: ")
        response, state = chatbot_response(user_input, state)
        print("ChatBot:", response)
        if state == ChatState.INIT:
            break


if __name__ == "__main__":
    main()
