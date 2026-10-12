# Code from my Stack Overflow answer https://stackoverflow.com/a/74819561 (posted 2022-12-16), extracted verbatim; may need the question's context to run.

# --- block 1 ---
page1_df = pd.concat([page1_df,pages_df])

# --- block 2 ---
pgdfList = [page1_df]
# for page in page_urls:
    ##### SCRAPE AND EXTRACT FOR dict_2 ##### 

    pgdfList.append(pd.DataFrame(dict_2))

page1_df = pd.concat(pgdfList)
print(page1_df)
