# Code from my Stack Overflow answer https://stackoverflow.com/a/75954774 (posted 2023-04-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> df = pd.DataFrame([
>   [140.5745654, 90.9496963, 157.5959379, 101.2858137, 236.882037, 105.4921111],
>   [140.8908259, 91.01647765, 157.4825549, 101.4976646,236.6523714,105.2591143],
>   [141.1076296, 91.08488883, 157.3080705, 101.8022116],
>   [141.3524628, 91.17138846, 157.3539987, 102.167996],
>   [143.2526588, 92.28797636], [143.776291, 92.62887289]
> ], columns=pandas.MultiIndex.from_tuples([
>     ('C5P', 'CI2', 1, 'p'), ('C5P', 'CI2', 1, 'q'), ('C5P', 'CI2', 2, 'p'), 
>     ('C5P', 'CI2', 2, 'q'), ('C5P', 'CI2', 3, 'p'), ('C5P', 'CI2', 3, 'q')
> ], names=['borehole', 'sample','specimen', '']))
>

# --- block 2 ---
df_pivot = df.T.reset_index().pivot(['borehole', 'sample','specimen'], '', )
df_stack = df_pivot.swaplevel(0,1,1).stack(1)

# --- block 3 ---
df.T.stack().to_frame().swaplevel().sort_index() ## OR
# df.unstack().to_frame().swaplevel().sort_index()
