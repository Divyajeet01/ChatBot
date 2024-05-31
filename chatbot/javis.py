import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
from googlesearch import search

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    time=int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("good morning")
    elif time>=12 and time<18:
        speak("good afternoon")
    else :
        speak("good evening")
    speak("i am Friday. how may i help u")
def takecommand():
    a=sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening....")
        a.pause_threshold=0.5
        audio=a.listen(source)

    try:
        print("Recongnizing >>>")
        q=a.recognize_google(audio,language="en")
        print(f"user said : {q}\n")
    except Exception as e:
        print("Say again....")
        return "none"
    return q

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('divyajeetbiswal@gmail.com', 's@odisha12')
    server.sendmail('divyajeetbiswal@gmail.com', to, content)
    server.close()



if __name__=="__main__":
    try:
        wish()
        while True:
            t=takecommand().lower()
        #only responde if name taken
            if "friday" in t:
                t=t.replace("friday"," ")
                if "wikipedia" in t:
                    speak("Searching Wikipedia")
                    t=t.replace ("wikipedia","")
                    result=wikipedia.summary(t,sentences=2)
                    print(result)
                    speak(result)
                elif "time" in t:
                    x=datetime.datetime.now()
                    time= x.strftime("%H:%M")
                    time=time.replace(":"," ")
                    if int(datetime.datetime.now().hour)<12:
                        time=time+" a m"
                    else:
                        time=time+" p m"
            
                    speak(time)
                elif "hello" in t:
                    speak("hello,nice to meet u")
                elif "play"  in t:
                    t=t.replace("play","")
                    t=t+" song"
                    print(t)
                    for i in search(t,tld = 'com',lang = 'en',num = 1,start = 0,stop = 1,pause = 2.0,):  
                        print(i)
                    webbrowser.open(i)

                elif "open youtube" in t:
                    webbrowser.open("youtube.com")  
                elif "search " in t:
                    t=t.replace("search","")
                    print(t)
                    for i in search(t,tld = 'com',lang = 'en',num = 1,start = 0,stop = 1,pause = 2.0,):  
                        print(i)
                    webbrowser.open(i) 
                
                elif "email" in t:
                    from email.message import EmailMessage
                    msg = EmailMessage()
                    msg.set_content("hello")
                    msg['Subject'] = 'The contents of '
                    msg['From']='divyajeetbiswal@gmail.com'
                    msg['To']="divyajeetbiswal@gmail.com"
                    try:
                        s = smtplib.SMTP('localhost')
                        s.send_message(msg)
                        s.quit()
                    except Exception as f:
                        print(f)
                    '''elif "email" in t:
                    try:
                        speak("reciever email address ")
                        to=takecommand()
                        to=to.replace(" ","")
                        speak("content ")
                        a=takecommand()
                        sendEmail(to,a)
                    except Exception as x:
                        print(x)
                        speak("email not send")'''
                    


                elif "exit"  in t:

                    speak("sayonara")
                    exit()
                    
                   
                else :
                    for i in search(t,tld = 'com',lang = 'en',num = 1,start = 0,stop = 1,pause = 2.0,):  
                        print(i)
                    webbrowser.open(i)
    except Exception as e:
        print (e)
                    



    
