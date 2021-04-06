import pyttsx3
import googlemaps
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib 
import ctypes
import time
import subprocess
import string
import PyDictionary
import requests,json
import random
from ecapture import ecapture as ec

'''
The Speech Application Programming Interface or SAPI is an 
API developed by Microsoft to allow the use of speech recognition 
and speech synthesis within Windows applications. 
'''

mailDir={
        #Enter your email directory here to send the email
    }
engine=pyttsx3.init('sapi5')
# There are 2 voices in the system, male and female
voices=engine.getProperty('voices')
#Here, we have set the female voice as engine property
engine.setProperty('voice',voices[0].id)

#This function takes audio (text input) and converts it to audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#This function wishes you according to the current date and time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >=12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Olivia. How may I help you?")


def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        #Pause threshold: Seconds of non-speaking audio before a phrase is complete 
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

#Enable less secure apps for gmail before sending
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    file=open("key.txt","rt")
    password=file.read()
    file.close()
    server.login('your-email-id-here','your-password-here')
    server.sendmail('your-email-id-here',mailDir[to],content)
    server.close()

def work():
    wishMe()
    chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    while True:
        query=takeCommand().lower()
        #Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.get(chromepath).open('youtube.com')
        elif 'open google' in query:
            webbrowser.get(chromepath).open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.get(chromepath).open("stackoverflow.com")
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\Dell\\Music"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                speak("To whom should I send the email?")
                to=takeCommand()
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email at the moment")
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
        elif "camera" in query or "take a photo" in query:
            N = 7
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
            speak("Take a pose!")
            speak("3")
            speak("2")
            speak("1")
            ec.capture(0, "Olivia Camera ", "/images/"+res+".jpg")
            speak("Picture taken!")
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            
        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            #Sign in to openweathermap website to get API
            api_key = "your-api-key"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x['main']
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature (in kelvin unit) = " +
                        str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+
                        str(current_pressure) +"\n humidity (in percentage) = " +
                        str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")
            
        elif "meaning" in query:
            dic=PyDictionary.PyDictionary()
            speak("Say the word you wanna find meaning of")
            word=takeCommand()
            ans=dic.meaning(word)
            print(ans)
            for state in ans:
                print(ans[state])
                speak("the meaning in "+state+ " form is" + str(ans[state]))
        
        elif "distance" in query:
            speak("Tell the cities you wanna know distance between")
            speak("First city")
            city1=takeCommand()
            speak("Second city")
            city2=takeCommand()
            webbrowser.open("https://www.google.nl/maps/dir/" + city1 + "/"+city2)
        
        elif "quit" in query or "close" in query:
            exit()
        
        

#Main function 
if __name__=="__main__":
    work()
    
    

    