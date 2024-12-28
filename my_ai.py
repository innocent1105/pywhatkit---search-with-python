import pywhatkit as kit
import pyttsx3

# Initialize the engine
engine = pyttsx3.init()
# Set the rate and volume
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
# Set a specific voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


searchText = (input("Enter your search text here : "))

result = kit.info(searchText, 5)

# result = "hello there"

# Speak the input text
engine.say(result)
engine.runAndWait()