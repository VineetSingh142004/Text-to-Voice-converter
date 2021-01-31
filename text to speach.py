from gtts import gTTS 
import os
f=open(r"talking to the moon.txt","r")
a=f.read()
print(a)
language = 'en'
speech = gTTS(text = a, lang = language, slow = False)
speech.save("text.mp3")
os.system("start text.mp3")
