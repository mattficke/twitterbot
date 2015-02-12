import twitter
from local_settings import *
import database

def connect():
    api = twitter.Api(consumer_key=MY_CONSUMER_KEY,
                        consumer_secret=MY_CONSUMER_SECRET,
                        access_token_key=MY_ACCESS_TOKEN_KEY,
                        access_token_secret=MY_ACCESS_TOKEN_SECRET)
    
    return api

def find_tweets(search_query):
    api = connect()
    result = api.GetSearch(term=search_query)
    previous_tweets = database.read()
    for tweet in result:
        if tweet.user.id in previous_tweets: continue
        if len(tweet.text) > 105: continue
        tweet_id = tweet.id
        tweet_text = tweet.text
        tweet_user = tweet.user.screen_name
        tweet_user_id = tweet.user.id
        return tweet_id, tweet_text, tweet_user, tweet_user_id

        break

def post_tweet(status, tweet_id):
    api = connect()
    
    api.PostUpdate(status, in_reply_to_status_id=tweet_id)

def main():
    search_query = SEARCH_QUERY
    status_frame = RESPONSE
    
    tweet_id, tweet_text, tweet_user, tweet_user_id = find_tweets(search_query)
    
    status = status_frame % (tweet_user, tweet_text)
    
    sent_tweet = post_tweet(status, tweet_id)
    
    database.write(tweet_user_id)

if __name__ == '__main__':
	main()