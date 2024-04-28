import got, codecs
from pymongo import MongoClient

def mongodb():
    client = MongoClient('localhost', 27017)
    db = client['twitter_db']
    collection = db['twitter_collection']

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('ChennaiFloods').setSince("2015-12-01").setUntil(
        "2015-12-02").setMaxTweets(6000)

    def streamTweets(tweets):
        for t in tweets:
            obj = {"user": t.username ,"retweets": t.retweets, "favorites": t.favorites, "text": t.text,"geo": t.geo,
                   "mentions": t.mentions, "hashtags": t.hashtags,"id": t.id, "permalink": t.permalink,}
            tweetind = collection.insert_one(obj).inserted_id

    got.manager.TweetManager.getTweets(tweetCriteria, streamTweets)

def csv():

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('ChennaiFloods').setSince("2015-12-01").setUntil(
        "2015-12-02").setMaxTweets(6000)

    outputFile = codecs.open("output_got.csv", "w+", "utf-8")
    outputFile.write('username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink')

    def receiveBuffer(tweets):
        for t in tweets:
            outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s' % (
                t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions,
                t.hashtags,
                t.id, t.permalink)))
        outputFile.flush()
        print('More {} saved on file...\n'.format(len(tweets)))

    got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
    outputFile.close()

if __name__ == '__main__':
    # mongodb()
    csv()