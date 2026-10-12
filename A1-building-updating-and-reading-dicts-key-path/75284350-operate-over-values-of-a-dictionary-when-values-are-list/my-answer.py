# Code from my Stack Overflow answer https://stackoverflow.com/a/75343141 (posted 2023-02-04), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>     data[key] = [value for value in values if value not in stop_words]
>

# --- block 2 ---
def remove_stopwords(orig, swList):
    return ' '.join(w for w in str(orig).split() if w.lower() not in swList)

# --- block 3 ---
stop_words = set(sw.lower() for sw in stopwords.words("english"))


for key, values in data.items():
    # data[key] = [remove_stopwords(v, stop_words) for v in values] # keeps empty strings
    swFil_gen = (remove_stopwords(v,stop_words) for v in values) # generator [not list]
    data[key] = [cleanStr for cleanStr in swFil_gen if cleanStr] # no empty strings

# --- block 4 ---
# data = {... # OR [if you don't want to change data]
cleaned_data = {key: [cleanStr for cleanStr in (
    remove_stopwords(v, stop_words) for v in values
) if cleanStr] for key, values in data.items()}

# --- block 5 ---
> {'ACCOUNT_CLOSURE': ['account closure',
>   'close account',
>   'close bank',
>   'terminate account',
>   'account deletion',
>   'cancel account',
>   'account cancellation'],
>  'ACCOUNT_CHANGE': ['change account',
>   'switch account',
>   'change private savings',
>   'convert family package',
>   'change title account',
>   'make title account family',
>   'help access documentation']}
>
