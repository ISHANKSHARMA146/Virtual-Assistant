import speech_recognition as aa
import pyttsx3 as tts
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()


machine = tts.init()

def talk(text):
    machine.say(text)
machine.runAndWait()

def input_instructions():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "ishank" in instruction:
                instruction = instruction.replace("ishank", " ")
                print(instruction)
            

    except:
        pass
    return instruction                

def play_ishank():

    instruction = input_instructions()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime("%I:%M:%P")
        talk("current time" + time)


    elif 'date' in instruction:
        date = datetime.datetime.now().strftime("%d / %m / %Y")
        talk("Todays date" + date)

    elif 'how are you' in instruction:
        talk("I am fine , how are you doing?")

    elif 'what is your name' in instruction:
        talk("my name is Ishank , i am your personal assistant , how can i help you?")

    elif 'who is' in instruction:
        human = instruction.replace('who is', '')
        information = wikipedia.summary(human, 1)
        print(information)
        talk("information")
    
    else:
        talk("please repeat")

play_ishank()