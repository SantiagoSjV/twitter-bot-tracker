from constants import *
import fb
import pathlib
import requests
import snscrape.modules.twitter as sntwitter

# Writes the media information in the DB
def setMedia(tweet: sntwitter.Tweet, mediumType: str, mediaData: dict):
    tweetData = TweetModel(tweet.id, mediumType, mediaData)
    fb.db.child(TABLE_TWEET).child(tweet.user.username).push(tweetData.__dict__)
    print(f'\nData pushed to: {TABLE_TWEET}/{tweet.user.username}')

# Identifies wether the media is a Photo or Video and calls the function to set the information
def createMedia(tweet: sntwitter.Tweet):
    for medium in tweet.media:
        if isinstance(medium, sntwitter.Photo):
            # mediaData: MediaMdodel = MediaMdodel(medium.previewUrl)
            # setMedia(tweet, TYPE_PHOTO, mediaData.__dict__)
            setMedia(tweet, TYPE_PHOTO, medium.previewUrl)

        elif isinstance(medium, sntwitter.Video):
            # mediaData: list[MediaMdodel] = []
            # object_dict: dict
            # for variant in medium.variants:
            #     if variant.contentType == MP4:
            #         object_dict = {variant.bitrate: variant.__dict__}
            url: str
            for variant in medium.variants:
                if variant.contentType == MP4:
                    url = variant.url
            setMedia(tweet, TYPE_VIDEO, url)

def getMedia():
    childTable = TABLE_TWEET
    for tableUser in fb.db.child(childTable).get().each():
        print("\n" + tableUser.key())
        childTable = f'{TABLE_TWEET}/{tableUser.key()}'
        for collection in fb.db.child(childTable).get().each():
            print(collection.val()[TABLE_MEDIA])
            if collection.val()[PROPERTY_MEDIA_TYPE] == TYPE_VIDEO:
                print(collection.val()[TABLE_MEDIA])
            fileName = f'{collection.key()}_{collection.val()[PROPERTY_TWEET_ID]}'
            downloadMedia(tableUser.key(), fileName, collection.val()[TABLE_MEDIA], collection.val()[PROPERTY_MEDIA_TYPE])
            # childTable = f'{childTable}/{TABLE_MEDIA}'
            # print(childTable)
            # for data in fb.db.child(childTable).get().each():
            #     print("hola")

def downloadMedia(mediaFolder: str, fileName: int, url: str, mediaType: str):
    if mediaType == TYPE_VIDEO:
        mediaName = f'{fileName}.mp4'
    elif mediaType == TYPE_PHOTO:
        mediaName = f'{fileName}.png'
    r = requests.get(url)
    pathlib.Path(f"media/{mediaFolder}").mkdir(parents=True, exist_ok=True) 
    with open(f"media/{mediaFolder}/{mediaName}", 'wb') as fp:
        fp.write(r.content)

#Get media stored this way: Media/Username/actual_data
def getMediaOld():
    tableMedia = fb.db.child(TABLE_MEDIA).get()
    for tableUser in tableMedia.each():
        print("\n" + tableUser.key())
        media = fb.db.child(TABLE_MEDIA).child(tableUser.key()).get()
        for m in media.each():
            print(m.val()[PROPERTY_URL])

#Delete data stored in: Media/
def deleteMedia():
    fb.db.child(TABLE_MEDIA).remove()
    
totalTweets = 0
totalTombTweets = 0
for tweet in sntwitter.TwitterProfileScraper(QUERY).get_items():
    if isinstance(tweet, sntwitter.Tombstone):
        totalTombTweets += 1
        print(tweet)
    elif not isinstance(tweet, sntwitter.Tombstone) and not tweet.retweetedTweet and tweet.media:
        print(f'retweet: {tweet.retweetedTweet}')
        totalTweets+=1
        createMedia(tweet)
print(f'\nTweets: {totalTweets}, Tomb Tweets: {totalTombTweets}')

getMedia()