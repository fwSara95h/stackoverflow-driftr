---
title: "How to cleanup ‘orphaned’ text in poorly written html using Python?"
site: stackoverflow
question_id: 74916307
url: https://stackoverflow.com/q/74916307
asked: 2022-12-25T23:01:58Z
asked_by: "Code Monkey"
asked_by_url: https://stackoverflow.com/users/9135359
last_edited: never
tags: [python, html, beautifulsoup]
score: 0
views_at_snapshot: 80
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 94c0f11f2e09b3919ef1525b96659e1f9367c08851210c39bcc6fda0b66ef1d9
---

# How to cleanup ‘orphaned’ text in poorly written html using Python?

Asked by [Code Monkey](https://stackoverflow.com/users/9135359) on Stack Overflow, <https://stackoverflow.com/q/74916307>, 2022-12-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Let me explain: I scrapped html off a poorly written website and wish to clean up the code by encapsulating each line within a `<div>` tag, keep the existing `bold`, `italic` and other formatting information, keep the `images` and `links`. I will then format everything and prettify it once cleaned.

Below are 3 sample lines from the website:

    line1 = '1. O: upper border of 1st rib &amp; cartilage.<div>2. I: inferior surface of middle third of the clavicle.&nbsp;</div><div>3. NS: nerve to subclavius.&nbsp;</div><div>4. A: anchors &amp; depresses clavicle.&nbsp;</div><div><br></div><div><div><img src="paste-3461743641109.jpg"></div><div><span style="font-weight: bolder">Image:&nbsp;</span>Gray, Henry.&nbsp;<i>Anatomy of the Human Body.</i>&nbsp;Philadelphia: Lea &amp; Febiger, 1918; Bartleby.com, 2000.&nbsp;<a href="">www.bartleby.com/107/</a>&nbsp;[Accessed 15 Nov. 2018].&nbsp;</div></div>'
    
    line2 = '''<div><i>CVS</i></div><div>1. Cardiovascular conditioning &amp; improves postural hypotension<br></div><div><b><span style="font-weight: 400;">2. Improves ventilation</span></b><br></div><div><b><span style="font-weight: 400;"><br></span></b></div><div><b><span style="font-weight: 400;"><i>BONES</i></span></b></div><div>3. Promote &amp; maintain bone density, prevent osteoporosis<b><span style="font-weight: 400;"><br></span></b></div><div><br></div><div><i>MUSCLES &amp; JOINTS</i></div>4. Safe reintroduction of the patient to vertical position<div><div>5. Facilitate early weight bearing</div><div><b><span style="font-weight: 400;">6. Prevent contractures</span></b><br></div><div><b><span style="font-weight: 400;"><br></span></b></div><div><b><span style="font-weight: 400;"><i>SKIN</i></span></b></div><div>7. Decreases prolonged bed rest &amp; its complications</div></div><div><br></div><div><i>PSYCHOLOGY</i></div><div>8. Improves psychological outlook &amp; motivation</div>'''

    line3 = '''ORIGIN<div>1. Branch of the posterior cord of the brachial plexus -&nbsp;C5, C6.</div><div><br></div><div>COURSE</div>2. Passes out of the axilla, through the quadrangular space with posterior circumflex humeral vessels, to the upper arm where it's in contact with surgical neck of the humerus.&nbsp;</div><div><br></div><div>BRANCHES</div><div><i><font color="#ff086c">3. Sensory supply to small 'regimental patch' over shoulder.</font></i></div><div><i><font color="#ff086c">4. Anterior - supplies the deltoid.&nbsp;</font></i></div><div><i><font color="#ff086c">5. Posterior - supplies teres minor, becomes upper lateral cutaneous nerve of the arm.&nbsp;</font></i></div><i><font color="#ff086c"><img src="paste-6103148528016.jpg"></font></i></div><div><div><b style="font-weight: bold; ">Image:&nbsp;</b>Gray, Henry.&nbsp;<i>Anatomy of the Human Body.</i>&nbsp;Philadelphia: Lea &amp; Febiger, 1918; Bartleby.com, 2000.&nbsp;<a href="https://www.bartleby.com/107/">www.bartleby.com/107/</a>&nbsp;[Accessed 16 Nov. 2018].</div></div>'''

You will notice that in `line1` there is no `<div>` tag at all at the beginning, whereas `line2` starts with a <div> tag but point `4` within is not enclosed in such a tag. `line3` has multiple strings not enclosed in `<div>` tags.

I wrote the following to correct the first line (`line1`):

    # 1. First, find all lines enclosed in <div> tags
    temp_soup = BeautifulSoup(html.unescape(line), "html.parser")
    soup = BeautifulSoup("", "html.parser")
    for tag in temp_soup.find_all('div'): 
        tag.extract()
        soup.append(tag)
    
    # 2. Then, ensure that the first line starts with the <div> tag, else isolate the first sentence and enclose it between <div> tags
    new_div = soup.new_tag("div")
    new_div.string = str(temp_soup)
    soup.insert(0, new_div)
    
    print(soup)

However, the above code does not fix the second line. Moreover, it cannot correct lines with multiple strings not enclosed in `<div>` tags.

Could someone suggest an algorithm to clean up all 3 lines? I've tried `BeautifulSoup.prettify()` and `lxml clean_html()` to no avail.
