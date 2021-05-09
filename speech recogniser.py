import speech_recognition as sr

print("setting all things ready....")
def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("lisning.....")
        r.pause_threshold=0.6
        audio=r.listen(source)
        print("recognising....")
        
    try:
         ask=r.recognize_google(audio,language='en-us')
         print(f"you said:{ask}")

    except Exception:
        print("sorry unable to recognise say that again...")
        return""
    return ask

command()
input("   ")
    
