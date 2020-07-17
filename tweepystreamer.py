# Library imports

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener
import config

class StdOutListener(StreamListener):

    # Take in data from streamed listener
    def on_data(self, data):
        print(data)
        return True

    # If error is encountered, print status message
    def on_error(self, status):
        print(status)

if __name__ == "__main__":

    listener = StdOutListener()

    # Authenticate using credentials
    auth = OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
    auth.set_access_token(config.BEARER_TOKEN, config.BEARER_TOKEN_SECRET)

    stream = Stream(auth, listener)

    # Filter tweets
    stream.filter(track=['donald trump', 'hillary clinton', 'barack obama', 'bernie sanders'])