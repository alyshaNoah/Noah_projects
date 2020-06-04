# Alysha Noah
# 05/18/2020
# Noah_text_analyzer.py
# Purpose: text analyzer that reads a file and outputs statistics about that file

from collections import Counter
file = open('play.txt', 'r')
wordCount = {}
for line in file:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
x = Counter(wordCount).most_common(20)
i = 1
for item in x:
    print('%i:' % i, item)
    i += 1
