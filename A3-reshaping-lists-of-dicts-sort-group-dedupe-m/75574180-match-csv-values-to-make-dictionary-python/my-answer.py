# Code from my Stack Overflow answer https://stackoverflow.com/a/75574315 (posted 2023-02-26), extracted verbatim; may need the question's context to run.

# --- block 1 ---
wordFreq = dict(zip(data['word'], data['count'])) ## same as:
# wordFreq = {k:v for k,v in zip(data['word'], data['count'])}

# --- block 2 ---
wordFreq = dict(data.to_dict('split')['data'])

# --- block 3 ---
wordFreq = dict(data.set_index('word')['count']) ## series with index ## OR
# wordFreq = dict(data[['word', 'count']].to_dict('split')['data']) ## list of lists
