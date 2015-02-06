import twitter
from local_settings import *

def connect():
	api = twitter.Api(consumer_key=MY_CONSUMER_KEY,
						consumer_secret=MY_CONSUMER_SECRET,
						access_token_key=MY_ACCESS_TOKEN_KEY,
						access_token_secret=MY_ACCESS_TOKEN_SECRET)
	
	return api

def find_tweets(api, search_query):
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