# Code from my Stack Overflow answer https://stackoverflow.com/a/73953386 (posted 2022-10-04), extracted verbatim; may need the question's context to run.
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('sex for grades since:2021-07-05 until:2022-07-06').get_items()):
    if i>150:
        break
    try:
      tweetMedia = tweet.media[0].fullUrl # .previewUrl if you want previewUrl
    except:
      tweetMedia = tweet.media # or None or '' or any default value 
    attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content, tweetMedia])
