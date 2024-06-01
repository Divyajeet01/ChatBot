import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
from googlesearch import search
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

reply = ['hello sir', 'welcome back sir', 'hi, how may I help you', 'good to see you again sir']
reply_1 = ['bye sir', 'Sayonara', 'see you again sir', 'have a good day sir']

def speak(audio):
    """Function to make the assistant speak the given text."""
    engine.say(audio)
    engine.runAndWait()

def wish():
    """Function to greet the user based on the time of day."""
    time = int(datetime.datetime.now().hour)
    if 0 <= time < 12:
        speak("Good morning")
    elif 12 <= time < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Friday. How may I help you?")

def takecommand():
    """Function to take voice commands from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 0.5
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say again...")
        return "none"
    return query

def send_Email(to, content):

    sender = "divyajeetbiswal@gmail.com"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, 'jvgi zlzf lkiv ggdh')  
        server.sendmail(sender, to, content)
        speak("Email has been sent")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send this email")
    finally:
        server.quit()

if __name__ == "__main__":
    wish()
    while True:
        try:
            query = takecommand().lower()
            if "friday" in query:
                query = query.replace("friday", "")
                if "wikipedia" in query:
                    speak("Searching Wikipedia")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=1)
                    print(results)
                    speak(results)
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                elif "hello" in query:
                    speak(random.choice(reply))
                elif "play" in query:
                    query = query.replace("play", "")
                    query += " song"
                    for result in search(query, tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
                        print(result)
                        webbrowser.open(result)
                elif "open youtube" in query:
                    webbrowser.open("youtube.com")
                elif "search" in query:
                    query = query.replace("search", "")
                    for result in search(query, tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
                        print(result)
                        webbrowser.open(result)
                elif 'email' in query:
                    try:
                        to = input('Enter Receiver Email: ')
                        sub = input('Enter Subject: ')
                        msg = input('Enter Message: ')
                        content = f"Subject: {sub}\n\n{msg}"
                        send_Email(to, content)
                    except Exception as e:
                        print(e)
                        speak("Sorry, I am not able to send this email")
                elif "exit" in query or "bye" in query or "shutdown" in query:
                    speak(random.choice(reply_1))
                    exit()
                else:
                    for result in search(query, tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
                        print(result)
                        webbrowser.open(result)
        except Exception as e:
            print(e)
