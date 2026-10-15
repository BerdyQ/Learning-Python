import os
import tweepy
from tweepy import OAuthHandler
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', 'API-Keys', '.env') # Path to the correct .env file
load_dotenv(env_path) # Used to read the info from the env file from the path specified above

print(os.getenv("X_consumer_key") is not None)

# Initialized the Tweepy client with Twitter API credentials
client = tweepy.Client(
    consumer_key=os.getenv("X_consumer_key"),
    consumer_secret=os.getenv("X_consumer_secret"),
    access_token=os.getenv("X_access_token"),
    access_token_secret=os.getenv("X_access_token_secret")
)

myUser = client.get_me()
print("Logged in as:", myUser.data.username)
my_Tweets = client.get_users_tweets(id=myUser.data.id, max_results=5, user_auth=True)
for tweet in my_Tweets.data or []:
    print(tweet.text)