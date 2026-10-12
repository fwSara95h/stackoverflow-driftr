# Code from my Stack Overflow answer https://stackoverflow.com/a/74373728 (posted 2022-11-09), extracted verbatim; may need the question's context to run.

# --- block 1 ---
table = soup.find('table')
sunlightHrs_byState = dict([(
    str(r.find('td').text.strip().lower()), # state name
    float(r.select_one('td ~ td').text.split()[0]) # sunlight
) for r in table.select('tr:has(td~td)')])

# --- block 2 ---
sunlightHrs_byState = dict([(
    r.find('td').get_text(strip=True), # state name
    (sum(
        float(a.strip()) for a in r.select_one('td ~ td').text.split('-')
    )/len(r.select_one('td ~ td').text.split('-'))) # averages sunlight hours
) for r in soup.select('table#tablepress-4 tr:has(td~td)')])
print(sunlightHrs_byState)

# --- block 3 ---
{'Alabama': 4.7, 'Alaska': 2.5, 'Arizona': 5.5, 'Arkansas': 4.550000000000001, 'California': 5.05, 'Colorado': 4.800000000000001, 'Connecticut': 4.0, 'Delaware': 4.199999999999999, 'Florida': 5.1, 'Georgia': 4.65, 'Hawaii': 5.05, 'Idaho': 4.1, 'Illinois': 4.15, 'Indiana': 4.1, 'Iowa': 4.1, 'Kansas': 4.699999999999999, 'Kentucky': 4.2, 'Louisiana': 4.85, 'Maine': 3.65, 'Maryland': 4.1, 'Massachusetts': 3.9, 'Michigan': 3.7, 'Minnesota': 3.75, 'Mississippi': 4.7, 'Missouri': 4.35, 'Montana': 3.9000000000000004, 'Nebraska': 4.4, 'Nevada': 5.199999999999999, 'New Hampshire': 3.65, 'New Jersey': 4.1, 'New Mexico': 5.5, 'New York': 3.8, 'North Carolina': 4.45, 'North Dakota': 3.9, 'Ohio': 3.9, 'Oklahoma': 4.9, 'Oregon': 4.05, 'Pennsylvania': 3.8499999999999996, 'Puerto Rico': 5.25, 'Rhode Island': 4.0, 'South Carolina': 4.7, 'South Dakota': 4.2, 'Tennessee': 4.3, 'Texas': 5.25, 'Utah': 4.95, 'Vermont': 3.5999999999999996, 'Virginia': 4.25, 'Washington': 3.6, 'Washington DC': 4.15, 'West Virginia': 4.0, 'Wisconsin': 3.8, 'Wyoming': 4.4}
