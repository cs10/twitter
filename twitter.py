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
# BASIC FUNCTIONS
def getText(tweet):
    return "YOUR CODE HERE"

def getUser(tweet):
    return tweet['user']

def getScreenName(user):
    return user['screen_name']
    
def getTimestamp(tweet):
    return "YOUR CODE HERE"

###############################################################################
# PART 1 -- Getting A Timeline
# You can get a basic timeline of tweets by calling get_home_timeline
def displayTimeline():
    tweets = twitter.get_home_timeline()
    for tweet in tweets:
        print("@" + getScreenName(getUser(tweet)) + ": " + getText(tweet) + "\n")
        # Ammend this function to print more interesting properties.
        # Try simply looking at tweet.keys() to see what you have to work with.


###############################################################################
# PART 2 -- Post a Tweet
def postStatus(s):
    twitter.update_status(status=s)

###############################################################################
# PART 3 -- Trending Topics

###############################################################################
# PART 4 -- Word Clouds