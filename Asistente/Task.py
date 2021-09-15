#Function
#from Asistente.Speak import Speak
import datetime
from Speak import Speak
#2 Types

#1 - Non Input
#eg: Time , Date , Speedtest

def Time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    Speak(time)

def Date():
    day = datetime.datetime.now().strftime("%d/%m/%Y")
    Speak(day)

def Day():
    date = datetime.date.today()
    Speak(date)

def NonInputExecution(query):

    query = str(query)

    if "hora" in query:
        Time()

    elif "fecha" in query:
        Date()

    elif "día" in query:
        Day()

#2 - Input
#eg - google search , wikipedia

def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("quién es","").replace("sobre","").replace("qué es","").replace("wikipedia","")
        import wikipedia
        wikipedia.set_lang("es")
        result = wikipedia.summary(name,1)
        Speak(result)

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("buscar","")
        import pywhatkit
        pywhatkit.search(query)
