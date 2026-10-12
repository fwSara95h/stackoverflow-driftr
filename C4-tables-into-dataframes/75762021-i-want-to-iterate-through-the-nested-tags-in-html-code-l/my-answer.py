# Code from my Stack Overflow answer https://stackoverflow.com/a/75796283 (posted 2023-03-20), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# from bs4 import BeautifulSoup

code_str = '''
<div class = "las">
    <div class = "asas">
      <table style="width:100%">
        <tr><th>Firstname</th><th>Lastname</th><th>Age</th></tr>
        <tr><td>Jill</td><td>Smith</td><td>50</td></tr>
        <tr><td>Eve</td><td>Jackson</td><td>94</td></tr>
        <tr><td>John</td><td>Doe</td><td>80</td></tr>
      </table>
    </div>
</div>
''' 
code = BeautifulSoup(code_str).div

# --- block 2 ---
# import re
# from bs4 import BeautifulSoup
code = BeautifulSoup(re.sub('>\s*<', '><', code_str).div

# --- block 3 ---
# import bs4
class indexableTag:
    def __init__(self, origTag:bs4.element.Tag, ignore_whitespace=True):
        self.tag = origTag
        self.tag_contents = [
            indexableTag(c) if isinstance(c,bs4.element.Tag) else c 
            for c in origTag.children
            if not (ignore_whitespace and isinstance(c,str) and not c.strip())
        ]

    def __getitem__(self, key): 
        return self.tag_contents[key]

code = indexableTag(bs4.BeautifulSoup(code_str).div)

# --- block 4 ---
# import pandas as pd 

df = pd.read_html(code_str)[0] ##-> df.loc[0]['Lastname'] #='Smith'
df_dict = df.to_dict() ##-> df_dict['Lastname'][0] #='Smith'
df_recs = df.to_dict('records') ##-> df_recs[0]['Lastname'] #='Smith'
