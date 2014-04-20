from twython import Twython
import calendar
import simplehist

try:
    # four keys should be in the file KEYS.txt, each on its own line.
    # there should be an empty line at the end of the file.
    file = open("KEYS.txt")
    APP_KEY = file.readline()[0:-1] # strip off the trailing '\n' left by readline
    APP_SECRET = file.readline()[0:-1]
    OAUTH_TOKEN = file.readline()[0:-1]
    OAUTH_TOKEN_SECRET = file.readline()[0:-1]
    print OAUTH_TOKEN_SECRET
except:
    print "We couldn't find your KEYS.txt file."
    exit()
finally:
    file.close()

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# try:
#     file = open("ACCESS_TOKEN.txt")
#     ACCESS_TOKEN = file.read()
# except IOError:
#     file = open("ACCESS_TOKEN.txt", "w")
#     ACCESS_TOKEN = twitter.obtain_access_token()
#     file.write(ACCESS_TOKEN)
# finally:
#     file.close()

#twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

results = twitter.get("search/tweets", params={'geocode': '37.874718,-122.272539,3mi', 'count':'100', 'result_type':'recent'})
id = results['statuses'][len(results['statuses']) - 1]['id']

twitter.verify_credentials()
timeline = twitter.get_home_timeline(count = 20)

content = []
geo = []

michaels_tweets = twitter.get("statuses/user_timeline", params = {'count': '200', 'screen_name':'cycomachead'})
days = [item['created_at'][0:3] for item in michaels_tweets]
hist = simplehist.SimpleHist(days)
summary = hist.getHist()

print "Summary of Michael's Last 200 Tweets"
for day in calendar.weekheader(3).split(" "):
    print day, "*" * summary[day]





def store_results(results):
    for elem in results['statuses']:
        if elem['geo'] != None:
            content.append(elem['text'])
            geo.append(elem['geo'])
        

def print_summary(tweets_list):
    count = 0
    for elem in tweets_list:
        print elem['user']['screen_name'], ":", elem['user']['name']
        print elem['text']
        print elem['created_at']
        print elem['geo']
        print
        if elem['geo'] == None:
            count += 1

    print count
    print "--------------------"


#print_summary(results)
#results = twitter.get("search/tweets", params={'geocode': '37.874718,-122.272539,3mi', 'count':'20', 'result_type':'recent'})
#print_summary(results)
# """
# store_results(results)

# for i in range(300):
#     results = twitter.get("search/tweets", params={'geocode': '37.874718,-122.272539,3mi', 'count':'100', 'result_type':'recent', 'max_id': id})
#     id = results['statuses'][len(results['statuses']) - 1]['id']
#     store_results(results)
#     print str(i + 2) + " queries completed"

# count = 0
# #for i in range(len(content)):
# #    print content[i]
# #    print geo[i]
# #    print

# try:
#     file = open("data/geotags", "w")
#     for tag in geo:
#         file.write(str(tag['coordinates'][0]) + " " + str(tag['coordinates'][1]) + '\n')
# except IOError:
#     print "Error: unable to write to file data/geotags"
# finally:
#     file.close()

# try:
#     file = open("data/content", "w")
#     for text in content:
#         file.write(text.replace("\n", "   ").encode("utf-8") + '\n')
# except IOError:
#     print "Error: unable to write to file data/content"
# finally:
#     file.close()




# print count, " / ", len(geo)
# """
