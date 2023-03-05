import fb
import requests
import snscrape.modules.twitter as sntwitter

def saveMedia(tweetMedia):
    media_url = []
    index = 0
    for medium in tweetMedia:
        if isinstance(medium, sntwitter.Photo):
            index += 1
            mediaFolder = f'{tweet.user.username}'
            mediaName = f'{tweet.id}_{index}.png'
            r = requests.get(medium.fullUrl)
            with open(f"media/{mediaName}", 'wb') as fp:
                fp.write(r.content)
            fb.connection.storage().child(f'{mediaFolder}/{mediaName}').put(f'media/{mediaName}')
            media_url.append(fb.connection.storage().child(f'{mediaFolder}/{mediaName}').get_url(None))
    return media_url

query = "#food"
currentId = 0
while 1:
    lastId = currentId
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        currentId = tweet.id
        if currentId != lastId and tweet.media:
            print(saveMedia(tweet.media))
            print("content: " + tweet.rawContent + "\n")
        break