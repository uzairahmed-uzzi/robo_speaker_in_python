import os
import pyttsx3

if __name__ == '__main__':
    engine=pyttsx3.init()
    
    print("Welcome to Robo Speaker version 0.1...")
    while True:    
        x=input("give what do want me to speak: ",);
        engine.say(x)
        engine.runAndWait()
        operation=input("press q to exit: ");
        if operation.lower()=='q':
            break