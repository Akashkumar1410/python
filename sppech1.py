import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print('You said:', command)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except Exception as e:
    print(f"An error occurred: {e}")
