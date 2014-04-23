import turtle as t
import random

COLORS = ["blue", "pink", "orange", "green", "yellow", "purple", "black"]

def drawCloud(words, num = 20):
    """ Draws a wordcloud with 20 random words, sized by frequency found in 
    the WORDS dictionary. """
    t.reset()
    t.up()
    t.hideturtle()
    topCounts = sorted([words[word] for word in list(words.keys()) if len(word) > 3])
    largest = topCounts[0]
    normalized_counts = {}
    for item in list(words.keys()):
        if len(item) > 3:
            newSize = int(float(words[item]) / largest * 24)
            normalized_counts[item] = newSize
    
    size = t.screensize()
    width_dim = (int(-1 * size[0] / 1.5), int(size[0] / 2))
    height_dim = (int(-1 * size[1] / 1.5), int(size[1] / 1.5))
    

    for item in random.sample(list(normalized_counts.keys()), num):
        t.goto(random.randint(*width_dim), random.randint(*height_dim))
        t.color(random.choice(COLORS))
        try:
            t.write(item, font = ("Arial", int(normalized_counts[item]), "normal"))
        except:
            try:
                t.write(str(item, errors = 'ignore'), font = ("Arial", int(normalized_counts[item]), "normal"))
            except:
                pass
            
    
 

