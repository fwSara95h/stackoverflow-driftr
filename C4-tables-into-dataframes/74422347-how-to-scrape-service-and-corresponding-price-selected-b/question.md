---
title: "How to scrape service and corresponding price, selected by string?"
site: stackoverflow
question_id: 74422347
url: https://stackoverflow.com/q/74422347
asked: 2022-11-13T15:32:58Z
asked_by: "Hronic"
asked_by_url: https://stackoverflow.com/users/10234524
last_edited: 2022-11-15T16:45:52Z
last_editor: "HedgeHog"
last_editor_url: https://stackoverflow.com/users/14460824
tags: [python-3.x, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 59
answer_count: 2
accepted_answer_id: 74455631
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dca550a206ee4961614a46668c7d0938454f65450c98961ffd97965af57c53e7
---

# How to scrape service and corresponding price, selected by string?

Asked by [Hronic](https://stackoverflow.com/users/10234524) on Stack Overflow, <https://stackoverflow.com/q/74422347>, 2022-11-13, last edited 2022-11-15 by [HedgeHog](https://stackoverflow.com/users/14460824). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

On specific, given website I want to:

 1. Check if specific service (provided by string) is available
 2. If available I want to get its price

Let's assume that pricing is stored in `table` which name I don't know. <br>
I've used `beautifulsoup` to find this service by variable called `strServiceVersion` on webiste (looking for columns which contains string).<br>

    arrDataCell = soup.find_all('td', text=strServiceVersion)
                if len(arrDataCell)>0:      #found data cell with given string
                    print("\nPrint whole data cell: ")
                    print(arrDataCell)               
                    print("\nPrint parent of the 1st data cell: ") #print below
                    print(arrDataCell[0].parent())

So I know this text (name of service) exist on the webpage in some table. <br>
I can print parent of the 1st data cell: <br> 

    [<td class="column-1"> Some_Text_1</td>, Some_Text_2, <td class="column-2">Price_1</td>, Price_2]

Now I know this X table has two columns and I know its class names (column-1 and column-2 I presume?) <br>
Now I would like to get this table as an object and being able to loop through it and extract it by row and column. <br>

How do I do that? <br>
Or any other solution? <br>

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2022-11-13): And what would that website be, if I may ask?
- **me** (2022-11-13): to *"get this table as an object and being able to loop through it"* you could try pandas - [`read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html) (keep in mind that it return a **list** of dataframes -  1 for each table after filtering with the `match` or `attrs` arguments) followed by [`to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html) (you'll probably want to set the `orient` argument to `"records"` or `"split"`)
- **me** (2022-11-13): I don't often see `td` tags alternating with text....why is *" parent of the 1st data cell"* a list anyway?
- **[Hronic](https://stackoverflow.com/users/10234524)** (2022-11-15): @BarrythePlatipus Example website: https://optimdent.pl/cennik/  Service Kompleksowe badanie stomatologiczne jamy ustnej  Price 150
- **[Hronic](https://stackoverflow.com/users/10234524)** (2022-11-15): @Driftr95 how do I identify, to which table given <td> belongs to? In this case, which table is it "arrDataCell[0].parent()"
- **[Hronic](https://stackoverflow.com/users/10234524)** (2022-11-15): @Driftr95  "parent of the 1st data cell" is a list, to be precise "<class 'bs4.element.ResultSet'>", doc: https://tedboy.github.io/bs4_doc/generated/generated/bs4.ResultSet.html
- **me** (2022-11-16): @Hronic Sorry for the misunderstanding - I confused it with `arrDataCell[0].parent` which would have been a single Tag (the one directly containing `arrDataCell[0]`) as opposed to the *Tags inside the `arrDataCell[0].parent`* which are returned by `arrDataCell[0].parent()`, because I didn't know about `.parent()` before; I used to use `.parent.find_all(True, recursive=False)`, but this is shorter so thanks!
- **me** (2022-11-16): @Hronic *re: "how do I identify, to which table given <td> belongs to"* - [`pandas.read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html) has a `match` argument - you could set it as `strServiceVersion` to only grab table/s containing that [just remember that it'll be a list of dataframes even if it contains only one df]
