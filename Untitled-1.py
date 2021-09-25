import pyttsx3  
# initialize Text-to-speech engine  
engine = pyttsx3.init()  
# convert this text to speech  


voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    text = "Chinki hardik ki dost hai"  
    engine.setProperty("rate", 100)  
engine.say(text)  
# play the speech  
engine.runAndWait()  