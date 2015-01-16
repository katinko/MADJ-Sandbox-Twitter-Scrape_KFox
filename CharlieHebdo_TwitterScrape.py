import twitter
import json
import sys
import csv
 
# == OAuth Authentication ==
# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "Keys and tokens")
 # PUT YOUR KEYS AND SECRETS IN HERE, IT WONT WORK WITHOUT YOUR KEYS FROM TWITTER !!!!!
consumer_key="xxxx"
consumer_secret="xxxx"
 
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="xxxx"
access_token_secret="xxxx"
 
auth = twitter.oauth.OAuth(access_token, access_token_secret,consumer_key, consumer_secret)
twitter_api = twitter.Twitter(auth=auth)

csvfile = open('CharlieHebdo.csv', 'a')
csvwriter = csv.writer(csvfile)

# Query terms
q = '#CharlieHebdo' # Comma-separated list of terms, start with something busy to test your script, then once you know its working put your hashtags in, max 400 tags
print >> sys.stderr, 'Filtering the public timeline for track="%s"' % (q,)
# Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
# See https://dev.twitter.com/docs/streaming-apis
stream = twitter_stream.statuses.filter(track=q)
for tweet in stream:
	print json.dumps(tweet, indent=1)
	print tweet['text'].encode('utf-8')
	print tweet['user']['screen_name'].encode('utf-8')
	print tweet['created_at'].encode('utf-8')
	print tweet['coordinates']
	
	text = tweet['text'].encode('utf-8')
	screen_name = tweet['user']['screen_name'].encode('utf-8')
	created_at = tweet['created_at']
	coordinates = tweet['coordinates']
	csvwriter.writerow([text, screen_name, created_at, coordinates])	