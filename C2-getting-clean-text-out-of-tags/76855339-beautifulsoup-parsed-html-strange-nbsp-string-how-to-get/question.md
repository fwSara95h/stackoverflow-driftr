---
title: "BeautifulSoup parsed HTML: strange NBSP string, how to get rid of them?"
site: stackoverflow
question_id: 76855339
url: https://stackoverflow.com/q/76855339
asked: 2023-08-07T21:45:42Z
asked_by: "Ziqi"
asked_by_url: https://stackoverflow.com/users/1783398
last_edited: 2023-08-08T08:35:15Z
tags: [beautifulsoup]
score: -1
views_at_snapshot: 187
answer_count: 1
accepted_answer_id: 76867902
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 77fe30c7088e14fd08415e402f95a111a31a3ca32d8cdc7bc554012f9661dc7b
---

# BeautifulSoup parsed HTML: strange NBSP string, how to get rid of them?

Asked by [Ziqi](https://stackoverflow.com/users/1783398) on Stack Overflow, <https://stackoverflow.com/q/76855339>, 2023-08-07, last edited 2023-08-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

**ANSWER FOUND, see the bottom of this message**

So I use BeautifulSoup to parse html content and while inspecting a **Tag** object created by soup, I have encountered very strange string that looks like the image below - this is through 'inspecting variables' in my IDE, pycharm.

[![enter image description here][1]][1]

The real HTML looks like below:

[![enter image description here][2]][2]

When I call `Tag.getText().strip()`, those 'NBSP' are not removed. Essentially all I want is just the text 'Take action for animals suffering now \n.'. But those NBSP does not seem to be the &nbsp; entities because I'd assume soup would've converted them to spaces? What are those NBSP's and how to get rid of them?

Thanks

**EDIT ANSWER FOUND**
I tried Claude and it gave me the right answer. I post here below, hopefully it is useful for others. 

In short, these 'NBSP' (I also had ZWNJ in another) are unicode characters that show up as white spaces after parsing HTML. The are NOT html entities so soup does not parse them. One reason these appear in your HTML is possibly the authors copied content from Word and inherited whitespaces - obviously that is not good practice.

To get rid of such content, do 

    import string
    text = tagobject.getText() #'tagobject' is whichever soup tag object you want to process    
    text=''.join(filter(lambda x: x in string.printable, text))

Alternatively, if you know the unicode for the character you want to rid of, you can use `text.replace(u'\xa0', ' ')`



  [1]: https://i.sstatic.net/7HRMT.png
  [2]: https://i.sstatic.net/mP1U4.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[MendelG](https://stackoverflow.com/users/12349734)** (2023-08-07): Please [edit] your question to include the HTML
- **[Ben Voigt](https://stackoverflow.com/users/103167)** (2023-08-07): Were any of these characters in the document before it was processed by beautifulsoup?
- **[MendelG](https://stackoverflow.com/users/12349734)** (2023-08-07): What IDE are you using? I have a feeling it's the way it's represented in the IDE and not the actual code. (the image looks like it's just the output within the IDE)
- **[baduker](https://stackoverflow.com/users/6106791)** (2023-08-08): Please don't post pictures of code. Make sure you have a [mre].
- **[Ziqi](https://stackoverflow.com/users/1783398)** (2023-08-08): Thank you, I have added the original HTML snippet. All these characters are found in the Tag object processed by soup, so yes, the content is processed by soup.
- **[Conrad](https://stackoverflow.com/users/3946752)** (2023-08-08): DO NOT use images of code
- **[Quentin](https://stackoverflow.com/users/19068)** (2023-08-08): Normally when people paste a picture of code, it just makes it hard for people to reproduce the problem because *everyone who wants to experiment with it has to transcribe it by hand* … but when the problem is caused by different kinds of whitespace character … 🤷🏻‍♂️
