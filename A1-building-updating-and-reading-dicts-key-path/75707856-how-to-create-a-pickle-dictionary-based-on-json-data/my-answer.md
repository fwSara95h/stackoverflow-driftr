---
title: "How to create a Pickle dictionary based on JSON data"
site: stackoverflow
question_id: 75707856
answer_id: 75710236
url: https://stackoverflow.com/a/75710236
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-11T23:36:14Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75710236/revisions
accepted: true
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 09148f8596ff59a9b4564a54c3f4c3c8913cba8255d6631a3fe817e4fa27fc8d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-11

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75710236>, 2023-03-11; **accepted**; score 1. Text as retrieved 2026-10-12.

Your snippet isn't JSON; most noticeably, JSON uses double-quotes `"` rather than single `'`; but more importantly the individual dictionaries containing user data need to all be wrangled into one sequence (like in the list below).

```py
people = [
  {'address': '01261 Cameron Spring\nTaylorfurt, AK 97791', 'id': 35193, 'jobs': ['Energy engineer', 'Engineer, site', 'Environmental health practitioner', 'Biomedical scientist', 'Jewellery designer'], 'mail': 'jsalazar@gmail.com', 'name': 'Lindsey Nguyen', 'sex': 'F', 'username': 'uhebert'},
  {'address': '66992 Welch Brooks\nMarshallshire, ID 56004', 'id': 91970, 'jobs': ['Music therapist', 'Volunteer coordinator', 'Designer, interior/spatial'], 'mail': 'bhudson@gmail.com', 'name': 'Cheryl Lewis', 'sex': 'F', 'username': 'vickitaylor'},
  {'address': 'Unit 1632 Box 2971\nDPO AE 23297', 'id': 1848091, 'jobs': ['Management consultant', 'Engineer, structural', 'Lecturer, higher education', 'Theatre manager', 'Designer, textile'], 'mail': 'darren44@yahoo.com', 'name': 'Julia Allen', 'sex': 'F', 'username': 'sheilaadams'},
  {'address': '9880 Michelle Bridge\nNew Kimberlybury, WY 02583', 'id': 50969, 'jobs': ['Mechanical engineer', 'Retail banker', 'Barrister'], 'mail': 'stevensonsarah@hotmail.com', 'name': 'Gina Stevens', 'sex': 'F', 'username': 'nicole82'},
  {'address': '9080 Monica Crescent Suite 820\nNorth Deanbury, HI 28977', 'id': 676820, 'jobs': ['Network engineer', 'Youth worker', 'Primary school teacher', 'Engineer, broadcasting (operations)'], 'mail': 'denise42@gmail.com', 'name': 'Nicholas Harrington', 'sex': 'M', 'username': 'jean67'},
  {'address': '635 Kenneth Ways Suite 172\nHancockfort, AZ 50544', 'id': 64918, 'jobs': ['Designer, ceramics/pottery', 'Engineer, energy', 'Engineer, manufacturing'], 'mail': 'monique02@hotmail.com', 'name': 'Allison Gomez', 'sex': 'F', 'username': 'james67'}
]
```

[If you aren't sure of how to go about that, you should edit the question to focus on that or (preferably) post a new question. Make sure to explain what format the data is in currently.]

---

Once you have the sequence of dictionaries `people`, there are many ways you can form your *`{ job: [list of 'username', who has this job title in json data] }`* dictionary.

<br>

You could use a nested [`for`](https://www.programiz.com/python-programming/for-loop) loop with [`.setdefault`](https://www.programiz.com/python-programming/methods/dictionary/setdefault) like:

```py
job_people = {}
for p in people:
    for j in p['jobs']:
        job_people.setdefault(j, [])
        job_people[j].append(p['username'])
``` 

<br>

Or you could use [dictionary comprehension](https://www.programiz.com/python-programming/dictionary-comprehension):

```py
jobs = {j for p in people for j in p['jobs']} ## list of unique job titles
job_people = {j: [u['username'] for u in people if j in u['jobs']] for j in jobs}
```

You could do it in one statement <sup>(with *`job_people = {j: [u['username'] for u in people if j in u['jobs']] for p in people for j in p['jobs']}`*)</sup>, but it's more efficient to build each list <sup>(of *`[u['username'] for u in people if j in u['jobs']]`*)</sup> only once. 

Not that it would make much difference for the sample data - since each job title only seems to appear once. [So each list only contains one person/username...] With either of the above methods, `job_people` [built from the sample data should] look like

>```py
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
>```

---

### Pickling the Data

> *It has to be done with pickle and then saved as file named "job_people.pickle"*

Once you have the `job_people` dictionary, it can be saved to "job_people.pickle" with [`pickle.dump`](https://docs.python.org/3/library/pickle.html#pickle.dump) as simply as:

```py
# import pickle
with open('ob_people.pickle', 'wb') as fp:
    pickle.dump(job_people, fp)
```

---
---

Btw, if you want to reduce the list of occupations to more general job titles, you could either use a dictionary <sup>(like *`{'Primary school teacher': Teacher', 'Engineer, energy': 'Engineer',....}`*)</sup> with [`.get(j,j)`](https://www.programiz.com/python-programming/methods/dictionary/get) or define a function like 

```py
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
```

and use it in the `for` loop like

```py
job_people = {}
for p in people:
    for j in p['jobs']:
        j = generalize_job(j)
        if p['username'] in job_people.setdefault(j, []): continue
        job_people[j].append(p['username']) 
```

to result in `job_people` as below:

>```py
> { 'Engineer': ['uhebert', 'sheilaadams', 'nicole82', 'jean67', 'james67'],
>   'Designer': ['uhebert', 'vickitaylor', 'sheilaadams', 'james67'],
>   'Educator': ['sheilaadams', 'jean67'],
>   'Volunteer coordinator': ['vickitaylor'],
>   'Management consultant': ['sheilaadams'],
>   'Environmental health practitioner': ['uhebert'],
>   'Retail banker': ['nicole82'],'Youth worker': ['jean67'], 
>   'Barrister': ['nicole82'], 'Biomedical scientist': ['uhebert'], 
>   'Theatre manager': ['sheilaadams'], 'Music therapist': ['vickitaylor'] }
>```
