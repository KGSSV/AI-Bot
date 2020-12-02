import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil

engine = pyttsx3.init()


def speak(audio):
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
    speak('Welcome Back Akhil')
    time_()
    date_()

    if hour > 6 and hour < 12:
        speak('Good morning Sir')
    elif hour > 12 and hour < 18:
        speak('Good afternoon Sir')
    elif hour > 18 and hour < 23:
        speak('Good evening Sir')
    else:
        speak('Good night Sir')

    speak('Zeebo at your service. what can i do for you today')


def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1  # waits for one second as threshold if no input to microphone given
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
    server.login("kgssvak2@gmail.com", "kemddkhlcskoqehs")
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


if __name__ == "__main__":

    # wishme_()

    while True:
        query = input()

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

        elif 'send email' in query:
            try:
                speak('What should i send')
                content = takecmd()
                speak('who should i send the email')
                to = input('Enter the Reciever Email :')
                speak('sending :')
                speak(content)
                sendemail(to, content)
                speak('Email Sent Successfully')

            except Exception as e:
                print(e)
                speak('Sending failed')

        elif 'search in chrome' in query:
            speak('what should i search')
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = takecmd().lower()
            # takes the path to exe appends in url form with .com
            wb.get(path).open_new_tab(search + '.com')

        elif 'search youtube' in query:
            speak('what should i search')
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = takecmd().lower()
            # takes the path to exe appends in url form with .com
            speak('hear we go to youtube')
            wb.get(path).open_new_tab(
                'https://www.youtube.com/results?search_query=' + search)

        elif 'search google' in query:
            speak('what should i search')
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = takecmd().lower()
            # takes the path to exe appends in url form with .com
            speak('finding search results')
            speak('opening chrome to view results')

            wb.get(path).open_new_tab(
                'https://www.google.com/search?q=' + search)

        elif 'cpu' or ' battery' in query:
            cpu()
