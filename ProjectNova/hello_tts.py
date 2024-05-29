import pyttsx3
import sys
import os

def say_hello(name):
    engine = pyttsx3.init()
    engine.say(f"Hello {name}, I see you")
    engine.runAndWait()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(f"name provided : {name}")
        say_hello(name)
    else:
        print("No name provided")
