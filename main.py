from datetime import datetime

print("=" * 50)
print("🤖 Welcome to Rule-Based AI Chatbot")
print("=" * 50)

name = input("Enter your name: ").strip().title()

hour = datetime.now().hour

if hour < 12:
    greeting = "Good Morning"
elif hour < 17:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

print(f"\n{greeting}, {name}! 😊")
print("Type 'help' to see available commands.")
print("Type 'bye' anytime to exit.\n")

while True:
    user = input("You: ").strip().lower()

    if user in ["hi", "hello", "hey"]:
        print(f"Bot: Hello {name}! How can I help you today?")

    elif user == "how are you":
        print("Bot: I am fine and always ready to help!")

    elif user == "your name":
        print("Bot: My name is RuleBot.")

    elif user == "my name":
        print(f"Bot: Your name is {name}.")

    elif user == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif user == "time":
        print("Bot:", datetime.now().strftime("%I:%M:%S %p"))

    elif user == "day":
        print("Bot:", datetime.now().strftime("%A"))

    elif user == "ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "python":
        print("Bot: Python is an easy and powerful programming language.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "help":
        print("""
Available Commands:
 hi
 hello
 heyh
how are you
 your name
 my name
 date
time
 day
ai
 python
 thank you
 help
 bye
 exit
 quit
""")

    elif user in ["bye", "exit", "quit"]:
        print(f"Bot: Goodbye {name}! Have a wonderful day. ")
        break

    else:
        print("Bot: Sorry! I don't understand that command.")