import snscrape.modules.twitter as sntwitter

query = "hola"
currentId = 0

while 1:
    lastId = currentId
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        currentId = tweet.id
        if currentId != lastId:
            print(f'@{tweet.user.username}: {tweet.content}')
        break