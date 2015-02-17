#Twitterbot

This is a script to run a Twitter bot that uses the Twitter Search API to find a tweet matching a search query of your choosing, and automatically replies to the found tweet from your account with a pre-set response.

The Master branch is set up to run on your local machine. The Heroku branch is modified to run on the [Heroku](heroku.com) platform.

##Setup

1. Create a twitter account to post to.
2. Add a phone number to the account profile. This is required by Twitter to create an application. Twitter only allows a phone number to be associated with one account, use a Google Voice number or similar if your number is already associated with your primary account.
3. Sign in to https://apps.twitter.com/ with this new account and create a new application. Set the permissions to "Read and Write".
4. Get the Consumer Key, Consumer Secret, Access Token, and Access Token Secret from the Twitter Application Management page. Set them as the [environment variables](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps) used in `local_settings.py`.
6. Export the string you want to search for as the environment variable `SEARCH_QUERY` (make sure to use [url encoding](http://en.wikipedia.org/wiki/Percent-encoding)).
7. Export the response you want your bot to make as the environment variable `RESPONSE`.
8. This script requires [python-twitter](https://github.com/bear/python-twitter), available with `pip install python-twitter`.

##Database Setup
Twitterbot uses a PostgreSQL database to store the Twitter IDs that the bot has previously responded to.

In your database, create table `tweets` with column `user_mentions_id` of data type `bigint` to store the Twitter IDs.

`bigint` is required, as Twitter IDs are now larger than the range of the regular `int` data type.

The database module requires [psycopg2](https://github.com/psycopg/psycopg2), available with `pip install psycopg2`.

##Running the script locally

From the command line, go to the project's root directory and run the script with `python twitterbot.py`.

##Running the script remotely

See instructions in the Heroku branch.

##Issues

1. If another user (other than a user the bot originally responded to) manually RTs one of the bot's tweets, it is possible that the bot will respond again to this RT. To fix, it needs to skip over tweets in which previously-responded-to users are mentioned at all.

2. If there are no matching tweets in the 100 that are returned with the API search that are short enough to quote and haven't yet been responded to, it will raise `UnboundLocalError: local variable 'tweet_id' referenced before assignment`. The script should be modified to exit cleanly rather than raising an error in this situation.

##Credit

This began as a modified version of Tom Meagher's [heroku_ebooks](https://github.com/tommeagher/heroku_ebooks).
