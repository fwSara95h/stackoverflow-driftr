# Code from my Stack Overflow answer https://stackoverflow.com/a/75050526 (posted 2023-01-08), extracted verbatim; may need the question's context to run.
jScript = soup.find(lambda s: s.name=='script' and 'window.__NUXT__' in s.text)
jScript = jScript.text if jScript else '0 SCRIPTS CONTAINING "window.__NUXT__"'
jsStr = jScript.replace('class:', 'was_class:').replace('default:', 'was_default:')
jsData = findObj_inJS(jsStr, [
    'info_text', 'info_title', 'search_text', 'date_of_entry',
    'info_bar_items', 'important_info_items', 'main_title', 'second_title'
], findAll=True, jStrict=False)
