import wordcloud as w
import testing as t

#print  t.michaels_tweaets

freq = {}
for item in t.michaels_tweets:
    for word in item['text'].split(" "):
        if word in freq.keys():
            freq[word] += 1
        else:
            freq[word] = 1

w.drawCloud(freq)
