from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Create a new chatbot
# Create a new chatbot
chatbot = ChatBot('ProgrammingBot')
custom_data = [
    ("What is Python?", "Python is a high-level programming language known for its simplicity and readability."),
    ("What are the features of Python?", "Python has a simple syntax, dynamic typing, and high-level data structures."),
    ("What is JavaScript?", "JavaScript is a scripting language commonly used for web development."),
    ("What are the features of JavaScript?", "JavaScript is used to add interactivity to web pages and can be run on the client side."),
    ("What is Java?", "Java is a high-level, class-based, object-oriented programming language."),
    ("What are the features of Java?", "Java is platform-independent, has a large standard library, and is used for building enterprise applications."),
]
# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)
# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot on the custom dataset
trainer.train(custom_data)
print("Hello, I'm ProgrammingBot. Ask me about programming languages or type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot.get_response(user_input)
    print("ProgrammingBot:", response)