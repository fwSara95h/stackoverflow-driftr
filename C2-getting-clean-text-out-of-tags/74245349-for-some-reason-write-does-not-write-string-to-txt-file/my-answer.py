# Code from my Stack Overflow answer https://stackoverflow.com/a/74245682 (posted 2022-10-29), extracted verbatim; may need the question's context to run.

# --- block 1 ---
with open('all_urls.txt', 'w') as f:
    f.write('\n'.join('tested_links')+'\n')

# --- block 2 ---
# before the while, if you're not sure the file exists
# [and/or to clear previous data from file]
# with open('all_urls.txt', 'w') as f: f.write('')

                # and inside the try block: 
                with open('all_urls.txt', 'a') as f:                 
                    f.write(f'{link}\n')
