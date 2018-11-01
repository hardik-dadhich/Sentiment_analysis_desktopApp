import re
from tweepy import OAuthHandler
from textblob import TextBlob
import tweepy  # To consume Twitter's API
import profile


class TwitterClient:
    def tweetsanalyse(self):

        self.tweet_user = 'sachin_rt'
        # getting tweeter username for analysis of comments:
        print("if does't call")
        try:
            myobj = profile.Ui_MainWindow()
            self.tweet_user = myobj.usernamefun()
            print(self.tweet_user)
        except:
            print("just default tweeter accounts tweets")

        # keys and tokens from the Twitter Dev Console
        CONSUMER_KEY = 'aCLcl8h15bhN196ZfZp0k5qqE'
        CONSUMER_SECRET = 'HMH2s7JEKjZbwxBSauKOIawirdyl4FCA1cqzpPgfOZxjKWCJJ3'
        ACCESS_TOKEN = '3196308522-rxqjP0NQyJcO7GdjzcJ6mNulQIVzlpasBRjyWSK'
        ACCESS_SECRET = '1p2Do64h1gjYXRszujIjjB3Fsgy6vVUGuZcFUO5Zs4snp'

        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        # Return API with authentication:
        api = tweepy.API(auth)

        # We create a tweet list as follows:
        tweets = api.user_timeline(screen_name=self.tweet_user, count=200)
        print("Number of tweets extracted: {}.\n".format(len(tweets)))

        # We print the most recent 5 tweets:
        print("5 recent tweets:\n")
        for tweet in tweets[:5]:
            print(tweet.text)
            print()

        data = []
        data = [str(tweet.text) for tweet in tweets[:5]]
        # data = pd.DataFrame(data=[tweet.text for tweet in tweets[:5]], columns=['Tweets'])
        # We display the first 10 elements of the dataframe:
        print("----------------------------")
        print(data[0])
        return data[0]


if __name__ == '__main__':
    obj = TwitterClient()
    z = obj.tweetsanalyse()
