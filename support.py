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



# This will hold all the special values which twitter needs to authenticate
# with this 'application' and for a specific account.
authentication_keys = {'APP_KEY' : '0juLuqWg02dUyQaH7mwtfr33x',
    'APP_SECRET' : '5hXK97BFEl5MLteUaVLTqUHjIe1SgYHWHkfdoYixpxFsnHypaz',
    'OAUTH_KEY' : '', 'OAUTH_SECRET' : ''}

def authenticateTwitter(usePersonal, keyNo):
    if usePersonal:
        personalAuthentication()
    else:
        authenticateBB(keyNo)

    # shorthand, for the sake of laziness
    auth = authentication_keys

    # create a twitter object to use for the rest of the project
    return Twython(auth['APP_KEY'], auth['APP_SECRET'],
                      auth['OAUTH_KEY'], auth['OAUTH_SECRET'])

def personalAuthentication():
    allKeys = fileToList(TOKEN_FILE)
    if len(allKeys[0]) > 4: # we've already saved the personal token
        for key in authentication_keys.keys():
            # The 4th item of the list of key data will be the key for a
            # personal account
            authentication_keys[key] = readToken(allKeys, key, 4)
    else:
        twitter = Twython(authentication_keys['APP_KEY'],
            authentication_keys['APP_SECRET'])
        auth = twitter.get_authentication_tokens()
        import webbrowser
        # Open a webpage with your twitter code
        webbrowser.open(auth['auth_url'])
        try:
            auth_pin = input("Please enter the code from twitter: ")
        except: # python 2.7
            auth_pin = raw_input("Please enter the code from twitter: ")

        # These are temporary, part of the overall authentication process
        OAUTH_TOKEN = auth['oauth_token']
        OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

        twitter = Twython(authentication_keys['APP_KEY'],
            authentication_keys['APP_SECRET'], OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        final_step = twitter.get_authorized_tokens(auth_pin)

        authentication_keys['OAUTH_KEY'] = final_step['oauth_token']
        authentication_keys['OAUTH_SECRET'] = final_step['oauth_token_secret']

        writeKeys(authentication_keys, TOKEN_FILE)

def authenticateBB(keyNo):
        # this grabs the "keys" which are the first part of a mapping in a dict.
        for key in authentication_keys.keys():
            # save the appropriate key from the file.
            authentication_keys[key] = readToken(allKeys, key, keyNo)
