import tkinter as tk
import PyPDF2
from PIL import Image,ImageTk
import turtle as tr

from tkinter.filedialog import askopenfile


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






root = tk.Tk() # beginning of the interface
#everything should be written in Tk and mainloop only
#variable canvas to enlarge


# root.title("KRISTY")
# root.configure(background='black')
canvas=tk.Canvas(root,width=600,height=300,background="black")
canvas.grid(columnspan=3,rowspan=3) #canvas initializer

#logo
root.title("KRISTY")
root.configure(background='black')
logo = Image.open('jarvis1.jpg')
logo = logo.resize((200,300))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image=logo #very important line
logo_label.grid(column=1,row=0) #line for placing the logo inside the window object

#instructions
instructions = tk.Label(root,activebackground='black',font='Railway')
instructions.grid(columnspan=3,column=0,row=1)

eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')
eng.setProperty('voice',voices[1].id)








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
    
    # browse_text.set("loading...")


def weather():

    # if (["weather","tell me the weather report","whats the condition outside"]):
    #     search_term = voice_data.split("for")[-1]
    url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
    webbrowser.get().open(url)
    speak("Here is today's weather report")


def news():
    url='https://timesofindia.indiatimes.com'
    webbrowser.get().open(url)
    speak("today's breaking news on times of india")   

def google():
    url = "https://google.com"
    webbrowser.get().open(url)
    speak("Here is google") 


def youtube():
    url = "https://youtube.com"
    webbrowser.get().open(url)
    speak("enjoy your time with youtubE") 

def location():
    url='http://ipinfo.io/json'
    response = urlopen(url)
    data=json.load(response)
    speak(data)
    text_box=tk.Text(root,height=10,width=50,padx=15,pady=15)
    text_box.insert(1.0,data)
    text_box.grid(column=1,row=3)

def amazon():
    url = "https://amazon.com"
    webbrowser.get().open(url)
    speak("Enjoy shopping") 

def battery():
    battery= ps.sensors_battery()
    percent=battery.percent
    speak(percent)
    # eng.say(battery.secsleft)
    # print(battery.secsleft,'seconds left to shutdown')
    n = battery.power_plugged
    if n ==False :
        speak('charging wire not plugged in')
    else:
        speak('charging wire plugged in')
    
def DateTime():
    now = datetime.datetime.now()
    time = now.strftime("20%y year/ %mth month/ %dday-- %Hhours:%Mminutes:%Sseconds")
    speak(time)
    text_box=tk.Text(root,height=10,width=50,padx=15,pady=15)
    text_box.insert(1.0,time)
    text_box.grid(column=1,row=3)
    
    
    # file = askopenfile(parent=root,mode='rb',title="choose",filetype=[('*Pdf file','*.pdf')])
    # if file:
    #     read_pdf=PyPDF2.PdfReader(file)
    #     page=read_pdf.pages[0]
    #     page_content='hello world'
    #     # page_content=page.extract_text()
    # #text box
    #     text_box=tk.Text(root,height=10,width=50,padx=15,pady=15)
    #     text_box.insert(1.0,page_content)
    #     text_box.grid(column=1,row=3)

def EXIT():
    speak("we could continue more sir but.,,...,,,,,..,,,,, byee")
    exit()
    

    browse_text.set("loading...")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:wishMe(),font='Railway',bg='#90ee90',fg="black",height=2,width=13)
browse_text.set("START 🏃‍♂️ ")
browse_btn.grid(column=1,row=3)

browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:weather(),font='Railway',bg='#00FFFF',fg="black",height=1,width=12)
browse_text.set("WEATHER ⛈️ ")
browse_btn.grid(column=0,row=5)

browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:news(),font='Railway',bg='#00FFFF',fg="black",height=1,width=12)
browse_text.set("NEWS 📰 ")
browse_btn.grid(column=2,row=5)

browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:google(),font='Railway',bg='#00FFFF',fg="black",height=1,width=12)
browse_text.set("GOOGLE 🥳 ")
browse_btn.grid(column=0,row=8)

browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:youtube(),font='Railway',bg='#00FFFF',fg="black",height=1,width=12)
browse_text.set("YOUTUBE 📺 ")
browse_btn.grid(column=2,row=8)

browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:location(),font='Railway',bg='#00FFFF',fg="black",height=1,width=12)
browse_text.set("LOCATION 📍 ")
browse_btn.grid(column=0,row=11)

browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:amazon(),font='Railway',bg='#00FFFF',fg="black",height=1,width=12)
browse_text.set("AMAZON 🛒 ")
browse_btn.grid(column=2,row=11)

browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:battery(),font='Railway',bg='#00FFFF',fg="black",height=1,width=12)
browse_text.set("BATTERY 🪫 ")
browse_btn.grid(column=0,row=14)

browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:DateTime(),font='Railway',bg='#00FFFF',fg="black",height=1,width=12)
browse_text.set("DATE,TIME 📆 ")
browse_btn.grid(column=2,row=14)

browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:EXIT(),font='Railway',bg='red',fg="black",height=1,width=12)
browse_text.set("EXIT ❌ ")
browse_btn.grid(column=1,row=16)

canvas=tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3,rowspan=3)

root.mainloop()