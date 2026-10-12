# Code from my Stack Overflow answer https://stackoverflow.com/a/74788681 (posted 2022-12-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# for i, tweet in...
    # tweets = ....
    with open('file.txt', 'a', encoding="utf-8") as f:
        print(tweets, file=f)

# --- block 2 ---
import snscrape.modules.twitter as twitter
maxTweets = 10
keyword='salvation'
timeStr = 'since:2021-11-01 until:2023-01-01 lang:"en" '
twGen = twitter.TwitterSearchScraper(f'{keyword} {timeStr} ').get_items() 

allTweets = []
for i, tweet in enumerate(twGen):
    if i > maxTweets: break

    tweets = {
             "tweet.url" : tweet.url
            }   
    allTweets.append(tweets)

## [OUTSIDE loop]
with open('file.txt', 'w', encoding="utf-8") as f:
    f.write('\n'.join[str(t) for t in allTweets])
