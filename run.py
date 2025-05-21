import speech_recognition as sr
import re
import webbrowser

text = None

def browse_intent_mapping(text):
    if text == "open website":
        webbrowser.open("https://www.google.ca/")
    elif text == "open new tab":
        webbrowser.open_new_tab("https://www.google.ca/")
    elif text == "open new window":
        webbrowser.open_new("https://www.google.ca/")   
    else:
        print ("Unknown Intent")
        
def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print ("say smth")
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print (text)
                if text:
                    browse_intent_mapping(text)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            except KeyboardInterrupt:
                print ("Exiting")
                break

if __name__ == "__main__":
    recognize_speech()