#!python3

import tweepy

#x.translate(non_bmp_map) for decode
import sys 
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#socks proxy
import socket
import socks
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket

#authenticate info
consumer_key = ""  
consumer_secret = ""  
access_token = ""  
access_token_secret = ""  

#set api object

#creat auth object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#set access token and access secret
auth.set_access_token(access_token, access_token_secret)
#incoming auth and creat api object
api = tweepy.API(auth)
#******************************************#


#TEST1 get timeline
timeline = api.home_timeline()
timelineList = []
for tweet in timeline:
    timelineList.append(tweet.text.translate(non_bmp_map))#x.translate(non_bmp_map) for decode

#TEST2 get specified account's tweets(20)
name = 'realdonloadtrump'
tweetCount = 20#number of tweets once time
specifiedTweets = api.user_timeline(id=name, count=tweetCount)
specifiedTweetsList = []
for tweet in specifiedTweets:
    specifiedTweetsList.append(tweet.text.translate(non_bmp_map))

#TEST3 search tweets with keyword
query = 'trump'#set keyword
language = 'en'#set language
keywordTweets = api.search(q=query, lang=language)
keywordTweetsList = []
for tweet in keywordTweets:
    keywordTweetsList.append(tweet.text.translate(non_bmp_map))

    
