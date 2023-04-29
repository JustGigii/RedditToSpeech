import pyttsx3

# Initialize the pyttsx3 text-to-speech engine
engine = pyttsx3.init()

# Get all available voices
voices = engine.getProperty('voices')

# Print the name and ID of each voice
for voice in voices:
    print('Name: {}, ID: {}'.format(voice.name, voice.id))

    # Set the voice to the current voice
    engine.setProperty('voice', voice.id)

    # Speak a sample phrase
    engine.say('The quick brown fox jumps over the lazy dog')

    # Wait for the phrase to finish
    engine.runAndWait()