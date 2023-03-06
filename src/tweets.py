from constants import *
import fb
import snscrape.modules.twitter as sntwitter

# Writes the media information in the DB
def setMedia(tweet: sntwitter.Tweet, mediaUrl: str, mediumType: str, bitrate: int = None):
    data = Media(tweet.user.username, mediaUrl , mediumType, bitrate)
    fb.db.child(TABLE_MEDIA).child(tweet.id).push(data.__dict__)
    print(f'\n{data.__dict__}')

# Identifies wether the media is a Photo or Video and calls the function to set the information
def createMedia(tweet: sntwitter.Tweet):
    for medium in tweet.media:
        if isinstance(medium, sntwitter.Photo):
            setMedia(tweet, medium.previewUrl, TYPE_PHOTO)

        elif isinstance(medium, sntwitter.Video):
            for variant in medium.variants:
                if variant.contentType == MP4:
                    setMedia(tweet, variant.url, TYPE_VIDEO, variant.bitrate)

#Get media stored this way: Media/Username/actual_data
def getMedia():
    tableMedia = fb.db.child(TABLE_MEDIA).get()
    for tableUser in tableMedia.each():
        print("\n" + tableUser.key())
        media = fb.db.child(TABLE_MEDIA).child(tableUser.key()).get()
        for m in media.each():
            print(m.val()[MEDIA_URL])

#Delete data stored in: Media/
def deleteMedia():
    fb.db.child(TABLE_MEDIA).remove()
    
# deleteMedia()
currentId = 0
while 1:
    lastId = currentId
    for tweet in sntwitter.TwitterSearchScraper(QUERY).get_items():
        currentId = tweet.id
        if currentId != lastId and tweet.media:
            createMedia(tweet)
        break