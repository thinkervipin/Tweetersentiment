import tweepy
from textblob import TextBlob

consumer_key='wXhyhgJN4HirSEYuRMWf7xZbC'
consumer_secret='MHVt8RicZYvN04BrocixpKJq9RJccobMqbG0D2t1mFRUgZ7eE8'

access_token='278004219-L8dY6srxkXqP2EDGVAzqO37QR2hAvizdPU9scEh9'
access_token_secret='KkgJHv4zSU4Ndg5M2IM1btBkSSyNJptj52xPcKgR4YiZ9'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api =tweepy.API(auth)

public_tweets =api.search('Modi')

for tweet in public_tweets:
  print(tweet.text)
  analysis =TextBlob(tweet.text)
  print(analysis.sentiment)
