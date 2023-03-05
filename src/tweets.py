import fb
import requests
import snscrape.modules.twitter as sntwitter

def saveMedia(tweetMedia):
    for medium in tweetMedia:
        if isinstance(medium, sntwitter.Photo):
            mediaFolder = f'{tweet.user.username}'
            mediaName = f'{tweet.id}.png'
            r = requests.get(medium.fullUrl)
            with open(f"media/{mediaName}", 'wb') as fp:
                fp.write(r.content)
            fb.connection.storage().child(f'{mediaFolder}/{mediaName}').put(f'media/{mediaName}')
            return fb.connection.storage().child(f'{mediaFolder}/{mediaName}').get_url(None)

query = "#food"
currentId = 0
while 1:
    lastId = currentId
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        currentId = tweet.id
        if currentId != lastId and tweet.media:
            print("\nmediaUrl: " + saveMedia(tweet.media))
            print("content: " + tweet.rawContent)
        break