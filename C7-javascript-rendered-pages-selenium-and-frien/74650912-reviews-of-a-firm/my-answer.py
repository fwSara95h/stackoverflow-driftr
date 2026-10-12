# Code from my Stack Overflow answer https://stackoverflow.com/a/74663815 (posted 2022-12-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
scrapedIds = []
# for...
    # for ###
        # soup = extract...

        # for r in ...
            if r.get('id') in scrapedIds: continue # skip duplicate
            ## rDet = ..... ## AND REST OF INNER FOR-LOOP ##

            empRevs.append(rDet) 
            scrapedIds.append(rDet['reviewId']) # add to list of ids to check against

# --- block 2 ---
## PASTE [OR DOWNLOAD&IMPORT] from https://pastebin.com/RsFHWNnt ##

startUrl = 'https://www.glassdoor.com/Reviews/3M-Reviews-E446.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng'
scrape_gdRevs(startUrl, 'empRevs_3M.csv', maxScrapes=1000, constBreak=False)
