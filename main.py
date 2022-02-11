# installed modules
"""
pyaudio,SpeechRecognition,pyttsx3
"""

# Imports
import ast
import datetime
import multiprocessing
import os
import time
import ctypes
import random
import urllib
import webbrowser
import requests

# Installed imports
# import pyaudio
import wikipedia
import pyttsx3  # (init)
import speech_recognition as sr
import pyautogui
import plyer

# file imports
import system_
import modules_

# **********************************************************************************************************************
# ENGINE

# engine properties
voice_id = 1
volume = 1
rate = 200

engine = pyttsx3.init('sapi5')  # Builds the engine to speak
voices = engine.getProperty('voices')  # list of all the voices available on the system

# Sets the properties of the engine
engine.setProperty('rate', rate)  # Sets the speech rate in words per minute
engine.setProperty('volume', volume)  # Sets the volume
engine.setProperty('voices', voices[voice_id].id)  # Sets the voice

# **********************************************************************************************************************
"""
    Fetching details from external files
"""

# Self
f_self = open("Files\\self_.txt")
data_self = f_self.read()
self = ast.literal_eval(data_self)

Name = self['name']

# User
f_user = open("Files\\user.txt")
data_user = f_user.read()
user = ast.literal_eval(data_user)

# Applications
f_app = open("Files\\applications.txt")
data_apps = f_app.read()
apps = ast.literal_eval(data_apps)

# Websites
f_web = open("Files\\websites.txt")
data_webs = f_web.read()
webs = ast.literal_eval(data_webs)

# Contacts
f_contact = open("Files\\contacts.txt")
data_contacts = f_contact.read()
contacts = ast.literal_eval(data_contacts)

# System
f_system = open("Files\\systm.txt")
data_system = f_system.read()
systm = ast.literal_eval(data_system)


# **********************************************************************************************************************
# Functions


# Speak th given argument
def speak(audio):
    """

    :param audio: test to be speaked
    :return: text in audio format and add to history
    """
    print(audio)
    engine.say(audio)
    add(f"{Name}: {audio}")
    engine.runAndWait()


# Speak th given argument
def Speak(audio):
    """

    :param audio: test to be speaked
    :return: text in audio format
    """
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    global query
    query = ""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.energy_threshold = 800
        # recognizer.pause_threshold = 0.8        # seconds of non-speaking audio before a phrase is considered complete
        # recognizer.phrase_threshold = 0.3
        # recognizer.adjust_for_ambient_noise(source, duration=1)
        # recognizer.non_speaking_duration = 0.5  # seconds of non-speaking audio to keep on both sides of the recording
        recorded_audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(recorded_audio)
        query = text.lower()
        print("User: ", query)

    except Exception as ex:
        print("Error")
        print(ex)

    add(f"User: {query}")

    return query


def initialize():
    # History
    add("")
    add("*"*50)
    add(datetime.datetime.now().strftime("%D %H:%M:%S"))

    speak("Initializing System")

    Speak("Scanning Folders and System")
    p1 = multiprocessing.Process(target=modules_.folders_, args=("C:\\Pankaj",))
    p1.start()

    p1.join()
    speak("Initiation successfully Done")


def open_():
    """

    :return: Open the application given by the user
    """
    speak("Sure")
    if "open google" in query:
        speak("What should i search on google?")
        takecommand()
        webbrowser.open(query)
        speak('Opening google Sir...')

    else:
        for i in apps:
            if i in query:
                app = i.replace('open ', '')
                os.startfile(apps[i])
                speak(f"Opening {app}...")
                break

        for j in webs:
            if j in query:
                web = j.replace('open ', '')
                webbrowser.open(webs[j])
                speak(f"Opening...{web}")
                break


def close_():
    """

    :return: Close the application given by the user
    """
    speak("Sure")
    for i in apps:
        if i in query:
            app = i.replace('close ', '')
            os.system(f"taskkill /f  /im {apps[i]}")
            speak(f"Closing {app}...")
            break

    for j in webs:
        if j in query:
            web = j.replace('close ', '')
            os.system("taskkill /f  /im msedge.exe")
            speak(f"Closing{web}...")
            break


def is_internet():
    """

    :return: Returns whether system is connected to internet or not
    """
    try:
        requests.urlopen('https://www.google.com', timeout=1)
        # var = True
        return True
    except urllib.error.URLError as Error:
        # var = False
        return False


def wish():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning Sir")
        time_phase = "AM"
    elif 12 <= hour < 18:
        speak("Good Evening Sir")
        time_phase = "PM"
    else:
        speak("Good Evening Sir")
        time_phase = "PM"

    text = "It is " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + " " + str(
        time_phase)
    speak(text)

    speak(f"I am {Name}. How may i help you")


def background():
    phrase = ''
    img = systm['wallpaper'][random.randrange(1, len(systm['wallpaper']) + 1)]
    list_img = os.listdir(img)
    imgChoice = random.choice(list_img)
    randomImg = os.path.join(img, imgChoice)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
    if 'background' in query:
        phrase = 'Background'
    elif "wallpaper" in query:
        phrase = 'Wallpaper'

    speak(f"{phrase} changed successfully")


def add(txt):
    global his
    his = open("Files\\history.txt", "a")
    his.write("\n")
    his.write(txt)
    his.close()


def pomodoro(con, for_):
    if con:
        speak("Pomodoro started")
        for j in range(for_ * 3):
            time.sleep(3)
            """plyer.notification.notify(
                title="Break time",
                message="Let's Take a break",
                timeout=3
            )
            speak("It's Break time")"""
            print("# seconds")


if __name__ == '__main__':
    # initialize()
    # if 1:
    while True:
        # query = takecommand()
        query = "wake up"

        # Checks for any other voice request
        if 'zira' in query:
            engine.setProperty("voice", voices[1].id)
        elif 'david' in query:
            engine.setProperty("voice", voices[2].id)
        else:
            pass

        if 'wake up' in query:
            # wish()

            # if 1:
            while True:
                # query = takecommand()
                query = "pomodoro"


                if "open" in query:
                    open_()

                elif 'close' in query:
                    close_()

                elif 'wikipedia' in query:
                    speak("Searching Wikipedia...")
                    query = query.replace('wikipedia', '')
                    result = wikipedia.summary(query, sentence=2)
                    speak("According to Wikipedia")
                    speak(result)
                # JARVIS***********************************************************************************************
                elif 'change your voice' in query:
                    speak("Sure")
                    if voice_id == 0:
                        voice_id = 1
                    elif voice_id == 1:
                        voice_id = 0

                    engine.setProperty('voices', voices[voice_id].id)
                    speak("Voice Changed Successfully")

                elif "your" in query and "speech rate" in query:
                    speak(f"My current speech rate is {rate}")

                elif 'change' in query and "your speech rate" in query:
                    query = query.split()
                    rate = query[query.index('to') + 1]
                    engine.setProperty('rate', rate)

                elif "your" in query and "speech volume" in query:
                    speak(f"My current speech volume is {volume}")

                elif 'change' in query and "your speech volume" in query:
                    query = query.split()
                    volume = query[query.index('to') + 1]
                    engine.setProperty('volume', volume)

                # Modes************************************************************************************************

                elif 'pomodoro' in query:
                    p1 = multiprocessing.Process(target=pomodoro, args=[True,50])
                    p1.start()
                    # p1.

                elif 'end' in query:
                    p1.terminate()

                # System***********************************************************************************************

                elif 'change background' in query or 'change wallpaper' in query:
                    background()

                elif "volume" in query:
                    if "mute" in query:
                        pyautogui.press('volumemute')

                    n = 2
                    for i in num:
                        if i in query:
                            n = num.index(i) + 1

                    if "volume up" in query or "increase volume" in query:
                        pyautogui.press("volumeup", n)
                    elif "volume down" in query or "decrease volume" in query:
                        pyautogui.press("volumedown", n)

                elif "switch the window" in query or "switch window" in query:
                    pyautogui.keyDown('alt')
                    pyautogui.press('tab')
                    time.sleep(0.1)
                    pyautogui.keyUp('alt')

                elif 'boot time' in query:
                    speak(system_.boot_time_())

                elif "power remaining" in query or "battery remaining" in query:
                    speak(system_.battery_remaining())

                elif "battery time" in query:
                    speak(system_.battery_time())

                elif 'memory usage' in query:
                    speak(system_.usage("memory"))

                elif 'disk usage' in query:
                    speak(system_.usage("disk"))

                elif 'sleep system' in query:
                    speak('Sir are you sure that you want system sleep')
                    takecommand()
                    if check(agree, query):
                        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    else:
                        speak("System sleep aborted")

                elif 'restart the system' in query or 'restart system' in query:
                    speak('Sir are you sure that you want to restart the system')
                    takecommand()
                    if check(agree, query):
                        os.system("restart /r /t s")
                    else:
                        speak("System restart aborted")

                elif "shutdown the system" in query or "shutdown the pc" in query or "shutdown system" in query or "shutdown pc" in query:
                    speak('Sir are you sure that you want to shutdown the system')
                    takecommand()
                    if check(agree, query):
                        os.system("shutdown /r /t s")
                    else:
                        speak("System shutdown aborted")

                elif 'you can sleep' in query or 'you may sleep' in query:
                    speak("Ok sir")
                    break

                elif f"quit {Name}" in query:
                    speak("Terminating the code")
                    exit()

                else:
                    speak("Not found any answer")
                    his = open("Files\\history.txt")
                    his.write("")
                    his.write(query)
                    his.close()

        elif 'bye' in query or 'quit' in query:
            speak("Terminating the code")
            exit()
