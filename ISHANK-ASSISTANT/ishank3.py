import speech_recognition as aa
import pyttsx3 as tts
import pywhatkit
import wikipedia
from datetime import datetime
import smtplib
import pyjokes
import random
from sympy import sympify, symbols

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
            print("Ishank: Hi, I am Ishank, your virtual assistant. What would you like me to do?")
            talk("Hi, I am Ishank, your virtual assistant. What would you like me to do?")
            print("Ishank: Here are some commands you can use:")
            print("1. Play a song.")
            print("2. Search on Wikipedia.")
            print("3. What is the date today?")
            print("4. Open a website.")
            print("5. Send an email.")
            print("6. Perform a math calculation.")
            print("7. Tell me a joke.")
            print("8. Exit")
            print("Ishank: Please speak your command.")
            speech = listener.listen(origin, timeout=10)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()

            return instruction

    except aa.WaitTimeoutError:
        return None

    except:
        return None

def open_website(website):
    pywhatkit.search(website)

def send_email():
    # Set up your email configuration
    # Note: This is a basic example and requires email account details
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'

    talk("Ishank: Who is the recipient?")
    recipient = input("Recipient: ")
    talk(f"Ishank: What should I say to {recipient}?")
    content = input("Content: ")

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, content)
            talk("Ishank: Email sent successfully.")
            display_text("Ishank: Email sent successfully.")
    except Exception as e:
        talk("Ishank: Sorry, I couldn't send the email.")
        display_text(f"Ishank: Sorry, I couldn't send the email. Error: {str(e)}")

def perform_math_calculation():
    talk("Ishank: What math calculation would you like me to perform?")
    expression = input_instructions()

    try:
        # Use sympify to convert the string expression to a sympy expression
        expression = expression.replace('times', '*').replace('by', '/').replace('plus', '+').replace('minus', '-')
        sympy_expression = sympify(expression)
        
        # Use evalf() to get a numerical result
        result = sympy_expression.evalf()

        talk(f"Ishank: The result of {expression} is {result}.")
        display_text(f"Ishank: The result of {expression} is {result}.")
    except Exception as e:
        talk("Ishank: Sorry, I couldn't perform the math calculation.")
        display_text(f"Ishank: Sorry, I couldn't perform the math calculation. Error: {str(e)}")

# The rest of the code remains unchanged

def tell_joke():
    joke = pyjokes.get_joke()
    talk(f"Ishank: {joke}")
    display_text(f"Ishank: {joke}")

def play_ishank():
    while True:
        instruction = input_instructions()

        if instruction is None:
            continue

        display_text("User: " + instruction)

        if 'play' in instruction:
            song = instruction.replace('play', '')
            talk("Ishank: Playing " + song)
            pywhatkit.playonyt(song)

        elif 'search' in instruction or 'who is' in instruction:
            search_query = instruction.replace('search', '').replace('who is', '')
            try:
                information = wikipedia.summary(search_query, sentences=3)
                display_text("Ishank: According to Wikipedia, " + information)
                talk("According to Wikipedia, " + information)
            except wikipedia.exceptions.DisambiguationError as e:
                display_text(f"Ishank: There are multiple results for {search_query}. Please be more specific.")
                talk(f"There are multiple results for {search_query}. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                display_text(f"Ishank: Sorry, I couldn't find any information on {search_query}.")
                talk(f"Sorry, I couldn't find any information on {search_query}.")

        elif 'date' in instruction and 'today' in instruction:
            today = datetime.now().strftime("%A, %B %d, %Y")
            talk(f"Ishank: Today's date is {today}.")
            display_text(f"Ishank: Today's date is {today}.")

        elif 'open' in instruction and 'website' in instruction:
            website = instruction.replace('open', '').replace('website', '').strip()
            open_website(website)

        elif 'send email' in instruction:
            send_email()

        elif 'perform math calculation' in instruction:
            perform_math_calculation()

        elif 'tell me a joke' in instruction:
            tell_joke()

        elif 'exit' in instruction:
            talk("Ishank: Goodbye! Have a great day.")
            break

        else:
            display_text("Ishank: I'm sorry, I didn't understand that command. Please try again.")

if __name__ == "__main__":
    play_ishank()
