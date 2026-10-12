# Code from my Stack Overflow answer https://stackoverflow.com/a/75910101 (posted 2023-04-02), extracted verbatim; may need the question's context to run.
date = cmbs_soup.find('input', title='Select as of date', type='text', value=True) # OR
# date = cmbs_soup.select_one('input.mm-date-field.form-control.input-sm.date-picker[title="Select as of date"][type="text"][value]')
