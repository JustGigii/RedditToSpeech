import re
from pydub import AudioSegment
from pydub.silence import *
import os
rate = 220
with open(r'C:\Users\try\Desktop\proj\recordings\The_Story_of_The_Amba\script.txt', "r") as f:
    script = f.read()
AudioSegment.ffmpeg = 'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\ffmpeg.exe'
AudioSegment.converter = 'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\ffmpeg.exe'

audio = AudioSegment.from_wav(
    r"C:\Users\try\Desktop\proj\recordings\The_Story_of_The_Amba\audio.wav", "wav")

# script = script.replace('\n', '')
# sentences = re.split(r'[.!?]+', script)
# sentences = [sentence.strip() for sentence in sentences]
# sentences = [sentence for sentence in sentences if sentence]
# # print(sentences)
# # word_durations = (5 / 165) * 60
# sec = 0
# subtitle = {}
# for i in sentences:
#     subtitle[sec] = (i, (len(i.split(" ")) / rate) * 60)
#     sec += (len(i.split(" ")) / rate) * 60
#     subtitle[sec] = ('', 0.5)
#     sec = sec+0.5
# for i in subtitle:
#     sub, dab = subtitle[i]
#     print(i, dab, end="\n")


def subtitle(script):
    script = script.replace('\n', '')
    sentences = re.split(r'[.!?,]+', script)
    sentences = [sentence.strip() for sentence in sentences]
    sentences = [sentence for sentence in sentences if sentence]
    # print(sentences)
    # word_durations = (5 / 165) * 60
    sec = 0.11
    subtitle = {}
    subtitle[0] = (' ', 0.8)
    for i in sentences:
        subtitle[sec] = (i, (len(i.split(" ")) / rate) * 60)
        sec += (len(i.split(" ")) / rate) * 60
        subtitle[sec] = (' ', 0.8)
        sec = sec+0.8
    return subtitle


# answer = subtitle(script)
# for i in answer:
#     sub, dab = answer[i]
#     print(i, dab, end="\n")

audio_chunks = detect_nonsilent(audio, min_silence_len=500, silence_thresh=-40)
print(audio_chunks)
