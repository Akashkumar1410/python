import pyttsx3
engine=pyttsx3.init()
while True:
    engine.setProperty("rate", 110)
    answer=input(" Enter your text\n")
    if 'name'in answer:
        engine.say("my name is python")
    elif 'you doing' in answer:
        engine.say(" i am doing my work")



    #engine.say(answer)
    engine.runAndWait()