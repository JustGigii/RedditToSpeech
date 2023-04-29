import re
rate = 165
# with open(r'C:\Users\try\Desktop\proj\recordings\I_want_to_write_books\script.txt', "r") as f:
#     script = f.read()
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
#     subtitle[sec] = ('', 1)
#     sec = sec+1
# print(subtitle)


def subtitle(script):
    script = script.replace('\n', '.')
    sentences = re.split(r'[.!?,]+', script)
    sentences = [sentence.strip() for sentence in sentences]
    sentences = [sentence for sentence in sentences if sentence]
    # print(sentences)
    # word_durations = (5 / 165) * 60
    sec = 0
    subtitle = {}
    for i in sentences:
        subtitle[sec] = (i, (len(i.split(" ")) / rate) * 60)
        sec += (len(i.split(" ")) / rate) * 60
        subtitle[sec] = (' ', 0.75)
        sec = sec+0.75
    return subtitle
