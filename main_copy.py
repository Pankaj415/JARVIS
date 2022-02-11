# wolframalpha

# imports
import random
from sys import exit
from ast import literal_eval
from datetime import datetime
from os import system, startfile, mkdir
import webbrowser
from random import choice, randrange
import ctypes
from smtplib import SMTP
import shutil

from time import sleep

# pip Install    pip Install    pip Install
from pyautogui import press, keyDown, keyUp
import pyjokes
from bs4 import BeautifulSoup
import pyqrcode
from requests import get, post
from wolframalpha import Client

#
from pyttsx3 import init
from wikipedia import summary

try:
    from pywhatkit import playonyt, sendwhatmsg_instantly
except:
    print("pywhatkit import failed")

try:
    from deep_translator import GoogleTranslator
except:
    print("GoogleTranslator import failed")

from modules_ import *
from system_ import *
from code_parts.general import general


agree = ['yes', 'sure', 'ok']
ques = ['what', 'who', 'when', 'whom', 'whose']
# **********************************************************************************************************************
Name = self['name']

# discord
file_discord = 'Files\\discord.txt'
with open(file_discord) as f_discord:
    data = f_discord.read()
discord_list = literal_eval(data)







def initialize():
    # History
    add("")
    add("*" * 50)
    add(datetime.now().strftime("%D %H:%M:%S"))

    speak("Initializing System")
    # Speak("Checking Internet Connection")
    # is_internet()
    # p = Process(target=folders_, args="C:\\Pankaj")
    # p.start()
    Speak('Scanning Folders')
    folders_("C:\\Pankaj")

    Speak('Scanning system')

    Speak("Initiation successfully done")


def temperature(place):
    """

    :param place: The place of which we have to find the temperature
    :return: return the temperature of the given location
    """
    search = f'temperature in {place}'
    url = f'https://www.google.com/search?q={search}'
    r = get(url)
    data = BeautifulSoup(r.text, 'html.parser')
    temp = data.find('div', class_='BNeawe').text
    return temp



def make_note(note):
    """

    :param note:
    :return:
    """
    date_ = str(datetime.now().date())
    time_ = datetime.now().strftime("%H:%M:%S")
    date_time = date_ + time_
    with open(f"Files/Note/note{user['note_no']}.txt", 'w') as f:
        f.write(f'{date_time}\n{note}\n')

    user['note_no'] += 1
    f_self = open('Files/self_.txt', 'w+')
    f_self.write(str(user))
    speak("Noted")


def avail(lis, sent):
    """

    :param lis: list of words which have be to search in sentence(sent)
    :param sent: Sentence in which the words from list(lis) hab=ve to search
    :return: return whether words of list(lis) are in sentence(sen) or not
    """
    n = 0
    for i in range(len(lis)):
        if lis[i] in sent:
            n += 1

    if n > 0:
        return True
    else:
        return False


# Not Completed
def send_mail():
    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user['email'], user['email_password'])

    speak("To whom you wan to send")
    takecommand()
    print(query)

    if query in contacts:
        to = contacts[query]['email']

        speak('What is the message')
        takecommand()
        message = query
        server.sendmail(user['email'], to, message)
        speak('Mail has been sent')

    else:
        print("Sorry sir this number is not in your contact list")
        speak("Sorry sir this number is not in your contact list")


def send_discord(to, msg):
    """

    :param to: discord channel_id of the person to send message
    :param msg: message to send
    :return: send the message on discord
    """
    # authorization in request headers in header section of browser of F12
    authorization = '745288958610768006'

    channel_id = to

    payload = {
        'content': msg
    }

    header = {
        'authorization': authorization

    }
    r = post(f'https://discord.com/api/v8/channels/{channel_id}/messages', data=payload, headers=header)

    print('Discord message has been sent')
    speak('Discord message has been sent')


def find_contact(qry):
    for name in contacts:
        if name in qry:
            print("Contact Found")
            return name
    for name in contacts:
        number = contacts[name]["phone number"][3:]
        if number in qry:
            print("Contact Found")
            return name


def qr(title, text, location):
    """

    :param location: folder where to save qr files
    :param title: name to give to the qr code image
    :param text: text to add in qr
    :return: create qr images and save in location folder
    """
    file_name_svg = title + '.svg'
    file_name_png = title + '.png'

    url = pyqrcode.create(text)

    url.svg(file_name_svg, scale=8)
    url.png(file_name_png, scale=10)

    mkdir(fr"QR\{title}")

    shutil.move(f'{file_name_svg}', f"{location}\\{title}")
    shutil.move(f'{file_name_png}', f"{location}\\{title}")


def check(lis, query):
    re = False
    for i in lis:
        if i in query:
            re = True
        else:
            pass
    return re


def BMI(height, weight):
    """

    :param height: height in centimeter
    :param weight: weight in kilograms
    :return: BMI
    """
    height = height / 100
    BMI = weight / (height * height)
    print("your Body Mass Index is: ", round(BMI, 2))
    if BMI > 0:
        if BMI <= 16:
            print("you are severely underweight")
        elif BMI <= 18.5:
            print("you are underweight")
        elif BMI <= 25:
            print("you are Healthy")
        elif BMI <= 30:
            print("you are overweight")
        else:
            print("you are severely overweight")
    else:
        print("enter valid details")


def yt_automation():
    """

    :return: automate the youtube through users voice
    """
    yt_shorts = {
        'pause video': 'k',
        'play video': 'k',
        'mute': 'm',
        'full screen': 'f',
        'captions': 'c',
        'move to next video': 'Shift N',
        'move to previous video': 'Shift P',
        'open the miniplayer': 'i',
        'search': '/',
        'restart': '0',
        'slow down': '<',
        'speed up': '>',
        'next frame': '.',
        'previous frame': ',',
        'increase volume': 'up',
        'decrease volume': 'down',
        'back': 'j',
        'forward': 'l',
        'theater mode': 't'
    }

    while True:
        query = takecommand()
        if 'exit youtube automation' in query:
            break
        for i in yt_shorts:
            if i in query:
                c = yt_shorts[i].split()
                if len(c) == 1:
                    press(yt_shorts[i])
                elif len(c) == 2:
                    keyDown(c[0])
                    press(c[1])
                    keyUp(c[0])


def wolframalpha_(query):
    """

    :param query: question to search
    :return: answer of the question from wolframalpha's api
    """
    work = False
    global app
    app_id = '3L7XKL-R45HWVAAJX'
    try:
        app = Client(app_id=app_id)
    except Exception as e:
        # print('app', e)
        pass
    res = app.query(query)
    try:
        ans = next(res.results).text
        # print(ans)
        work = True
    except Exception as e:
        ans = ''
        # print('ans', e)
        work = False
        pass
    if work:
        return work, ans



while True:

    elif 'play music' in query or 'play song' in query:
        if "on youtube" in query:
            speak("What you want to play?")
            query = takecommand()
            playonyt(query)

        else:
            try:
                music_dir = systm['songs']
                songs = listdir(music_dir)
                # print(songs)
                n = randrange(len(songs))
                speak(f"Playing {songs[n]}")
                startfile(path.join(music_dir, songs[n]))
            except:
                speak("Songs Folder not found")

    elif 'note' in query:
        make_note("Hello")

    elif 'send mail' in query:
        send_mail()

    elif 'send whatsapp' in query or 'send a whatsapp' in query:
        to = find_contact(query)
        if to is None:
            speak("To whom you want to send")
            query = takecommand()
            to = find_contact(query)
        to = contacts[to]['phone number']

        speak("What is the message?")
        msg = takecommand()
        try:
            msg = msg.replace('the message is', '')
        except Exception as e:
            pass
        try:
            msg = msg.replace('message is', '')
        except Exception as e:
            pass

        sendwhatmsg_instantly(to, msg, 5)

    elif 'send a discord' in query:
        print("To whom you want to send")
        speak("To whom you want to send")
        takecommand()
        name = query
        print(name)
        to = True
        for i in discord_list:
            if i in name:
                to = discord_list[i]
                print(to)

                print()
                print("What is the message?")
                speak("What is the message?")
                takecommand()
                msg = query

            else:
                to = False
                print()
                print("Sorry this is not in you contact")
                speak("Sorry this is not in you contact")

        if to:
            send_discord(to, msg)
        else:
            pass

    elif 'tell a joke' in query:
        speak('Sure')
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif 'where is' in query:
        print('Checking...')
        speak('Checking...')
        ind = query.lower().split().index('is')
        location = query.split()[ind + 1:]
        url = "https://www.google.com/maps/place/" + "".join(location)
        speak(f"this is where {str(location)} is")
        webbrowser.open(url)

    elif 'translate' in query:
        to_translate = query.replace('translate', '')
        print('In which language you+ want to translate?')
        speak('In which language you+ want to translate?')

        to = takecommand()
        translated = GoogleTranslator(source='en', target=to).translate(to_translate)
        print(translated)
        speak(translated)


    elif 'check typing speed' in query or "check my typing speed" in query:
        speak('Sure sir')
        from typing_speed_test import test

        test()

    elif 'nasa news' in query:
        speak("Searching latest NASA news...")
        url = "https://api.nasa.gov/planetary/apod?api_key=wtphnyVvkDmyV9W9REkvFLNcLtLh5tbF9H5vjCZc"
        r = get(url)
        data = r.json()
        print(data['date'])
        speak("Today's NASA News is...")
        webbrowser.open(data['hdurl'], 1)         # Shows image related to news
        speak(data['explanation'])

    elif 'location' in query:
        speak("Getting location...")
        ip_add = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_q = get(url)
        geo_d = geo_q.json()
        country = geo_d['country']
        city = geo_d['city']
        speak(f"Sir, your current location is {city}, {country}")

# **********************************************************************************************************************
#               Automation / Mode

    elif 'start youtube automation' in query or 'run youtube automation' in query:
        speak('Sure sir')
        speak('But make sure you have opened youtube. If not should i open it')
        takecommand()
        if check(agree, query):
            query = "open youtube"
            open_()
        elif 'already opened' in query or 'opened' in query:
            speak("That's great sir")
        speak('Starting youtube automation mode')

        yt_automation()

    elif check(ques, query):
        que = query.replace('jarvis', '')
        speak("Searching answer...")
        try:
            work, ans = wolframalpha_(que)
        except:
            work = False

        if work:
            speak(ans)

        elif 'how in query' in que:
            import pywikihow
            how = pywikihow.search_wikihow('how to make chapati', 1)
            assert len(how) == 1
            how[0].print()
            speak('Look at the Output Tab for answer')

        else:
            speak('Not found any answer')
            his = open("Files//unanswered.txt", "a")
            his.write("\n")
            his.write(query)
            his.close()

    query = ""
