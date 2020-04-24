import time
import sys
import tweepy
from pprint import pprint

from qzap_bot import get_tweet

LOCAL_DEVELOPMENT = True

if LOCAL_DEVELOPMENT:
    from secrets import *

else:
    from os import environ

    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tweet_text = get_tweet()

media_ids = []
for i in range(3):
    filename = './media/zine_{}.jpg'.format(i)
    print(filename)
    res = api.media_upload(filename)
    media_ids.append(res.media_id)

api.update_status(status=tweet_text, media_ids=media_ids)

# TODO:
# - handle errors and missing PDFS
# - get twitter creds working
# - deploy
# - write README
