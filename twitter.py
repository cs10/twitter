'''
This sets up TODO

'''
###############################################################################
###############################################################################
from twython import Twython
from support import *

# Make this True if you would like to use you own twitter account for this
# lab. It will have you sign in and save your login info, to keys.csv
personal_account = True

# We have 3 sets of keys setup incase of API limit troubles.
key_number = 1

# This will hold all the special values which twitter needs to authenticate
# with this 'application' and for a specific account.
authentication_keys = {'APP_KEY' : '0juLuqWg02dUyQaH7mwtfr33x',
    'APP_SECRET' : '5hXK97BFEl5MLteUaVLTqUHjIe1SgYHWHkfdoYixpxFsnHypaz',
    'OAUTH_KEY' : '', 'OAUTH_SECRET' : ''}

# decide which authentication keys to grab
# These files are included in support.py
allKeys = fileToList(TOKEN_FILE)


if personal_account:
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
else:
    # this grabs the "keys" which are the first part of a mapping in a dict.
    for key in authentication_keys.keys():
        # save the appropriate key from the file.
        authentication_keys[key] = readToken(allKeys, key, key_number)

# shorthand, for the sake of laziness
auth = authentication_keys

# create a twitter object to use for the rest of the project
twitter = Twython(auth['APP_KEY'], auth['APP_SECRET'],
                  auth['OAUTH_KEY'], auth['OAUTH_SECRET'])

print(key_number)
twitter.verify_credentials()
###############################################################################
###############################################################################

# FIXME use a try except for duplicate statuses
# twitter.update_status(status="I'm using Python to post this tweet! #CSROCKS")