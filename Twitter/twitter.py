from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "Hello test!"
twitter.update_status(status=message)
print("Tweeted: %s" % message)

#messages = [
    #"Hello World",
    #"Hi there",
    #"What's up?",
    #"How's it going?",
    #"Have you been here before?",
    #"Get a hair cut!",
#]

#message = random.choice(messages)
#twitter.update_status(status=message)
#print("Tweeted: " + message)

#image = open('image.jpg', 'rb')
#response = twitter.upload_media(media=image)
#media_id = [response['media_id']]
#twitter.update_status(status=message, media_ids=media_id)
#print("Tweeted: " + message)
