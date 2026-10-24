import pariertts
import pipertts
from mayaos import Mayalogic

# Initialize AI and TTS engines
maya_brain = Mayalogic()
parler = pariertts.load("parler")
piper = pipertts.load("piper")

def connect_to_voice(text, engine="parler"):
    if engine == "parler":
        return parler.speak(text)
    elif engine == "piper":
        return piper.speak(text)
    return None

# Integration logic
while True:
    input_text = input("You: ")
    maya_response = maya_brain.reply(input_text)
    print(f"Maya: {maya_response}")
    connect_to_voice(maya_response)
