import pyttsx3
from TTS.api import TTS

# Initialize the pyttsx3 text-to-speech engine
# engine = pyttsx3.init()

# # Get all available voices
# voices = engine.getProperty("voices")

# # Print the name and ID of each voice
# for voice in voices:
#     print("Name: {}, ID: {}".format(voice.name, voice.id))

#     # Set the voice to the current voice
#     engine.setProperty("voice", voice.id)

#     # Speak a sample phrase
#     engine.say("The quick brown fox jumps over the lazy dog")

#     # Wait for the phrase to finish
#     engine.runAndWait()

model_name = TTS.list_models()[0]
tts = TTS(model_name)
print(tts.speakers)
# wav = tts.tts(
#     "This is a test! This is also a test!!",
#     speaker=tts.speakers[0],
#     language=tts.languages[0],
# )
