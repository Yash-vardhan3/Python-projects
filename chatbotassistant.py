import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ["I'm good, thank you!", "I'm doing well, thanks for asking!"]),
    (r'what is your name?', ["I'm a chatbot created with NLTK!", "You can call me Chatbot."]),
    (r'(.*) your name(.*)', ["You can call me Chatbot.", "I'm a chatbot created with NLTK!"]),
    (r'(.*) (love|like) (you|me)', ["I'm just a chatbot, but I appreciate the sentiment!"]),
    (r'(.*) (weather|forecast)(.*)', ['Sorry, I am not programmed to check the weather.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
    (r'what can you do\?', ["I can answer your questions, engage in conversation, and provide information."]),
    (r'(.*) (age|old) (are|you)', ["I don't have an age as I'm just a program.", "I'm ageless!"]),
    (r'(.*) (thank you|thanks)(.*)', ["You're welcome!", "No problem.", "My pleasure!"]),
    (r'(.*) (help|assistance)(.*)', ["Sure, how can I assist you?", "I'm here to help!"]),
    (r'how (can|do) I contact you\?', ["You can reach out to my developer for assistance."]),
    # Add more patterns and responses here...
    # Additional patterns for common questions
    (r'what (can|do) you know\?', ["I have knowledge about various topics such as technology, science, and entertainment."]),
    (r'(.*) (good|great)(.*)', ["I'm glad to hear that!", "That's fantastic!"]),
    (r'(.*) (bad|not good)(.*)', ["I'm sorry to hear that. How can I help you feel better?"]),
    (r'(.*) (sad|upset)(.*)', ["I'm sorry to hear that. Would you like to talk about it?"]),
    (r'(.*) (funny|joke)(.*)', ["Sure! Why couldn't the bicycle stand up by itself? Because it was two-tired!"]),
    (r'(.*) (music|song)(.*)', ["Music is great for relaxation and inspiration. Do you have a favorite genre?"]),
    (r'(.*) (movie|film)(.*)', ["Movies are a fantastic form of entertainment. Do you have a favorite genre or movie?"]),
    (r'(.*) (book|novel)(.*)', ["Books can take you on amazing adventures. Do you have a favorite book or author?"]),
    (r'(.*) (food|eat)(.*)', ["Food is one of life's pleasures. What's your favorite cuisine?"]),
    (r'(.*) (game|play)(.*)', ["Games are a fun way to pass the time. Do you have a favorite game?"]),
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Welcome to the NLTK Chatbot. Type 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot:", chatbot.respond(user_input))