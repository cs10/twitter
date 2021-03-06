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
# the wordcloud file for this lab
import wordcloud

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

def getTimestamp(tweet):
    return "YOUR CODE HERE"

def getScreenName(user):
    return user['screen_name']

def getUserID(user):
    return user['id']

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
# PART 2 -- Followers
def getFollowers():
    # Returns a dictionary which contains a list of users
    # This list is pretty ugly, honesty.
    # Follow the example about make it print a list of
    # @username
    return twitter.get_friends_list()['users']

def followUser(userID):
    # Fix this function to follow a particular user. To follow someone you need to know their userID
    # The function you need to call is create_friendship() and it has an id
    # parameter

    # YOUR CODE HERE
    return


###############################################################################
# PART 3 -- Post a Tweet
def postStatus(s):
    twitter.update_status(status=s)

###############################################################################
# PART 4 -- Word Clouds

def join(tweetList):
    """
    Take in a list of tweets, and output a list of words.
    """
    # YOUR CODE HERE
    return

def buildCount(words):
    """
    Take in a list of words and return a dictionary or counts
    """
    # YOUR CODE HERE
    return