
# Name: Emlyn Witherspoon
# Date: October 26, 2026
# Week 1 Project: Hello AI World

import datetime

print("Hello! I am a simple AI reflex agent.")
print("AI Fact 1: AI can help doctors detect diseases.")
print("AI Fact 2: AI is used in Siri and Alexa.")

name = input("What is your name? ")
mood = input("How are you feeling today? ").lower()

if "happy" in mood:
    print("That's great! Keep smiling!")
elif "sad" in mood:
    print("I'm sorry you're feeling sad. Hope things get better!")
elif "tired" in mood:
    print("You sound tired. Take a break and get some rest!")
else:
    print("Thank you for sharing how you feel!")

hour = datetime.datetime.now().hour

if hour < 12:
    greeting = "Good morning"
elif hour < 17:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print(greeting + ", " + name + "!")
print("Thanks for chatting with me!")