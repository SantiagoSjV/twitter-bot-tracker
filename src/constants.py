QUERY: str = "#cdmx"
TABLE_MEDIA: str = "media"
MEDIA_URL: str = "mediaUrl"
MP4: str = "video/mp4"
TYPE_PHOTO: str = "Photo"
TYPE_VIDEO: str = "Video"

class Media():
    def __init__(self, username: str, mediaUrl: str, mediaType: str, bitrate: int = None):
        self.username = username
        self.mediaUrl = mediaUrl
        self.mediaType = mediaType
        self.bitrate = bitrate