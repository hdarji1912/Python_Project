# Personal Chat Assitant

import datetime
import time
name = input("Enter your name: ")
presentHour = datetime.datetime.now().hour
if 5<= presentHour <= 11:
     print("Good morning,",name)
elif 11<= presentHour <= 17:
     print("Good afternoon,",name)
elif 17<= presentHour <= 20:
     print("Good evening,",name)
else:
     print("Good night")
     

print("Namaste! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

# Chatbot Memory Creation 

responses = {
    "hi": "hi i am chatbot i will help you",
    "hello": "Hi, welcome, How can I help you?",
    "how are you": "I am very fine, Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug in your project makes you a better developer",
    "happy": "Great to hear that!",
    "sad": "Don't worry, better days are coming",
    "good morning": "Good Morning! Have a productive day",
    "good afternoon": "Good Afternoon! Keep learning",
    "good evening": "Good Evening! How was your day?",
    "good night": "Good Night! Sweet dreams",
    "thanks": "You're welcome!",
    "thank you": "My pleasure",
    "bye": "Goodbye! See you again",
    "study": "Consistency is the key to success",
    "exam": "Stay calm and revise important topics",
    "java": "Java follows Object Oriented Programming concepts",
    "project": "Projects help improve your practical skills",
    "sing a song": "La la la... I am better at coding than singing!",
    "are you human": "No, I am a chatbot powered by code.",
    "tell me a joke": "Why did the Python programmer wear glasses? Because they couldn't C.",
    "who is your creator": "I was created by talented developers.",
    "do you like pizza": "I don't eat, but pizza sounds popular!",
    "are you smart": "I try my best to be helpful and smart.",
    "can you dance": "Only if dancing means executing algorithms.",
    "what is love": "Love is care, trust, and understanding.",
    "tell me a riddle": "What has keys but can't open locks? A keyboard.",
    "surprise me": "You are capable of more than you think.",
    "success": "Success comes from hard work and patience",
    "failure": "Failure is a stepping stone to success",
    "friend": "A good friend is a treasure",
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "weather": "I cannot check live weather right now",
    "goal": "Set small goals and achieve them one by one",
    "time": "Please check your system clock",
    "college": "Study regularly and attend practical sessions",
    "ssc mts": "Practice mock tests and previous year papers daily",
    "motivation": "Believe in yourself and keep moving forward",
    "coding": "The more you code, the better you become",
    "error": "Every error teaches something new",
    "ai": "Artificial Intelligence helps machines learn and think",
    "machine learning": "Machine Learning is a branch of AI",
    "data science": "Data Science extracts insights from data",
    "book": "Reading books improves knowledge",
    "food": "Healthy food keeps your mind active",
    "sports": "Sports keep the body fit and healthy",
    "dream": "Dream big and work hard",
    "hard work": "Hard work always pays off",
    "confidence": "Confidence comes from preparation",
    "teacher": "Teachers guide us toward success",
    "family": "Family is our biggest support system",
    "life": "Life is a journey of learning and growth"}

# Function  to get response of chatbot

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    
    return "I am not able to tell that yet. I am learn it soon"

# Take use input

while True:
    userinput = input("please ask your question :")
    reply = getResponseOfBot(userinput)
    print("Bot Response :",reply)

    if "bye" in userinput.lower():
           break
     