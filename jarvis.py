import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import smtplib
import random
import cx_Oracle

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def reminder():
    try:
        con=cx_Oracle.connect('system/1234@localhost')
        cur=con.cursor()
        cur.execute("select * from reminder where doe = trunc(sysdate)")
        data=cur.fetchall()
        for row in data:
            name=row[1]
        rem="This is a reminder that today is Birthday of "+ name
        speak(rem)
        
    except cx_Oracle.DatabaseError as e:
        if con:
            con.rollback()
            print("There is a problem: ",e)

    finally:
        if cur:
            cur.close()
        if con:
            con.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hi, I'm Jarvis. How may I help you")


def takeCommand():
    # Itpippip take microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_thresold = 1
        audio = r.listen(source)

    try:

        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"

    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chittithe13@gmail.com','chittitherobo2.0')
    server.sendmail('chittithe13@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()  
    reminder()

    
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query

        if 'wikipedia' in query:

            speak('Searching wikipedia....')
            query = query. replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you jarvis'in query:
            speak("im fine sir what about you") 
            
        elif 'all good'in query:
            speak("great sir have a good day") 

        elif 'open youtube' in query:
            speak("wait youtube is openning") 
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("wait google is openning")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("wait stackoverflow is openning")
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            speak("wait facebook is openning") 
            webbrowser.open("facebook.com")

        elif 'open flipkart' in query:
            speak("wait flipkart is openning") 
            webbrowser.open("flipkart.com")

        elif 'open amazon' in query:
            speak("wait amazon is openning") 
            webbrowser.open("amazon.com")

        elif 'open instagram' in query:
            speak("wait instagram is openning") 
            webbrowser.open("instagram.com")

        elif 'open chrome' in query:
            speak("wait chrome is openning")
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open vs code' in query:
            speak("wait vs code is opening")
            os.startfile("C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        
        
        elif 'play music' in query:
            music_dir = 'G:\\Music\\New Astomintal'
            songs = os.listdir(music_dir)
            sl = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[sl]))
        
        elif 'please tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'please tell me date' in query:
            strTime = datetime.datetime.today().strftime("%d %m %y")    
            speak(f"Sir, the Date is {strTime}")

        elif 'google' in query:
            query = query.replace("google", "")
            webbrowser.open(query)


        elif 'email to mayank' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "sahumayank.18@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
 
            except Exception as e:
                print(e)
                speak("Sorry, Email can't be sent")

        elif 'exit' or 'quit' in query:
            speak("Thank you sir")
            break


         
    
    