#Utiliser la bibliothèque Twython

from twython import Twython

consumer_secret = 'CabsczUroATEuVm5gjMRDJBnxlrzYMXLgqDuR1jzUhBX985aE8'
consumer_key = 'DDScZa8AfRvTLrxEAo5AfBIx6'
access_token        = '1184801885456424960-WhJxi89nonWJPlgN0kzh8S9Cr6HhV3'
access_token_secret = 'S3lkUYFwWptnFCnNi4ule19wyWGvgkwTOS13nFC10CRXJ'

def tweet(message):
        twitter = Twython(
            consumer_key,
            consumer_secret,
            access_token,
           access_token_secret
        )
    
        twitter.update_status(status=message)
        print("Tweeted : {}".format(message))

tweet("test fct tweeter")