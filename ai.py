import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


#setting up voice of (step-1)
engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

#speak function(step-2)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wish function(step-4)
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
       speak("morning sir!")

    elif hour>=12  and hour<16:
        speak("good afternoon sir!")

    elif hour>=16 and hour<20:
        speak("good evening sir!")

    else:
        speak("good night!")

    speak("ready ")


#function to take input from user from mic and return string[use energy_threshold for changing loudness of input](step-3)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...")
       r.energy_threshold=700
       r.pause_threshold = 1
       audio = r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Please say that again...")
        return "None"
    return query


#funtion to send email(step-5)
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender mail id','password')
    server.sendmail('sender mail id',to, content)
    server.close()


#main function
if __name__ == '__main__':

    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query

            #wikipedia search
        if 'wikipedia' in query:
            speak('Let me look...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


           #browser based actions
        elif 'fire youtube' in query:
            webbrowser.open("youtube.com")

        elif 'fire google' in query:
            webbrowser.open('Google.com')


            #music
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Sameer Yadav\\Desktop\\songs'
            songs = os.listdir(music_dir)
            print(songs)#use random module to randomize songs
            os.startfile(os.path.join(music_dir,songs[0]))

            #current time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

            #open specific apps
        elif 'open vlc media player' in query:
            vlcPath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcPath)

            #sending email
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "ronitroi040@gmail.com"
                sendEmail(to,content)
                speak("Email sent")
            except Exception as e:
                print(e)
                speak("sorry sir can't able to send email at the moment")

