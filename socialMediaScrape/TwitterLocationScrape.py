import tweepy
import csv
import enchant


#####setup our link to Twitter
consumer_key = 'suUf2FGWLkwCVnSvKItPM6FTz' ###API key
consumer_secret = 'afhjm4VYeMp3sHHJWRWyTuWhpGdVDDKXhnFudSgUydcxFCFeyP' ###APT Secrete Key

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

en_us = enchant.Dict("en_US")

##create our csv file 'w' means open file to write into in, 'a' append (add) 'r' read
csvFile = open('twitter_location.csv', 'w')
csvWriter = csv.writer(csvFile)

#write the header, if appending comment this line out
csvWriter.writerow(["user", "tweetText", "latitude", "longitude"])


#lets search twitter for tweets based on a location
search_words = "" #this is for keyword
for tweet in tweepy.Cursor(api.search, q=search_words, geocode="34.011675, -118.212644, 5km", lang="en").items(1000):
    print(tweet.user)
    if str(tweet.geo) != "None":
        user = tweet.user.name
        g = tweet.geo
        lat = g["coordinates"][0]
        lon = g["coordinates"][1]
        tText = tweet.text
        tText = tText.replace("\n"," ")
        tText = tText.replace("#", "")
        tText = tText.replace("@", "")
        tText = ' '.join(w for w in tText.split() if en_us.check(w))
        csvWriter.writerow([user,tText,lat,lon])
