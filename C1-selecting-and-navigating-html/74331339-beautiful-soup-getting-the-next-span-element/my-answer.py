# Code from my Stack Overflow answer https://stackoverflow.com/a/74334049 (posted 2022-11-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
html = '''
<br/>
<h4>Dieses Jahr</h4>
<br/>
<span class="parName">Januar:</span> <span class="parValue">143.92 kWh</span> | 
<span class="parName">Diesen Monat:</span> <span class="parValue">67.54 kWh</span> | 
<span class="parName">Februar:</span> <span class="parValue">350.51 kWh</span> | 
'''
BeautifulSoup(html).find("span", string="Diesen Monat:").find_next_sibling()

# --- block 2 ---
BeautifulSoup(html, 'html5lib').select_one("span:-soup-contains('Diesen Monat:') + span")
