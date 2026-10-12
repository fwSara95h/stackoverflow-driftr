# Code from my Stack Overflow answer https://stackoverflow.com/a/73888211 (posted 2022-09-28), extracted verbatim; may need the question's context to run.
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('sex for grades since:2021-07-05 until:2022-07-06').get_items()):
    if i>150:
        break

    attributes_container.append(
        dict(
            (name, getattr(tweet, name)) for name in dir(tweet) 
            if not name.startswith('_') and name not in ['count','index']
        ) 
    )

tweets_df = pd.DataFrame(attributes_container)
