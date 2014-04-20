import turtle as t
from random import randint, choice

COLORS = ["blue", "pink", "orange", "green", "yellow", "purple", "black"]

def drawCloud(words):
    t.reset()
    t.up()
    t.hideturtle()
    topCounts = sorted([words[word] for word in words.keys() if len(word) > 3])[0:20]
    largest = max(topCounts)
    normalized_counts = {}
    for item in words.keys():
        newSize = int(float(words[item]) / largest * 48)
        if words[item] in topCounts:
            normalized_counts[item] = newSize
    
    size = t.screensize()
    width_dim = (-1 * size[0] / 2, size[0] / 2)
    height_dim = (-1 * size[1] / 2, size[0] / 2)
    
    for item in normalized_counts.keys():
        t.goto(randint(*width_dim), randint(*height_dim))
        t.color(choice(COLORS))
        try:
            t.write(item, font = ("Arial", int(normalized_counts[item]), "normal"))
            # try:
        #     t.write(unicode(item, errors = 'ignore'), font = ("Arial", int(normalized_counts[item]), "normal"))
        except:
            try:
                t.write(unicode(item, errors = 'ignore'), font = ("Arial", int(normalized_counts[item]), "normal"))
            except:
                pass
            #except:
            #    t.write(decode('utf-8'), font = ("Arial", int(normalized_counts[item]), "normal"))
            
    
 

