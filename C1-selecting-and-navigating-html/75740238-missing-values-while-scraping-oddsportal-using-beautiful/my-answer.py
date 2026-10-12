# Code from my Stack Overflow answer https://stackoverflow.com/a/75747651 (posted 2023-03-15), extracted verbatim; may need the question's context to run.
# a_cont # <-- no longer necessary
ac_sel = 'div:has(>a.active-item-calendar)' # a_cont selector
a_sel = f'{ac_sel}>a[href]:not([href^="#"]):not(.active-item-calendar)'
a_tags = soup.select(a_sel)
urls = ['https://www.oddsportal.com'+a_tag['href'] for a_tag in a_tags]
