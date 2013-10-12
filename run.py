#!/usr/bin/env python
#Author: Mehmet Dursun INCE
import twitter
import time
class DeleteTweet():

    def __init__(self):
        self.consumer_key = ''
        self.consumer_secret = ''
        self.access_token_key = ''
        self.access_token_secret = ''
        self.api = ''
        self.tweets = list()

    def connect(self):
        try:

            self.api = twitter.Api(self.consumer_key,
                                   self.consumer_secret,
                                   self.access_token_key,
                                   self.access_token_secret)
        except:
            print "Error: cant connect twitter. check ur credentials."

    def start(self):
        is_there_any_tweet = True
        latest_tweet = None
        while is_there_any_tweet:
            last_tweet = self.api.GetUserTimeline(count=150)
            if len(last_tweet) > 0:
                self.tweets = self.tweets + last_tweet
            else:
                is_there_any_tweet = False
                pass
            # delete current tweet list
            self.destroy_tweet()
            self.tweets = list()

    def destroy_tweet(self):
        for tweet in self.tweets:
            try:
                text = tweet.text.replace('\n', '').replace('\r', '')
                print "Tweet id: ", tweet.id, " ||  Date: ", tweet.created_at, " || ", text.encode('utf-8')
                self.api.DestroyStatus(tweet.id)
                time.sleep(1)
            except Exception, e:
                pass

if __name__ == '__main__':
    go = DeleteTweet()
    go.connect()
    go.start()
