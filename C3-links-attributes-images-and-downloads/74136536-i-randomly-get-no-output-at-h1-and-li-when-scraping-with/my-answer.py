# Code from my Stack Overflow answer https://stackoverflow.com/a/74146125 (posted 2022-10-20), extracted verbatim; may need the question's context to run.
repeats = 0  # initiate
maxRepeats = 10 # limit allowed errors

abl_copy = audiobooklinks[:] # preserve original
for link in abl_copy:
    r = requests.get(link) #headers=headers)

    soup = BeautifulSoup(r.content, "lxml")

    if r.status_code != 200 or not r.content:
        print(f'! {r.status_code} {r.reason} - for {link} !')
        repeats += 1
        if maxRepeats < repeats: 
            print('! Stopping because of too many bad responses !')
            break
        abl_copy.append(link)
        continue

    soup = BeautifulSoup(r.content, "lxml")

    # rest of your for loop
