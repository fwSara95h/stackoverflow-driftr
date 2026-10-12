# Code from my Stack Overflow answer https://stackoverflow.com/a/74367438 (posted 2022-11-08), extracted verbatim; may need the question's context to run.

# --- block 1 ---
tLinkSel = 'table.table-main.only12.js-nrbanner-t a[href^="/tennis"]:has(strong)'
matchlist = set('https://www.betexplorer.com'+a.get('href') for a in soup.select(tLinkSel))

# --- block 2 ---
tLinkSel = 'tr[data-dt^="2,11,2022,"] a[href^="/tennis"]:has(strong)'
