# Code from my Stack Overflow answer https://stackoverflow.com/a/74343296 (posted 2022-11-07), extracted verbatim; may need the question's context to run.
last_page_num = # set the last page number here

scraped_data = []
for page_num in range(1, last_page_num + 1):
    url = f'youtube.com/user/{page_num}/'
    try:

        ################## SCRAPE URL ################## 

        ############ APPEND TO scraped_data ############

    except Exception as err: 
        print(f'unable to scrape {url}\n{str(err)}')
        # break # if you want to stop after first error

################# SAVE scraped_data #################
