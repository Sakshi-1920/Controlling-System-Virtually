import os 
import time
import wikipedia
import webbrowser
import requests
import wolframalpha
import datetime
import pyttsx3
from AppOpener import open, close
import speech_recognition as sr
import pyjokes
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from datetime import date

class Virtual_Assistant:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1920x1080+0+0') 
        self.root.title('VIRTUAL SYSTEM CONTROLLER')
        
        title_label=Label(self.root,text="AI VIRTUAL ASSISTANT",font=("times new roman",25,"bold"),bg="#FFD700",fg="black")
        title_label.place(x=0,y=0,width=1920,height=55)
        
        img=Image.open(r'C:\Users\SAKSHI SONAR\Desktop\FINAL YEAR PROJECT\IMAGES\10.jpg')
        img=img.resize((1920,760),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        flabel=Label(self.root,image=self.photoimg)
        flabel.place(x=0,y=65,width=1920,height=920)
        
        title1_button=Button(self.root,text="AI VIRTUAL ASSISTANT",command=self.assistant,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="black")
        title1_button.place(x=800,y=930,width=350,height=45)
        
    def assistant(self):
        print('LOADING YOUR PERSONAL A.I ASSISTANT')
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty("voice",'voices[0].id')
        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("Good Morning")
                print("Good Morning")
            elif hour>=12 and hour<=16:
                speak("Good Afternoon")
                print("Good Afternoon")
            elif hour>16 and hour<22:
                speak("Good Evening")
                print("Good Evening")
            else:
                speak("It was a good day. Good Night")
                print("It was a good day. Good Night")

        def takeCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)

            try:
                print("Recognizing...")
                statement = r.recognize_google(audio, language='en-in')
                print(f"User Said: {statement}\n")

            except Exception as e:
                print(e)
                print("Please can you say it again..")
                return "None"

            return statement

        speak("LOADING YOUR VIRTUAL ASSISTANT")
        wishMe()  
        while True:
            speak("How can I help you?")
            statement=takeCommand().lower()
            if statement == 0:
                continue
            if "thank you" in statement or "stop" in statement:
                speak("Virtual Assistant is shutting down, GOOD BYE")
                print("Virtual Assistant is shutting down, GOOD BYE")
                break
            
            if 'search' in statement:
                speak("Searching Wikipedia...")
                print("Searching Wikipedia...")
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=2)
                speak("According to wikipedia...")
                print(results)
                speak(results)

            
            elif "open youtube" in statement:
                speak("Opening Youtube")
                print("Opening Youtube")
                webbrowser.open_new_tab("https://www.youtube.com")
                time.sleep(5)
            
            elif "open google" in statement:
                speak("Opening google")
                print("Opening google")
                webbrowser.open_new_tab("https://www.google.com")
                time.sleep(5)
            
            elif "open gmail" in statement:
                speak("Opening gmail")
                print("Opening gmail")
                webbrowser.open_new_tab("https://mail.google.com")
                time.sleep(5)  
            
            elif "weather" in statement:
                api_key = "8ef61edcf1c576d65d836254e11ea420"
                base_url = 'https://api.openweathermap.org/data/2.5/weather?'
                speak("What is the city name?")
                city_name = takeCommand()
                complete_url = base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidity = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak("the temperature in kelvin units is " + str(current_temperature) + "\nhumidity in percentage is" +
                        str(current_humidity)+"\n weather descripton" + str(weather_description))
                    print("the temperature in kelvin units is " + str(current_temperature) + "\nhumidity in percentage is" +
                        str(current_humidity)+"\n weather descripton" + str(weather_description))
                else:
                    speak("city not found")
                    print("city not found")
            
            elif "time" in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is{strTime}")
                
            elif "date" in statement:
                today = date.today()
                d2 = today.strftime("%B %d, %Y")
                print("Today's date is =", d2)
                speak("Today's date is" + d2)

            elif "who are you" in statement or "what can you do" in statement:
                speak("Iam Your personal assistant. I can perform the following task like opening YouTube, Gmail, Google chrome and stack overflow. Also, I can Predict current time, take a photo, search Wikipedia to abstract required data, predict weather in different cities, get top headline news from Times of India and can answer computational and geographical questions too.")
                print("Iam Your personal assistant. I can perform the following task like opening YouTube, Gmail, Google chrome and stack overflow. Also, I can Predict current time, take a photo, search Wikipedia to abstract required data, predict weather in different cities, get top headline news from Times of India and can answer computational and geographical questions too.")
                
            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I am made by JCE students")
                print("I am made by JCE students")
            
            elif "open stackoverflow" in statement:
                speak("Opening stack overflow")
                print("Opening stack overflow")
                webbrowser.open_new_tab("https://stackoverflow.com")
                time.sleep(5)
                
            elif "news" in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak("Here are some headlines from times of India for you")
                time.sleep(5)
                
            elif "ask" in statement:
                speak("My versions are still under upgradation progress to enable more cool features. But you can try asking me computational and geographical questions now. Sure, I will answer those. What do you want to ask?")
                question = takeCommand()
                app_id = "R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)
                
            elif 'shutdown' in statement:
                os.system('shutdown /p /f')
                
            elif 'tell me some joke' in statement:
                Myjoke = pyjokes.get_joke(language="en", category="neutral")
                print(Myjoke)
                speak(Myjoke)

            elif 'open'+'' in statement:  
                app_name = statement.replace("open ","").strip()
                os.system(app_name)
            
            elif 'close'+'' in statement:
                app_name = statement.replace("close ","").strip()
                close(app_name, match_closest=True, output=False)
                print('Closing ' + app_name)

            elif 'start virtual keyboard' in statement:
                os.startfile('C:/Users/SAKSHI SONAR/Desktop/FINAL YEAR PROJECT/dist/vkeyboard/vkeyboard.exe')
            
            elif 'start virtual mouse' in statement:
                os.startfile('C:/Users/SAKSHI SONAR/Desktop/FINAL YEAR PROJECT/start.bat')
                
if __name__ == '__main__':
    root=Tk()
    obj=Virtual_Assistant(root)
    root.mainloop()

