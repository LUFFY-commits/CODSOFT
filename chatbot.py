
def chatbot():
    print("Hello! I'm your simple chatbot. How can I assist you today?")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("\nYou: ").strip().lower()
        
        
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! How can I help you?")
        elif user_input == "how are you?":
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather right now, but you can try using a weather app!")
        elif "your name" in user_input:
            print("Chatbot: I am a simple chatbot created to assist you.")
        elif "time" in user_input:
            from datetime import datetime
            print(f"Chatbot: The current time is {datetime.now().strftime('%H:%M:%S')}.")
        elif user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you please rephrase?")
            
# Run the chatbot
chatbot()

