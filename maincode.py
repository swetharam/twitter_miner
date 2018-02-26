import tweepy
from textblob import TextBlob
consumer_key= 'Quo2d5FNN6F9LNwqOExTufMxR'
consumer_secret='qKHT8wy8PGrf7NcsONuUtk0RWhnvCrYbNp6NPqFOJbR4ZQldsT'

access_token='914577085347323906-YtVrpvFXrUZHt5v6rTdnl0tr6KY0cjs'
access_token_secret='rZzCmPxP5ZS8FNfXt4MT3QAzuAfFPCOeSmDx44XaaEahs'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api=tweepy.API(auth)

public_tweets=api.search('sridevi')

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)