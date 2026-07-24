def chatbot():
    print("===================================")
    print("     Welcome to Basic Chatbot")
    print("Type 'bye' to exit")
    print("===================================")

    while True:
        user = input("\nYou: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hello! How are you?")
        elif user == "how are you":
            print("Bot: I am fine. Thank you!")
        elif user == "what is your name":
            print("Bot: My name is CodeAlpha Bot.")
        elif user == "who created you":
            print("Bot: I was created using Python.")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()