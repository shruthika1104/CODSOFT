print("Hi! I'm CODBOT. How can I help you today?")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("CODBOT: Hello! How are you today?")
    elif "help" in user_input:
        print("CODBOT: Sure! Tell me what you need help with.")
    elif "your name" in user_input:
        print("CODBOT: I'm CODBOT, your virtual assistant!")
    elif "bye" in user_input or "exit" in user_input:
        print("CODBOT: Goodbye! Have a nice day!")
        break
    else:
        print("CODBOT: I'm not sure how to respond to that.")
