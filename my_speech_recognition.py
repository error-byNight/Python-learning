import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Record the audio input
with sr.Microphone() as source:
    print("Speak Something...")
    audio = r.listen(source)

# Recognize the audio input
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
