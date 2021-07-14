import re

words = set()
while True:
    try:
        line = input()
        wordsList = list(map(lambda x: re.findall(r'[a-z]+', x.lower()), line.split()))

        wordsList = [ item for elem in wordsList for item in elem]
        words.update(wordsList)
    except EOFError:
        break

for word in sorted(words):
    if word:
        print(word)
