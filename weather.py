import pyttsx3
import requests 
import tkinter
from tkinter import *
from bs4 import BeautifulSoup 
from geopy.geocoders import Nominatim

window = tkinter.Tk()
window.title("Weather forcast")
window.geometry("600x300")
def speak(text):
    #initiaize the class
    engine = pyttsx3.init()

    #
    engine.setProperty('rate', 160)

    #changethe voice of speaker
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    #utter the words
    engine.say(text)

    engine.runAndWait()
  

label = tkinter.Label(window, text = "welcome to the weather forcasting app", bd=8, relief=GROOVE, font = ("times new roman", 24), bg='#3498DB', fg='black').pack()
 
label = tkinter.Label(window, text = ' ').pack()
 
label = tkinter.Label(window, text = 'Enter Location:', font = ("times new roman", 20)).pack()
e = Entry(window,font = ("times new roman", 15), bd=5, relief=GROOVE)
e.config(fg='black')
e.pack()

def get_weather():
    geolocator = Nominatim(user_agent='Anay')
    location = geolocator.geocode(e.get())
    lat = location.latitude
    lon = location.longitude 

    page = requests.get("https://weather.com/en-IN/weather/today/l/{},{}?par=google&temp=c".format(lat,lon))

    soup = BeautifulSoup(page.text, "html.parser") 

    temp = soup.find("span", class_='CurrentConditions--tempValue--3KcTQ')
    print_t = 'Temperature is ' +  temp.text
    label1 = tkinter.Label(window, text = print_t).pack()
  
    weather = soup.find("div", class_='CurrentConditions--phraseValue--2xXSr')
    print_w = 'Weather is ' + weather.text
    label2 = tkinter.Label(window, text = print_w).pack()
    
    humidity = soup.find("span", attrs={'data-testid':'PercentageValue'})
    print_h = 'Humidity is '+ humidity.text
    label3 = tkinter.Label(window, text = print_h).pack()

    air_qual_index = soup.find("text", class_='DonutChart--innerValue--k2Z7I')
    print_a = 'Air Quality Index is '+ air_qual_index.text
    label4 = tkinter.Label(window, text = print_a).pack()
    
    air_qual = soup.find("p", class_='AirQualityText--severityText--3QoOU')
    print_q = 'Air Quality ' + air_qual.text
    label5 = tkinter.Label(window, text = print_q).pack()
    
    def button_2():    
        speak(print_t)
        speak(print_w)
        speak(print_h)
        speak(print_a)
        speak(print_q)
    tkinter.Button(window, text = "Speak", command = button_2).pack()
    
tkinter.Button(window, text = "Output", command = get_weather).pack()

window.mainloop()