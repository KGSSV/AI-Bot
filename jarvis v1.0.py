import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import string
import random
import pyautogui
import os
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')


def speak(audio):
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def time_():
    time = datetime.datetime.now().strftime(
        '%I:%M:%S')   # for 24 hrs use %h and 12hrs use %i
    speak('the current time is')
    speak(time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak('The current date is')
    speak(year)
    speak(month)
    speak(day)


def wishme_():
    hour = datetime.datetime.now().hour

    speak('Welcome Back AKhil')
    time_()
    date_()

    if hour > 6 and hour <= 12:
        speak('Good morning Sir')
    elif hour > 12 and hour <= 18:
        speak('Good afternoon Sir')
    elif hour > 18 and hour <= 23:
        speak('Good evening Sir')
    else:
        speak('Good night Sir')

    speak('friday at your service. what can i do for you today')


def takecmd():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print('Listening....')
        # waits for one second as threshold if no input to microphone given
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print('Please say that again')
        return 'None'
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # now make your bot login to your gmail
    server.login("kgssvak2@gmail.com", "key / pass")
    server.sendmail('kgssvak2@gmail.com', to, content)
    server.quit()


def cpu():

    cpuper = str(psutil.cpu_percent())
    batper = psutil.sensors_battery()
    print(cpuper)
    print(batper)
    speak('The cpu utilization is at ' + cpuper)
    speak('battery percentage is at')
    speak(batper.percent)


def joke():
    speak('Lets try This!!')
    speak(pyjokes.get_joke())


def screenshot():
    n = 7
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

    img = pyautogui.screenshot()
    #path = 'C:/Users/akura/Desktop/{nam}.png'.format(nam=name)
    img.save('{nam}.png'.format(nam=name))
    speak('image saved successfully under name {n}'.format(n=name))


if __name__ == "__main__":

    # wishme_()

    while True:
        query = takecmd()

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()

        elif 'wikipedia' in query:
            print('Searching....')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak('According to Wikipedia')
            print(result)
            speak(result)

        elif 'send' in query and ('mail' or 'email') in query:
            email_flag = 1
            try:
                speak('What should i send sir')

                while True:
                    if email_flag == 0:
                        break
                    content = takecmd()
                    resp = ''
                    if content == 'None':
                        speak(
                            'did not understand sir !!! do you want to type the email')
                        resp = takecmd()
                        if 'no' in resp:
                            speak('Please Say the message clearly')
                            content = takecmd()
                        if 'yes' in resp:
                            content = input('Enter email content : ')
                    print(content)
                    speak('is it ok to send this email content')
                    response = takecmd()
                    choice = ['ok', 'yes', 'yup',
                              'done', 'okay', 'fine']
                    for word in choice:
                        if word in response:
                            email_flag = 0
                            break
                    ch = ['nope', 'don\'t', 'no']
                    for word in ch:
                        if word in response:
                            speak('please say email content again')
                            break
                speak('Who do you want to send sir')
                to = input('Receiver email :')
                speak('Sending')
                sendemail(to, content)
                speak('email sent successfully sir')

            except Exception as e:
                print(e)
                speak('Sending failed')

        elif 'search in Chrome' in query:
            speak('what should i search')
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = takecmd().lower()
            # takes the path to exe appends in url form with .com
            wb.get(path).open_new_tab('https://google.com/search/' + search)

        elif 'search youtube' in query:
            speak('what should i search')
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = takecmd().lower()
            # takes the path to exe appends in url form with .com
            speak('hear we go to youtube')
            wb.get(path).open_new_tab(
                'https://www.youtube.com/results?search_query=' + search)

        elif 'search Google' in query:
            speak('what should i search')
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = takecmd().lower()
            # takes the path to exe appends in url form with .com
            speak('finding search results')
            speak('opening chrome to view results')

            wb.get(path).open_new_tab(
                'https://www.google.com/search?q=' + search)

        elif 'cpu' in query:
            cpu()

        elif ('laugh' or 'joke') in query:
            joke()

        elif ('offline') in query:
            speak('friday Going offline sir.')

            quit()
        elif ('remember' or 'note') in query:
            if 'remember' in query:
                speak('What do you want me to remember!')
            elif 'note' in query:
                speak('what do you want me to note!!')
            file = open('notes.txt', 'w')
            while True:
                notes = takecmd()
                currenttime = datetime.datetime.now().strftime('%I:%M:%S')
                file.write(currenttime)
                file.write(':-')
                file.write(notes)
                file.write('\n')
                speak('remembered successfully...  want to take an another note')
                word = takecmd()
                choice = ['ok', 'yes', 'yup',
                          'done', 'okay', 'fine']
                if word not in choice:
                    speak('ok')
                    break
                speak('please say what else to remember!!')

        elif 'show' in query:
            file = open('notes.txt', 'r')
            print(file.read())

        elif 'screenshot' in query:
            speak('taking screenshot')
            screenshot()

        elif ('songs' or 'song') in query:
            songsdir = 'C:/Songs'
            music = os.listdir(songsdir)
            speak('what should i play')
            print(music)
            ans = input()

            no = int(ans.replace('number', ''))
            os.startfile(os.path.join(songsdir, music[no]))

        elif 'news' in query:
            url = 'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey='
            response = requests.request('GET', url)
            print(response)
            response = response.json()
            i = 1
            for item in response['articles']:
                print(str(i) + '. ' + item['title']+'\n')
                print(item['description'])
                i += 1
                print()

        elif 'where is' in query or 'locate' in query:
            speak('what should i locate')
            location = takecmd()
            speak('locating' + location)
            p = 'https://www.google.com/maps/place/' + location
            wb.open_new_tab(p)
