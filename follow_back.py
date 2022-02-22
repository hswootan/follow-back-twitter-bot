import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        Break

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'name_of_user':
        follower.follow()
        print(f"Now You are following {follower.name}")
    else:
        print(f"You are already following {follower.name}")
