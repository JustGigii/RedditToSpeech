import praw
import pyttsx3
import os
import string
from config import DevAuth


def loadstories():
    # load all identity
    dev = DevAuth()
    # Initialize Reddit API credentials
    reddit = praw.Reddit(
        client_id=dev.CLIENT_ID,
        client_secret=dev.CLIENT_SECRET,
        user_agent=dev.USER_AGENT,
    )

    # Get the most recent post from a subreddit
    subreddit = reddit.subreddit("stories")

    # Loop through recent posts until a valid post is found
    for post in subreddit.hot(limit=None):
        # Check if post title is between 35-90 characters and has punctuation marks
        length = len(post.selftext.split(" "))
        if length >= 35 and length <= 90:
            has_punctuation = False
            for char in post.selftext:
                if char in string.punctuation:
                    has_punctuation = True
                    break
            if has_punctuation:
                # Check if post title has already been saved as an audio file
                folder_name = "_".join(post.title.split()[:5])
                if not os.path.exists(os.path.join("recordings", folder_name)):
                    break

    # Print information about the selected post
    print("Selected post: {}".format(post.title))

    # Initialize the pyttsx3 text-to-speech engine
    engine = pyttsx3.init()

    # Set the rate of speech (words per minute)
    engine.setProperty("rate", 200)

    # Choose the voice to use
    voices = engine.getProperty("voices")
    voice = voices[0]
    print("Using voice: {}".format(voice.name))

    # Set the voice to use
    engine.setProperty("voice", voice.id)

    # Create the output directory if it doesn't exist
    if not os.path.exists("recordings"):
        os.makedirs("recordings")

    # Create a folder_name for the recording
    folder_name = "_".join(post.title.split()[:5])
    os.makedirs(os.path.join("recordings", folder_name))
    print("Saving to folder: {}".format(folder_name))

    # Generate the text-to-speech audio
    text = post.title + "." + post.selftext.replace("\n", " ")
    text_with_breaks = ""
    for char in text:
        text_with_breaks += char + ("\n" if char in [".", "?", ",", "!"] else "")
    lastword = text_with_breaks[0]
    fainal_text = ""
    for char in text_with_breaks:
        if not (lastword == "\n" and char == " "):
            fainal_text += char
        lastword = char

    with open(
        os.path.join("recordings", folder_name, "script.txt"), "w", encoding="utf-8"
    ) as f:
        f.write(fainal_text)
    print("Generating audio for text: {}".format(fainal_text))
    engine.save_to_file(
        fainal_text, os.path.join("recordings", folder_name, "audio.wav")
    )

    engine.runAndWait()

    print("Finished!")
