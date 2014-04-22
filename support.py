"""
SUPPORT.PY

This file contains some related functions for the Besides Blocks lab.
We decided to separate these functions because they aren't strictly necessary
to make things work. If you're new to Python not all of this code will make
sense, but that's ok. Feel free to ask questions or check on Google if you're
curious.

"""
from twython import Twython

# this is a global reference to a file containing all the authentication keys
# The first line is a row of column titles
# rows 2-4 are alternate tokens for the pythonblocks account
# if there's a line 5, it's for a personal accout
TOKEN_FILE = 'keys.csv'

def fileToList(fileName):
    result = []

    file = open(fileName)

    # Grab first line of the file and split by ,
    firstRow = file.readline()
    firstRow = firstRow.strip()
    firstRow = firstRow.split(',')
    for col in firstRow:
        # [] turns col into a 1 item list
        result.append( [col] )

    # Add the remaining lines to the result list
    # turn each line of the file into a list
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        lineList = line.split(',')
        for item in range(len(lineList)):
            result[item].append(lineList[item])

    return result

def readToken(file, tokenName, number):
    for item in file:
        if item[0] == tokenName:
            return item[number]
    return 'KEY NOT FOUND'

def writeKeys(auth, tokenFile):
    # Manually build a string since dictionaries have no order
    s = auth['APP_KEY'] + ',' + auth['APP_SECRET'] + ',' + auth['OAUTH_KEY'] \
        + ',' + auth['OAUTH_SECRET'] + '\n'

    with open(tokenFile, 'a') as f:
        f.write(s)

def authenticateTwitter(usePersonal, keyNo):
    if usePersonal:
        return personalAuthentication()
    else:
        return authenticateBB(keyNo)

def personalAuthentication():
    pass

def authenticateBB(keyNo):
    pass