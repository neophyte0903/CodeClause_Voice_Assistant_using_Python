import os

import pyttsx3,datetime
import speech_recognition as sr
import wikipedia,webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am julia sir. Please tell me how may i help you?")

def takecommand():
    #it takes microphone input and string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print('user said: ',query)

    except Exception as e:
        print(e)

        print('say that again please')
        return "none"
    return query

if __name__=="__main__":
    WishMe()
    while True:
        query=takecommand().lower()
        #logic for executing task
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir='D:\\ai ke panne\\assistant\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strTime}")