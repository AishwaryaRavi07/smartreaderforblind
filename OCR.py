import pytesseract
import cv2
from PIL import Image
from gtts import gTTS
import os
import time
language = 'en'
import pyttsx3

def onWord(name, location, length):
    global string_spoken
    string_spoken = string[len(string_spoken):len(string_spoken) + length]
    print(string_spoken, end='', flush=True)

engine = pyttsx3.init()
engine.connect('started-word', onWord)

image = cv2.imread('saved_img.jpg')
string = pytesseract.image_to_string(image)
print(string)

#voices = engine.getProperty('voices') 
#engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
print (rate)
engine.setProperty('rate', 125) 

engine.say(string)
engine.runAndWait()

# get the string
#string = pytesseract.image_to_string(image)
#string =" please add your word"
#print(string)
# print it
#myobj = gTTS(text=string, lang=language, slow=False)
#myobj.save("welcome.mp3")
#os.system("cvlc welcome.mp3 &")
#print(string)
#time.sleep(1)
