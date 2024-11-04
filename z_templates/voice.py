import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: ", text)

        # Here, you can add logic to perform actions based on 'text'
        # For example, you can run commands or trigger specific functions.

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")