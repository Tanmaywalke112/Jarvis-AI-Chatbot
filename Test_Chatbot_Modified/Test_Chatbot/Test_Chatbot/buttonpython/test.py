import speech_recognition as sr
import win32com.client
import webbrowser
import pyjokes
import pywhatkit
import openai
import os
import datetime
from AppOpener import open

import random


chatstr=""
def chat(prompt):
    import openai
    #todo: Add ur API key here
    apikey="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"
    openai.api_key = apikey

    global chatstr
    chatstr+=f"User:{prompt}\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": chatstr
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    chatstr+=f"Jarvis:{response['choices'][0]['message']['content']}\n"
    print(chatstr)
    say(response['choices'][0]['message']['content'])

def ai(prompt):
    import openai
    openai.api_key = "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"

    text=f"OpenAI response for Prompt:{prompt} \n **********************\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    #todo:wrap this is try catch for errors
    text += response["choices"][0]["message"]["content"]
    print(text)

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# while 1:
#     print("Enter the word you want to speak it out by Computer")
#     s = input()
#     speaker.Speak(s)


def say(text):
    speaker.Speak(text)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold= 0.6 #change setting of mike :ctrl+click on threshold
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language="en-in")# hi-in for hindi
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    import sys
    input_query="%s" % (sys.argv[1])
    
    say("Hello I am Jarvis AI")
    say("What can i do for you")
    while True:
        print("Listening...")
        # if(input_query!=""):
        #     print("taking text")
        #     query=input_query
        
        # else:
        #     print("taking voice")
        query = takeCommand()
        
        
        # say(query)

        if "Open Youtube".lower() in query.lower():
            say("Opening Youtube Sir...")
            webbrowser.open("https://www.youtube.com")
        elif "Open Google".lower() in query.lower():
            say("Opening Google Sir...")
            webbrowser.open("https://www.google.com")
        elif "Open Wikipedia".lower() in query.lower():
            say("Opening Wikepedia Sir...")
            webbrowser.open("https://www.wikipedia.com")
        elif "Play".lower() in query.lower():
            song = query.replace('play', '')
            say("Playing"+song+"song...")
            pywhatkit.playonyt(song)
        # to add a feature to play a specific song
        # elif "open music" in query:
        #     musicPath = r"C:\Users\Tanmay Walke\Desktop\tvari-hawaii-vacation-159069.mp3"
        #
        #     # subprocess.Popen([musicPath], shell=True)
        #     os.system(f"start {musicPath}")
        elif 'joke'.lower() in query.lower():
            joke = pyjokes.get_joke()
            print(joke)
            say(joke)

        elif "time".lower() in query.lower():
            time = datetime.datetime.now().strftime('%I:%M %p')  # string format of time in AM/PM format
            print(time)
            say('Current time is ' + time)
        elif "open" in query:
            app = query.replace('open', '')
            say('Opening' + app)
            open(app)

        elif "Using AI".lower() in query.lower():
            ai(prompt=query)

        elif "Done".lower() or "Exit".lower() in query.lower():
            exit()

        #todo: weather api,news api,etc.
        else:
            chat(prompt=query)

        # except Exception as e:
        #     say('Sorry i didnt get it ,please say the command again')
       
