#Twitterbot

This is a script to run a Twitter bot that uses the Twitter Search API to find a tweet matching a search query of your choosing, and automatically replies to the found tweet from your account with a pre-set response.

##Setup

1. Create a twitter account to post to.
2. Add a phone number to the account profile. This is required by Twitter to create an application. Twitter only allows a phone number to be associated with one account, use a Google Voice number or similar if your number is already associated with your primary account.
3. Sign in to https://apps.twitter.com/ with this new account and create a new application. Set the permissions to "Read and Write".
4. Make a copy of the `local_settings_example.py` file and name it `local_settings.py`.
5. Get the Consumer Key, Consumer Secret, Access Token, and Access Token Secret from the Twitter Application Management page and add them to the appropriate places in `local_settings.py`.
6. Replace `[Your Search Query]` with the string you want to search for in `SEARCH_QUERY` (make sure to use [url encoding](http://en.wikipedia.org/wiki/Percent-encoding)).
7. Replace `[Your Response]` in `RESPONSE` with the response you want your bot to make.
8. This script requires [python-twitter](https://github.com/bear/python-twitter), available with `pip install python-twitter`.

##Running the script

From the command line, go to the project's root directory and run the script with `python twitterbot.py`.

##Issues

The script doesn't store data about what you've previously tweeted, so the bot will only respond to the first tweet it finds with your search query. If there are no new tweets matching the search query the next time you run the script, it will reply to the same tweet it previously found.

Possible fixes: storing a record of previous responses in a database, or using the Twitter API to query your own timeline and skip over tweets previously responded to.

##Credit

This began as a modified version of Tom Meagher's [heroku_ebooks](https://github.com/tommeagher/heroku_ebooks).