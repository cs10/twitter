'''
This sets up TODO

'''
###############################################################################
# SETUP
###############################################################################
# Twython is an easy to use Python library for twitter
from twython import Twython
# We've provided this support file to do some of the heavy-lifting for you
from support import *

# We have 3 sets of keys setup incase of API limit troubles.
# If you have a problem with "API limits" try changing this number to 2 or 3.
key_number = 1

# Make this True if you would like to use you own twitter account for this
# lab. It will have you sign in and save your login info, to keys.csv
personal_account = True

twitter = authenticateTwitter(personal_account, key_number)
# This makes sure we can correctly access twitter
twitter.verify_credentials()
###############################################################################


###############################################################################
# PART 1 -- Getting A Timeline

###############################################################################
# PART 2 -- Post a Tweet
def postStatus(s):
    twitter.update_status(status=s)

###############################################################################
# PART 3 -- Trending Topics

###############################################################################
# PART 4 -- Word Clouds