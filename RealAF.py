import re
import sys
import twitter
import os
import psycopg2
import urlparse
#from datetime import datetime, timedelta
from local_settings import *

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

def connect():
	api = twitter.Api(consumer_key=MY_CONSUMER_KEY,
						consumer_secret=MY_CONSUMER_SECRET,
						access_token_key=MY_ACCESS_TOKEN_KEY,
						access_token_secret=MY_ACCESS_TOKEN_SECRET)
	
	return api

def find_tweets(api, search_query, max_id=None):
	found_tweet = []
	result = api.GetSearch(term=search_query)
	
	for tweet in result:
		tweet_id = tweet.id
		tweet_text = tweet.text
		tweet_user = tweet.user.screen_name
		break

	return tweet_id, tweet_text, tweet_user

def post_tweet(api, status_frame, tweet_id, tweet_text, tweet_user):
	status = status_frame % (tweet_user, tweet_text)
	
	api.PostUpdate(status, in_reply_to_status_id=tweet_id)

if __name__ == '__main__':
	search_query = SEARCH_QUERY
	status_frame = RESPONSE
	api = connect()
	tweet_id, tweet_text, tweet_user = find_tweets(api, search_query)
	status = status_frame % (tweet_user, tweet_text)
	
	sent_tweet = api.PostUpdate(status, in_reply_to_status_id=tweet_id)
	print sent_tweet.text.encode('utf-8')