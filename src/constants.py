MP4: str = "video/mp4"
PROPERTY_BITRATE: str = "bitrate"
PROPERTY_MEDIA_TYPE: str = "mediaType"
PROPERTY_TWEET_ID: str = "tweetId"
PROPERTY_URL: str = "url"
QUERY: str = "#food"
TABLE_MEDIA: str = "media"
TABLE_TWEET: str = "tweet_test"
TYPE_PHOTO: str = "Photo"
TYPE_VIDEO: str = "Video"

class MediaMdodel():
    def __init__(self, url: str, bitrate: int = None):
        self.url = url
        self.bitrate = bitrate

class TweetModel():
    def __init__(self, tweetId: str, mediaType: str, media: str):
        self.tweetId = tweetId
        self.mediaType = mediaType
        self.media = media