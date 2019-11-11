# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:35:47 2019

@author: Khusnul
"""
import pandas
import tweepy
from tweepy import OAuthHandler, Stream, StreamListener

consumer_key="avLu8KO8eVTBeiTttRXHsvU6r"
consumer_secret="dVTKCvMKfmvdk9Lu1Yv4Cn54AdGvompSAwBme0aFC2fLqPalJ9"
access_token="1098368194765414400-yMsWFbeVQ8Yzu7YO4vq0BjJoVzeSXs"
access_token_secret="lMjzDDL76xpfTL4EhTAc5uOQogiDpZb6uAk6hhmXAmKdn"
auth = OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#table=[]
topics = ["WeGoHard","GrindCity","TissotBuzzerBeater","ThisIsYourTime","MFFL"]
for topic in topics:     
    for tweet in tweepy.Cursor(api.search,q=topic,count=10,lag="id",since="2019-10-22", until="2019-10-24").items():
        print (tweet.created_at, tweet.text)
        #table.append()

#myData = pandas.DataFrame(table)
#myData