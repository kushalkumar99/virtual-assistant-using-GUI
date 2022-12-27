import pyttsx3
import datetime
from gtts import gTTS
import playsound
import os
import random
import speech_recognition as sr
import webbrowser
import psutil as ps
import json
from urllib.request import urlopen


eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')
eng.setProperty('voice',voices[1].id)

class asis:
    name = ''
    def setName(self, name):
        self.name = name




r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def speak(audio):
    eng.say(audio)
    eng.runAndWait()


def wishMe():
    hr = int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("good morning")

    elif hr>=12 and hr<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("I am kristy. how may i help you???")  


def respond(voice_data):

    #time and date
    if there_exists(['what is time and date','what is time',"what is today's date"]):
        now = datetime.datetime.now()
        time = now.strftime("20%y year/ %mth month/ %dday-- %Hhours:%Mminutes:%Sseconds")
        print(time)
        eng.say(time)
        eng.runAndWait()

    #weather
    if there_exists(["weather","tell me the weather report","whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")
    
     #battery level
    if there_exists(['show me the battery level','battery level','battery percentage']):
        battery= ps.sensors_battery()
        percent=battery.percent
        eng.say(percent)
        print(percent,'percent')
        eng.say(battery.secsleft)
        print(battery.secsleft,'seconds left to shutdown')
        n = battery.power_plugged
        if n ==False :
            eng.say('charging wire not plugged in')
        else:
            eng.say('charging wire plugged in')
        eng.runAndWait()

    #location
    if there_exists(['my location','give me my location']):
        url='http://ipinfo.io/json'
        response = urlopen(url)
        data=json.load(response)
        eng.say(data)
        print(data)
        eng.runAndWait()

    #news
    if there_exists(["what is today's news",'breaking news','news headlines']):
        url='https://timesofindia.indiatimes.com'
        webbrowser.get().open(url)
        engine_speak("today's breaking news on times of india")

    #google search
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

asis_obj = asis()

if __name__=="__main__":
    wishMe()


while(1):
    voice_data = record_audio("Listening...") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond