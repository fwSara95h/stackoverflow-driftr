---
title: "Extracting contents from a PDF to display on web pages"
site: stackoverflow
question_id: 74701968
url: https://stackoverflow.com/q/74701968
asked: 2022-12-06T11:46:29Z
asked_by: "Ajay Surya Senthilrajan"
asked_by_url: https://stackoverflow.com/users/20681043
last_edited: 2022-12-07T05:59:20Z
tags: [html, python-3.x, pdf, web, beautifulsoup]
score: -1
views_at_snapshot: 538
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: de8aea4dd4fbb985fa8e3909983f62ad09292dd2cc2aa3e242288d9332d48f5d
---

# Extracting contents from a PDF to display on web pages

Asked by [Ajay Surya Senthilrajan](https://stackoverflow.com/users/20681043) on Stack Overflow, <https://stackoverflow.com/q/74701968>, 2022-12-06, last edited 2022-12-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to display the contents of the pdf by converting PDF into HTML using Adobe Acrobat 2021, extracting the paragraph structure, and post-processing. I saw a website whose only source is judgments as PDFs from the Supreme Court Website and displays them flawlessly. Does anybody have any idea how it's done? 

My current flow is to convert the PDF into HTML to preserve the page layout and extract the text using Beautifulsoup.
Issues I'm currently facing:
- Bulletin numbers are somehow dynamically calculated in the PDF and are tagged as 
```
::before 
```
on the browser. bs4 won't recognize it
- Miss some paragraphs in between as some paragraphs are detected incorrectly
- Table is detected as a table but some imperfections

PDF example : [drive link][1]

HTML from Adobe Acrobat : [HTML file of the above PDF][2]

This is my goal : [Advocatekhoj][3]

This is how accurate I'm expecting it to be.
Could someone please shed light on this? how-to(s) or any suggestions.

Note: I tried various PDF to HTML tools and the Adobe Acrobat was the best in detecting paragraph layout and preserving structure.

    
```

    from bs4 import BeautifulSoup
    from pprint import pprint 
    
    from os import listdir
    from os.path import isfile, join
    mypath = "sup_del_htmls/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    counter = 0
    for f in onlyfiles:
        print(counter)
        with open("output_txt/"+f+".txt", 'w',encoding='utf-8') as txtfile:
            with open(mypath+f, encoding='utf-8') as fp:
                soup = BeautifulSoup(fp, "html.parser")
                
                para_counter = 1
                for li in soup.select("li"):
                    if li.find_parent("li"):
                        continue
                    
                    full_para = ""
                    for para in li.select("p"):
                        for match in para.findAll('span'):
                            match.unwrap()
                        para_txt = para.get_text().replace("¶", "")
                        para_txt = para_txt.strip()
                        if para_txt.endswith(".") or para_txt.endswith(":") or para_txt.endswith(";") or para_txt.endswith(",") or para_txt.endswith('"') or para_txt.endswith("'"):
                            full_para += para_txt + "\n"
                        else:
                            full_para += para_txt + " "
    
                    txtfile.write(full_para)
                    txtfile.write("\n" + "--sep--" + "\n")
                    if li.find("table"):
                        tables = li.find_all("table")
                        for table in tables:
                            txtfile.write("--table--"+ "\n")
                            txtfile.write(str(table) + "\n")
                            txtfile.write("--sep--" + "\n")
                reversed_end = []
                for p in reversed(soup.select("p")):
                    if p.find_parent('li') or p.find_parent('ol'):
                        break
                    reversed_end.append(" ".join(p.text.split()))
                if reversed_end!=[]:
                    for final_end in reversed(reversed_end):
                        txtfile.write(final_end + "\n")
                        txtfile.write("--sep--" + "\n")
```

The Result : [output.txt][4]


  [1]: https://drive.google.com/file/d/1Sobqym3RVjyaK9qid395khB9nOmZc0g0/view?usp=sharing
  [2]: https://drive.google.com/file/d/1mfHEDnI7DTcWI4zORrMvVdcwG0B3cmJG/view?usp=sharing
  [3]: https://www.advocatekhoj.com/library/judgments/announcement.php?WID=13472
  [4]: https://drive.google.com/file/d/19qVA4eXjXO8ambBbwo0fkM3ouySh0INX/view?usp=sharing

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[baduker](https://stackoverflow.com/users/6106791)** (2022-12-06): Please read [ask] and provide a [mre].
- **me** (2022-12-06): Please include a sample of the html you're getting (it can be another drive link to the whole file and/or a relevant snippet), and a snippet of the current bs4 output that shows the part you're not happy with
- **[Ajay Surya Senthilrajan](https://stackoverflow.com/users/20681043)** (2022-12-07): Hi, @Driftr95 I've fixed it. Please ask me if you need anything else.
