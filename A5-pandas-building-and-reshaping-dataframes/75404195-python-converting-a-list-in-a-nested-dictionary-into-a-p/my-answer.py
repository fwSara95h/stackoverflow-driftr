# Code from my Stack Overflow answer https://stackoverflow.com/a/75404500 (posted 2023-02-09), extracted verbatim; may need the question's context to run.
# Includes later revisions by: wjandrea (https://stackoverflow.com/users/4518341), revision 2, 2023-02-10, CC BY-SA 4.0.

# --- block 1 ---
# import pandas as pd

def tabulate_actions(actionsList:list, returnDf=False):
    aTbl = [{
        a['action_type']: a['value'] for a in al['actions']
        # if isinstance(a, dict) and all([k in a for k in ['action_type', 'value']])
    } for al in actionsList
    # if isinstance(al, dict) and isinstance(al.get('actions'), list)
    ]
    return pd.DataFrame(aTbl) if returnDf else aTbl
## uncomment the conditions if you're unsure of your data structure

# --- block 2 ---
> [{'link_click': '16',
>   'post_engagement': '16',
>   'page_engagement': '16'},
>  {'comment': '5',
>   'onsite_conversion.post_save': '1',
>   'link_click': '465',
>   'post': '1',
>   'post_reaction': '20',
>   'video_view': '4462',
>   'post_engagement': '4954',
>   'page_engagement': '4954'}]
>
