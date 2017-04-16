import twitter
import auth_info

t = twitter.Api(consumer_key = auth_info.my_consumer_key,
                consumer_secret = auth_info.my_consumer_secret,
                access_token_key = auth_info.my_access_token,
                access_token_secret= auth_info.my_access_token_secret)
try:
    status = t.PostUpdate("首が痛すぎる")
    print(status.text)
except twitter.error.TwitterError as e:
    print(e)
