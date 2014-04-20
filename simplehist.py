
class SimpleHist(object):
    
    def __init__(self, data):
        self.bins = {}
        for item in data:
            if item in self.bins:
                self.bins[item] += 1
            else:
                self.bins[item] = 0
    def getHist(self):
        return self.bins


    
