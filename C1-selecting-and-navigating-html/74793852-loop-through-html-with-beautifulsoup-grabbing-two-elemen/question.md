---
title: "Loop through html with beautifulsoup grabbing two elements from each <hr> tag then move on to the next and do the same"
site: stackoverflow
question_id: 74793852
url: https://stackoverflow.com/q/74793852
asked: 2022-12-14T05:14:29Z
asked_by: "qLu"
asked_by_url: https://stackoverflow.com/users/3923696
last_edited: 2022-12-14T13:00:53Z
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 179
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 350a7a4feb9bb6245280c69245efb97782ff4bfd072769fc91d069e907f2f8d9
---

# Loop through html with beautifulsoup grabbing two elements from each <hr> tag then move on to the next and do the same

Asked by [qLu](https://stackoverflow.com/users/3923696) on Stack Overflow, <https://stackoverflow.com/q/74793852>, 2022-12-14, last edited 2022-12-14. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Original question here: https://stackoverflow.com/questions/74778403/scrape-certain-elements-from-html-using-python-and-beautifulsoup/74778465#74778465

Follow-up question:

How do I loop through the entire html page grabbing the same info from each ```<hr>```?

The raw data would look like this:

```
<hr>
<b>1946 December 13 - </b>. 
<i>Launch Site</i>: <a href="http://www.astronautix.com/w/whitesands.html">White Sands</a>. 
<i>Launch Complex</i>: <a href="http://www.astronautix.com/w/whitesandslc33.html">White Sands LC33</a>. 
<i>LV Family</i>: <a href="http://www.astronautix.com/w/wac.html">WAC</a>. 
<i>Launch Vehicle</i>: <a href="http://www.astronautix.com/w/wacb.html">WAC B</a>. 
<ul><li><b>Test mission</b> - . 
<i>Nation</i>: <a href="http://www.astronautix.com/u/usa.html">USA</a>. 
<i>Agency</i>: <a href="http://www.astronautix.com/u/usaor.html">USA OR</a>. 
<i>Apogee</i>: 53 km (32 mi). </li></ul>

<hr>
<b>1948 December 13 - </b>. 
<ul><li><b>XS-1 Flight 102</b> - . 
<i>Crew</i>: <a href="http://www.astronautix.com/y/yeager.html">Yeager</a>. 
 <i>Payload</i>: XS-1 # 1 flight 59. <i>Nation</i>: <a href="http://www.astronautix.com/u/usa.html">USA</a>. 
<i>Related Persons</i>: <a href="http://www.astronautix.com/y/yeager.html">Yeager</a>. 
<i>Class</i>: <a href="http://www.astronautix.com/m/manned.html">Manned</a>. 
 <i>Type</i>: Manned rocketplane. <i>Spacecraft</i>: <a href="http://www.astronautix.com/x/xs-1.html">XS-1</a>. 
AF flight 37. Handling qualities and wing and tail loads at mach 1.. 
</li></ul>

<hr>
<b>1953 December 13 - </b>. 
<i>Launch Vehicle</i>: <a href="http://www.astronautix.com/r/r-11.html">R-11</a>. 
<ul><li><b>R-11 production decree</b> - . 
<i>Nation</i>: <a href="http://www.astronautix.com/r/russia.html">Russia</a>. 
<p>A government decree was issued for SKB-385 in the Urals to be 
responsible for series production of the R-11 and its S2.253 engine. 
SKB-385 had not distinguished itself in 1949-1951 when it was 
responsible for the first abortive attempt to put the R-1 rocket into 
production.</p></li></ul>

<hr>
<b>1954 December 13 - </b>. 
<i>LV Family</i>: <a href="http://www.astronautix.com/a/atlas.html">Atlas</a>. 
<i>Launch Vehicle</i>: <a href="http://www.astronautix.com/a/atlas.html">Atlas</a>. 
<ul><li><b>First production funding for Atlas.</b> - . 
Air Force Procurement Authorization 54-GM-3 authorized $3.6 million in 
P-150 production funding for Atlas. This was the first production 
funding for Atlas.. 
</li></ul>

<hr>
<b>1955 December 13 - </b>. 
05:00 GMT - . 
<i>Launch Site</i>: <a href="http://www.astronautix.com/w/whitesands.html">White Sands</a>. 
<i>Launch Complex</i>: <a href="http://www.astronautix.com/w/whitesandslc35.html">White Sands LC35</a>. 
<i>LV Family</i>: <a href="http://www.astronautix.com/a/aerobee.html">Aerobee</a>. 
<i>Launch Vehicle</i>: <a href="http://www.astronautix.com/a/aerobeertv-n-10a.html">Aerobee RTV-N-10a</a>. 
<ul><li><b>Airglow / Mass spectrometer Aeronomy mission</b> - . 
<i>Nation</i>: <a href="http://www.astronautix.com/u/usa.html">USA</a>. 
<i>Agency</i>: <a href="http://www.astronautix.com/n/nrl.html">NRL</a>. 
<i>Apogee</i>: 142 km (88 mi). Gas composition research. Launched at 2200 local time. Reached 142 km.. 
</li></ul>

<hr>
<b>1955 December 13 - </b>. 
17:58 GMT - . 
<i>Launch Site</i>: <a href="http://www.astronautix.com/h/holloman.html">Holloman</a>. 
<i>Launch Complex</i>: <a href="http://www.astronautix.com/h/hollomana.html">Holloman A</a>. 
<i>LV Family</i>: <a href="http://www.astronautix.com/a/aerobee.html">Aerobee</a>. 
<i>Launch Vehicle</i>: <a href="http://www.astronautix.com/a/aerobeeaj10-27.html">Aerobee AJ10-27</a>. 
<ul><li><b>Colorado UVS Solar ultraviolet mission</b> - . 
<i>Nation</i>: <a href="http://www.astronautix.com/u/usa.html">USA</a>. 
<i>Agency</i>: <a href="http://www.astronautix.com/u/usaf.html">USAF</a>. 
<i>Apogee</i>: 138 km (85 mi). Lyman alpha, solar limb darkening research. Launched at 1058 local time. Reached 138.4 km.. 
</li></ul>
```

The provided info works on the first ```<hr>``` but then I can't get it to go to the next one. I have been able to get it to repeat the same info x times or get just the first tag.

My loop looks like this:
```
soup = BeautifulSoup(page.content, "html.parser")


with open("test1.txt", "w") as file:
    hrs = soup.find_all('hr')
    for hr in hrs:
        title = soup.find("li").b.text
        text = soup.find("li").contents[-1].strip(" .\n")
        file.write("Today in #Space #History- "+title+" "+text.strip()+"\n")
```

This gives the output of:

```
Today in #Space #History- X-1 manned supersonic rocket aircraft begun. In an AAF-NACA conference, Air Force representatives indicated strong preference for use of rocket engines instead of jets in X-1 research airplane project..
Today in #Space #History- X-1 manned supersonic rocket aircraft begun. In an AAF-NACA conference, Air Force representatives indicated strong preference for use of rocket engines instead of jets in X-1 research airplane project..
Today in #Space #History- X-1 manned supersonic rocket aircraft begun. In an AAF-NACA conference, Air Force representatives indicated strong preference for use of rocket engines instead of jets in X-1 research airplane project..
Today in #Space #History- X-1 manned supersonic rocket aircraft begun. In an AAF-NACA conference, Air Force representatives indicated strong preference for use of rocket engines instead of jets in X-1 research airplane project..
Today in #Space #History- X-1 manned supersonic rocket aircraft begun. In an AAF-NACA conference, Air Force representatives indicated strong preference for use of rocket engines instead of jets in X-1 research airplane project..
Today in #Space #History- X-1 manned supersonic rocket aircraft begun. In an AAF-NACA conference, Air Force representatives indicated strong preference for use of rocket engines instead of jets in X-1 research airplane project..
```

I am getting from other threads that it's only grabbing the first element, but I can't figure out how to get it to keep going through the rest of the page.

It would also be nice to know why it is repeating, I feel like what's happening is that the for loop is grabbing the number of elements correctly but then the loop isn't updating the variables "title" and "text" so those are getting printed repeatedly the number of times the first element appears on the whole page.

I worked for a long time on this before I came back to make sure and do my due diligence but I am STUCK.



UPDATE:
I understand that there is obviously something wrong with the way I'm thinking about this for loop so I'll write what I think is going on if someone can help me correct my own thinking.

The page in question is horribly organized and changes each day so for today's page it would be like this: 

```
http://www.astronautix.com/d/december14.html
```

Here's what I think the loop is doing:

```
for hr in hrs:
```

Find each ```<hr>``` element on the page, I picked that because the ```<hr>``` tag precedes every section of data that I want to target.

```
title = soup.find("li").b.text
text = soup.find("li").contents[-1].strip(" .\n")
```

Within each ```<hr>``` section, grab the contents of ```<b>``` and the ```<li>``` and store them in variables.

Then what I think should happen is that it should iterate down to the next ```<hr>``` and do the same but my logic is very obviously flawed.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[qLu](https://stackoverflow.com/users/3923696)** (2022-12-14): I think afterwards I could modify with if statements to select elements if they exist, but getting this loop going is killing me lol.
