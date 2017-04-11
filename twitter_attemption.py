from twitter import *
from auth_info import *

t = Twitter(auth=OAuth(access_token,
                       access_token_secret,
                       consumer_key,
                       consumer_secret)
            )
try:
    t.statuses.update(status="test read external files")
except TwitterHTTPError as e:
    print(e)
