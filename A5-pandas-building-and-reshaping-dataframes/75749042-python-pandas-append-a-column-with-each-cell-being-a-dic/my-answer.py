# Code from my Stack Overflow answer https://stackoverflow.com/a/75755016 (posted 2023-03-16), extracted verbatim; may need the question's context to run.

# --- block 1 ---
df['ColDict'] = [{str(b): myfunc(v, b) for b in list_b} for v in df['val']]

# --- block 2 ---
df['ColDict'] = df['val'].apply(lambda v: {str(b): myfunc(v, b) for b in list_b})

# --- block 3 ---
# list_b = [....] # define first so that it can be used as arg2 default below

def myfunc(arg1, arg2=list_b):
    if isinstance(arg2, list):
        return {str(k): myfunc(arg1, k) for k in arg2}

    ##### continue with ORIGINAL FUNCTION BODY #####

# --- block 4 ---
df['ColDict'] = df['val'].apply(myfunc)

# --- block 5 ---
df = pd.DataFrame.from_dict(df.to_dict('index'), orient='index')
