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

def display_text(text):
    print(text)

def input_instructions():
    instruction = ""
    try:
        with aa.Microphone() as origin:
            talk("Ishank is listening. Speak now.")
            display_text("Ishank is listening. Speak now.")
            
            speech = listener.listen(origin, timeout=5)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "ishank" in instruction:
                instruction = instruction.replace("ishank", " ")

    except aa.WaitTimeoutError:
        return None

    except:
        pass
    
    return instruction

def play_ishank():
    while True:
        instruction = input_instructions()

        if instruction is None:
            continue

        display_text("User: " + instruction)

        if "play" in instruction:
            song = instruction.replace('play', "")
            talk("playing" + song)
            pywhatkit.playonyt(song)

        elif 'time' in instruction:
            current_time = datetime.datetime.now().strftime("%I:%M:%p")
            talk("Current time: " + current_time)

        elif 'date' in instruction:
            current_date = datetime.datetime.now().strftime("%d / %m / %Y")
            talk("Today's date: " + current_date)

        elif 'how are you' in instruction:
            talk("I am fine, how are you doing?")

        elif 'what is your name' in instruction:
            talk("My name is Ishank. I am your personal assistant. How can I help you?")

        elif 'who is' in instruction:
            human = instruction.replace('who is', '')
            try:
                information = wikipedia.summary(human, sentences=3)
                display_text("Ishank: According to Wikipedia, " + information)
                talk("According to Wikipedia, " + information)
            except wikipedia.exceptions.DisambiguationError as e:
                display_text(f"Ishank: There are multiple results for {human}. Please be more specific.")
                talk(f"There are multiple results for {human}. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                display_text(f"Ishank: Sorry, I couldn't find any information on {human}.")
                talk(f"Sorry, I couldn't find any information on {human}.")

        else:
            display_text("Ishank: Please repeat")

if __name__ == "__main__":
    play_ishank()
