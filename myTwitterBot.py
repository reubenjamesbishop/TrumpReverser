import tweepy

#I have my keys here...

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Check if it's working
user = api.me()
print (user.name)

#Follow all the users following me
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)

#Get the tweet and reverse it
tweetList = api.user_timeline(screen_name = 'realDonaldTrump', count = 1)
tweet = tweetList[0]
#tweet = str(tweet.full_text)
tweet = str(tweet.text)
print(tweet)
reversedTweet = ''.join(reversed(tweet))
print(reversedTweet)

#Tweet it from my bot account
api.update_status(reversedTweet)
