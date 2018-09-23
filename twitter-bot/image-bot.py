#the image bot
import tweepy as tp 
import os
import time

#twitter credentials
consumer_key = 'XX7OqHQiZ6NqgjVuE7NGp567m'
consumer_key_secret = 'eOrGWscbQV68fhYrNkA7rF9qBvnMQofIQbodsaN0pz9DnCD8Kl'
access_token = '1043616581144600576-ZtnFYctkMwAaQF2Kh8bMeouHlEpxl1'
access_token_secret = 'mm3SUwza4WL3te1ODJ24HK2DkdqFn3lFQhFRUOrHRlfb9'

#login to twitter
auth = tp.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth)

#iterate over pictures in pictures directory
os.chdir('pictures')
for image in os.listdir('.'):
	api.update_with_media(image)
	time.sleep(10)