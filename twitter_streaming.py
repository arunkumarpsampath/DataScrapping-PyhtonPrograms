from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd,glob

consumer_key = "STmfnnIiWOKB8S5SENEUAGZAZ"
consumer_secret = "uM6gVsNw7qTrpuicXVFx3Vgb8qyA6bdDNpfJhU01oll5bDUnmQ"

access_token = "1102777661523410944-mkT0HKSNzbspAxnfsAPiaM18g8gD9D"
access_token_secret = "CiXpgkpHZ0PB6DdvzIAXadjWEPXQta8iCbVPjv5UPVHzv"


class StdOutListener(StreamListener):

    def on_data(self, data):
        print('----')
        tweet = json.loads(data)
        tweet_df = pd.DataFrame(
            {'user_name' : [tweet['user']['name']],
             'user_handler' : [tweet['user']['screen_name']],
             'text' : [tweet['text']],
             'created_at': [tweet['created_at']],
             'user_location' : [tweet['user']['location']],
             'source' : [tweet['source']]})
        file_name = 'tweets_datascience.csv'
        cwd = glob.glob('*.csv')
        file_exists = file_name in cwd
        if file_exists:
            with open(file_name,'a') as f:
                print('appending to file')
                tweet_df.to_csv(f,index=False, header=False,encoding='utf-8') # only for first time header(column names) should be added
        else:
            print('creating file')
            tweet_df.to_csv(file_name,index=False,encoding='utf-8')

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
stream.filter(track=['#Worldcup2019'])