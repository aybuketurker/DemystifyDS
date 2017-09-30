
import tweepy 
import csv

access_key = "get this from TWIITER "
access_secret = "get this from TWIITER"
consumer_key = "7get this from TWIITER"
consumer_secret = "get this from TWIITER"



def get_all_tweets(query):
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#request for most recent tweets
	new_tweets = api.search(q = query)
	
	#most recent tweets
	alltweets.extend(new_tweets)
	
	#id of the oldest tweet 
	oldest = alltweets[-1].id - 1
	
	#keep getting tweets until there are no tweets left
	while len(new_tweets) > 0:
		
		new_tweets = api.search(q = query, max_id=oldest)		
		alltweets.extend(new_tweets)	
		oldest = alltweets[-1].id - 1
		

	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.user.location, tweet.retweet_count, tweet.place, tweet.lang, tweet.geo, tweet.user.description] for tweet in alltweets]


	#write the csv
	with open('new_metis_tweets02.csv', 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text", "user_location", "retweet_count", "place", "lang", "GEO", "user_description"])
		writer.writerows(outtweets)
	
	pass

if __name__ == '__main__':
	#pass the tweet hashtag you want 
	get_all_tweets("#DemystifyDS")