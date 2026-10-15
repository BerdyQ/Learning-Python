import os
import tweepy
from dotenv import load_dotenv

load_dotenv() # Used to read the info from the env file

consumer_key = os.getenv("X_consumer_key")
consumer_secret = os.getenv("X_consumer_secret")
access_token = os.getenv("X_access_token")
access_token_secret = os.getenv("X_access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("v1.1 test is running")
for status in tweepy.Cursor(api.user_timeline, count=5).items(5):
    print(status.text)