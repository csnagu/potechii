import twitter,datetime
import auth_info

t = twitter.Api(consumer_key = auth_info.my_consumer_key,
                consumer_secret = auth_info.my_consumer_secret,
                access_token_key = auth_info.my_access_token,
                access_token_secret= auth_info.my_access_token_secret)

today = datetime.datetime.today()
days = today.strftime('%Y/%m/%d')
times = today.strftime('%H:%M:%S')

sc_ymd = input('予定日(eg.' + days + '):')
sc_hm = input('予定時刻(ex.' + times +  '):')
tweet_text = input('tweet text :')
schedule = sc_ymd.split('/')
schedule.extend(sc_hm.split(':'))

while True:
    today = datetime.datetime.today()
    today = today.strftime('%Y/%m/%d/%H/%M/%S').split('/')
    if today == schedule:
        try:
            status = t.PostUpdate(tweet_text)
            print(status.text)
            #users = t.GetFriends()
            #print(len(users))
        except twitter.error.TwitterError as e:
            print(e)
        break


