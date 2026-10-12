# Code from my Stack Overflow answer https://stackoverflow.com/a/75710236 (posted 2023-03-11), extracted verbatim; may need the question's context to run.

# --- block 1 ---
people = [
  {'address': '01261 Cameron Spring\nTaylorfurt, AK 97791', 'id': 35193, 'jobs': ['Energy engineer', 'Engineer, site', 'Environmental health practitioner', 'Biomedical scientist', 'Jewellery designer'], 'mail': 'jsalazar@gmail.com', 'name': 'Lindsey Nguyen', 'sex': 'F', 'username': 'uhebert'},
  {'address': '66992 Welch Brooks\nMarshallshire, ID 56004', 'id': 91970, 'jobs': ['Music therapist', 'Volunteer coordinator', 'Designer, interior/spatial'], 'mail': 'bhudson@gmail.com', 'name': 'Cheryl Lewis', 'sex': 'F', 'username': 'vickitaylor'},
  {'address': 'Unit 1632 Box 2971\nDPO AE 23297', 'id': 1848091, 'jobs': ['Management consultant', 'Engineer, structural', 'Lecturer, higher education', 'Theatre manager', 'Designer, textile'], 'mail': 'darren44@yahoo.com', 'name': 'Julia Allen', 'sex': 'F', 'username': 'sheilaadams'},
  {'address': '9880 Michelle Bridge\nNew Kimberlybury, WY 02583', 'id': 50969, 'jobs': ['Mechanical engineer', 'Retail banker', 'Barrister'], 'mail': 'stevensonsarah@hotmail.com', 'name': 'Gina Stevens', 'sex': 'F', 'username': 'nicole82'},
  {'address': '9080 Monica Crescent Suite 820\nNorth Deanbury, HI 28977', 'id': 676820, 'jobs': ['Network engineer', 'Youth worker', 'Primary school teacher', 'Engineer, broadcasting (operations)'], 'mail': 'denise42@gmail.com', 'name': 'Nicholas Harrington', 'sex': 'M', 'username': 'jean67'},
  {'address': '635 Kenneth Ways Suite 172\nHancockfort, AZ 50544', 'id': 64918, 'jobs': ['Designer, ceramics/pottery', 'Engineer, energy', 'Engineer, manufacturing'], 'mail': 'monique02@hotmail.com', 'name': 'Allison Gomez', 'sex': 'F', 'username': 'james67'}
]

# --- block 2 ---
job_people = {}
for p in people:
    for j in p['jobs']:
        job_people.setdefault(j, [])
        job_people[j].append(p['username'])

# --- block 3 ---
jobs = {j for p in people for j in p['jobs']} ## list of unique job titles
job_people = {j: [u['username'] for u in people if j in u['jobs']] for j in jobs}

# --- block 4 ---
> {'Energy engineer': ['uhebert'],
>  'Engineer, site': ['uhebert'],
>  'Environmental health practitioner': ['uhebert'],
>  'Biomedical scientist': ['uhebert'],
>  'Jewellery designer': ['uhebert'],
>  'Music therapist': ['vickitaylor'],
>  'Volunteer coordinator': ['vickitaylor'],
>  'Designer, interior/spatial': ['vickitaylor'],
>  'Management consultant': ['sheilaadams'],
>  'Engineer, structural': ['sheilaadams'],
>  'Lecturer, higher education': ['sheilaadams'],
>  'Theatre manager': ['sheilaadams'],
>  'Designer, textile': ['sheilaadams'],
>  'Mechanical engineer': ['nicole82'],
>  'Retail banker': ['nicole82'],
>  'Barrister': ['nicole82'],
>  'Network engineer': ['jean67'],
>  'Youth worker': ['jean67'],
>  'Primary school teacher': ['jean67'],
>  'Engineer, broadcasting (operations)': ['jean67'],
>  'Designer, ceramics/pottery': ['james67'],
>  'Engineer, energy': ['james67'],
>  'Engineer, manufacturing': ['james67']}
>

# --- block 5 ---
# import pickle
with open('ob_people.pickle', 'wb') as fp:
    pickle.dump(job_people, fp)

# --- block 6 ---
def generalize_job(job_title:str):
    titles_ref = {
        'engineer': ['engineer'], 
        'designer': ['design'],
        'educator': ['educat', 'teach']
    }
    for title, keywords in titles_ref.items():
        for kw in keywords:
            if kw.lower() in job_title.lower(): return title.title() 
    return job_title ## default: return the original string

# --- block 7 ---
job_people = {}
for p in people:
    for j in p['jobs']:
        j = generalize_job(j)
        if p['username'] in job_people.setdefault(j, []): continue
        job_people[j].append(p['username'])

# --- block 8 ---
> { 'Engineer': ['uhebert', 'sheilaadams', 'nicole82', 'jean67', 'james67'],
>   'Designer': ['uhebert', 'vickitaylor', 'sheilaadams', 'james67'],
>   'Educator': ['sheilaadams', 'jean67'],
>   'Volunteer coordinator': ['vickitaylor'],
>   'Management consultant': ['sheilaadams'],
>   'Environmental health practitioner': ['uhebert'],
>   'Retail banker': ['nicole82'],'Youth worker': ['jean67'], 
>   'Barrister': ['nicole82'], 'Biomedical scientist': ['uhebert'], 
>   'Theatre manager': ['sheilaadams'], 'Music therapist': ['vickitaylor'] }
>
