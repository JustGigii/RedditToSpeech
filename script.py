import re
from pydub import AudioSegment
from pydub.silence import *

rate = 220
with open(
    r"C:\Users\try\Desktop\proj\recordings\The_Story_of_The_Amba\script.txt", "r"
) as f:
    script = f.read()
AudioSegment.ffmpeg = "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\ffmpeg.exe"
AudioSegment.converter = "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\ffmpeg.exe"


audiopath = r"C:\Users\try\Desktop\proj\recordings\The_Story_of_The_Amba\audio.wav"


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


def subtitle(script, audiopath):
    audio = AudioSegment.from_wav(audiopath, "wav")
    audio_chunks = detect_nonsilent(audio, min_silence_len=500, silence_thresh=-40)
    script = script.replace("\n", "")
    sentences = re.split(r"[.!?,]+", script)
    sentences = [sentence.strip() for sentence in sentences]
    sentences = [sentence for sentence in sentences if sentence]
    # print(sentences)
    # word_durations = (5 / 165) * 60
    subtitledict = {}
    index = 0
    for sentence in sentences:
        durablity = (audio_chunks[index][1] - audio_chunks[index][0]) / 1000
        subtitledict[(audio_chunks[index][0]) / 1000] = sentence, durablity
        index += 1
    return subtitledict


# answer = subtitle(script, audiopath)
# for i in answer:
#     sub, dab = answer[i]
#     print(i, dab, end="\n")
# print(answer)
