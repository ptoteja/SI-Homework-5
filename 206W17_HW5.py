import unittest
import tweepy
import requests
import json

## SI 206 - W17 - HW5
## COMMENT WITH:
## Name: Prashant Toteja
## Your section day/time: Thursday 6-7pm
## Any names of people you worked with on this assignment: 

######## 500 points total ########

## Write code that uses the tweepy library to search for tweets with a phrase of the user's choice (should use the Python input function), and prints out the Tweet text and the created_at value (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in between each of them, e.g.

## TEXT: I'm an awesome Python programmer.
## CREATED AT: Sat Feb 11 04:28:19 +0000 2017

## TEXT: Go blue!
## CREATED AT: Sun Feb 12 12::35:19 +0000 2017

## .. plus one more.

## You should cache all of the data from this exercise in a file, and submit the cache file along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets about "rock climbing", when we run your code, the code should use CACHED data, and should not need to make any new request to the Twitter API. 
## But if, for instance, you have never searched for "bicycles" before you submitted your final files, then if we enter "bicycles" when we run your code, it _should_ make a request to the Twitter API.

## The lecture notes and exercises from this week will be very helpful for this. 
## Because it is dependent on user input, there are no unit tests for this -- we will run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

## **** For 50 points of extra credit, create another file called twitter_info.py that contains your consumer_key, consumer_secret, access_token, and access_token_secret, import that file here, and use the process we discuss in class to make that information secure! Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information for an 'extra' Twitter account you make just for this class, and not your personal account, because it's not ideal to share your authentication information for a real account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these with variables rather than filling in the empty strings if you choose to do the secure way for 50 EC points
consumer_key = "HYpQBmSwCfPNa5Vl4NZQ0StPd" 
consumer_secret = "ZG7tpl1DJVTpKIFIkf4kd2zCJhSaRtnU1vmqh0HVHrFXnQi2Iw"
access_token = "832299683200516096-t1ls18VfpgvxX1AVQFjw0DXJronKP33"
access_token_secret = "8ZOWPQYO5ZJ7Il3TcyfEl3SaWB3bwFD7Ecnsgk8aWjIU8"
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # Set up library to grab stuff from twitter with your authentication, and return it in a JSON-formatted way

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except statement shown in class.
## 2. Write a function to get twitter data that works with the caching pattern, so it either gets new data or caches data, depending upon what the input to search for is. You can model this off the class exercise from Tuesday.
## 3. Invoke your function, save the return value in a variable, and explore the data you got back!
## 4. With what you learn from the data -- e.g. how exactly to find the text of each tweet in the big nested structure -- write code to print out content from 3 tweets, as shown above.


CACHE_FNAME = "cache_HW5.json"
try:
	cache_file_obj = open(CACHE_FNAME, 'r')
	cache_contents = cache_file_obj.read()
	CACHE_DICTION = json.loads(cache_contents)
	cache_file_obj.close()
except:
	CACHE_DICTION = {}

def get_twitterinfo():
	query = input("What tweets should we look for?")
	if query in CACHE_DICTION:
		print("Using cached data for", query)
		search_results = CACHE_DICTION[query]
	else:
		print("getting new data from the web for", query)  
		search_results = api.search(query, count = 3)
		CACHE_DICTION[query] = search_results
		f = open(CACHE_FNAME,'w')
		f.write(json.dumps(CACHE_DICTION))
		f.close()
	return search_results

##PART 4
tweet_data = get_twitterinfo()

toString = json.dumps(tweet_data)
toJsonAgain = json.loads(toString)


final_dict = {}
for i in toJsonAgain["statuses"]:
	final_dict[i['text']] = i['user']['created_at']
for k in final_dict:
	print("TEXT:", k)
	print("CREATED AT:", final_dict[k])
	print("\n")




#jsonformatter.org  -> beautify type cast to string  if unicode error

