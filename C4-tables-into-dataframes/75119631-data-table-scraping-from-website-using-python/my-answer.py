# Code from my Stack Overflow answer https://stackoverflow.com/a/75120574 (posted 2023-01-14), extracted verbatim; may need the question's context to run.
dfList = pd.read_html(url) # OR
# dfList = pd.read_html(page.text) # OR
# dfList = pd.read_html(soup.prettify())

allTime = dfList[0].set_index(['rank', 'Youtuber'])

# (header row in 1st half so 2nd half reads as headerless to pandas)
dfList[2].columns = dfList[1].columns 
perYear = pd.concat(dfList[1:]).set_index(['rank', 'Youtuber'])


columns_ordered = [
    'started', 'category', 'subscribers', 'subscribers/year', 
    'video views', 'Video views/Year', 'video count', 'Video count/Year'
] # re-order columns as preferred
combinedDf = pd.concat([allTime, perYear], axis='columns')[columns_ordered]
