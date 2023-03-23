---
title: "itterating over a set of data - so that i fetch data from a site with beautiful-soup, panda and store it subsequently"
site: stackoverflow
question_id: 75828524
url: https://stackoverflow.com/q/75828524
asked: 2023-03-23T22:32:05Z
asked_by: "zero"
asked_by_url: https://stackoverflow.com/users/525865
last_edited: 2023-03-24T01:03:31Z
tags: [python, pandas, csv, beautifulsoup]
score: 1
views_at_snapshot: 250
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0cea0bc1a7d779224fe10efaf6f4b117ee75135d90a84710c596aca897dfe96d
---

# itterating over a set of data - so that i fetch data from a site with beautiful-soup, panda and store it subsequently

Asked by [zero](https://stackoverflow.com/users/525865) on Stack Overflow, <https://stackoverflow.com/q/75828524>, 2023-03-23, last edited 2023-03-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

i am currently workin on a sript to be able to scrape the data from the given website using Beautiful Soup and store it in a CSV format: the site 'https://schulen.bildung-rp.de' - a governmental site that lists schools. 

**update:**  see a result-page here.



[![enter image description here][1]][1]

with the following dataset:

    Kurzbezeichnung:	GY Ludwigshafen Carl-Bosch
    Schulnummer:	50360
    Anschrift:	Carl-Bosch-Gymnasium Ludwigshafen
    Jägerstr. 9
    67059 Ludwigshafen am Rhein
    Telefon:	(0621)504430810
    Telefax:	(0621)504430898
    E-Mail:	cbg(at)cbglu.de
    Internet:	http://www.cbglu.de
    Träger:	Stadtverwaltung Ludwigshafen am Rhein
    letzte Änderung:	15 Nov 2012 14:39:15 von 50360

well i am looking for the following things -( categories ) in the dataset:

    Kurzbezeichnung:	
    Schulnummer:
    Anschrift:	
    Telefon:
    Telefax:
    E-Mail:	
    Internet:	
    Träger:	

subsequently i have to correct the code!

#well Here's an example code snippet that i am using as a starting point:

what is aimed: this code will extract data from the table on the above given website, and store it in both a CSV file (schools.csv) and a pandas dataframe (schools_pandas.csv). 
note  that the table on the website contains seven columns or lemme say fieldnames = ['Kurzbezeichnung','Schulnummer','Anschrift', 'Telefon', 'Telefax', 'E-Mail','Internet', 'Träger').  ... but



    import requests
    from bs4 import BeautifulSoup
    import csv
    import pandas as pd
    
    # send a GET request to the target URL
    url = 'https://schulen.bildung-rp.de'
    response = requests.get(url)
    
    # parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # find the table element containing the desired data
    table = soup.find('table')
    
    # extract the data from the table and store it in a list of dictionaries
    data = []
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 7:
            # extract the desired columns and store them in a 
    
       # extract the desired columns and store them in a dictionary
            Kurzbezeichnung = cols[0].text.strip()
            Anschrift = cols[1].text.strip()
            Telefon: =  cols[2].text.strip()
            Telefax: = cols[3].text.strip()
            E-Mail: =  cols[4].text.strip()
            Internet = cols[5].text.strip()
            Träger =   cols[6]text.strip()
            data.append({'Kurzbezeichnung': school_name,
                         'Anschrift': school_type,
                         'Telefon': phonenumber,
                         'Telefax': faxnumber,
                         'E-Mail': mailadress   
                         'Internet': internet-adress,
                         'Träger': trager,})
                        
    # store the data in a CSV file
    with open('schools.csv', 'w', newline='') as csvfile:
    fieldnames = ['Kurzbezeichnung','Schulnummer','Anschrift', 'Telefon', 'Telefax', 'E-Mail','Internet', 'Träger'] 

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)
    
    # alternatively, load the data into a pandas dataframe
    df = pd.DataFrame(data)
    df.to_csv('schools_pandas.csv', index=False)



it does not store the data ... but the table structure  i think is correctly "reworked and treated" in the code -

well i think that the code is pretty complete hmmm  i think that i may need to modify the code accordingly a bit...


  [1]: https://i.sstatic.net/EAkNT.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-03-23): On the page I see table with 4 columns but the columns are `"Schulnummer"/"Kurzbezeichnung"/"PLZ"/"Datenschutz"`, not `School Name, School Type, City, and District`. Do I see the same table?
- **me** (2023-03-23): [As far as I can see] there's only one table at https://schulen.bildung-rp.de and you can save it to CSV as simply as `pd.read_html('https://schulen.bildung-rp.de')[0].to_csv('schools_pandas.csv', index=False)` [It *will* have different column than you seem to be looking for, as AndrejKesely noted, although you can probably figure out the Type from the first "word" in the Kurzbezeichnung column]
- **[zero](https://stackoverflow.com/users/525865)** (2023-03-24): hello dear Andrej and Driftr95 - many thanks for the reply - youre right - i have added some explanation in the threadstart - and yes well i am looking for the following things -( categories ) in the dataset:      Kurzbezeichnung:	     Schulnummer:	     Telefon:     Telefax:     E-Mail:	     Internet:	     Träger:	  subsequently i have to correct the code!... hopefully i manage that  - guess that this can be done... Driftr - did i get you right: can we save this to csv with your line? i will digg deeper into all that... many  thanks for all your help here  - its outstanding ...
- **[zero](https://stackoverflow.com/users/525865)** (2023-03-24): HI there i added some ideas and corrections  accordingly - but i have seen that even more corrections are necessary - i will have to do even more corrections....
