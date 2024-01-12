from gtts import gTTS   #importing GTTS module
import os
f=open(r"talking to the moon.txt","r") # opening text file in read mode
a=f.read()
print(a)
language = 'en'
speech = gTTS(text = a, lang = language, slow = False)
speech.save("text.mp3")
os.system("start text.mp3")
