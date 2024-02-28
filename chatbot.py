def chatbot():
    print("Hello! I'm a simple chatbot. Let's have a conversation:))")
    
    conversation_history = []
    questions_asked = 0
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "quit":
            print("Bye!")
            break
        else:
            try:
                response = get_response(user_input, conversation_history)
                conversation_history.append((user_input, response))
                print("Chatbot:", response)
                if response == "Bye! Have a great day!" and questions_asked >= 2:
                    break
                elif response == "Bye! Have a great day!" and questions_asked < 2:
                    print("Chatbot: It seems like you haven't asked enough questions. Let's continue.")
                else:
                    questions_asked += 1
            except Exception as e:
                print("An error occurred:", e)

def get_response(user_input, conversation_history):
    responses = {
        "hey": "Hello!",
        "how are you?": "I'm good, I am here to help you!",
        "what's your name?": "You can call me Simple Chatbot.",
        "what can you do?": "I can only have simple conversation!",
        "bye": "Bye! Have a great day!"
    }
    
    for input_text, output_text in reversed(conversation_history):
        if user_input == input_text:
            return f"You've already asked me '{user_input}' and I responded '{output_text}'."
    
    response = responses.get(user_input)
    if response is None:
        raise ValueError("I can't respond to that")
    
    return response
    
if __name__ == "__main__":
    chatbot()