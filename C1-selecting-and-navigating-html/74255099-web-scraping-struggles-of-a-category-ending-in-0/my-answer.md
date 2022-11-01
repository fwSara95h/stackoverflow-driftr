---
title: "Web scraping struggles of a category ending in == 0$"
site: stackoverflow
question_id: 74255099
answer_id: 74274619
url: https://stackoverflow.com/a/74274619
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T10:37:50Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74274619/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a57662b10ffb7fa843ecf93d2db0066c3e247fac670cb28386ba5846db77f794
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74274619>, 2022-11-01; **accepted**; score 0. Text as retrieved 2026-10-12.

I believe your parser might be the issue. When I run your code with https://www.maquillalia.com/apieu-m-406.html, I also don't get anything *until* I change the parser to `html.parser` - which gives me one tag in `productlist` but there is a warning message; the warning goes away if I use `html5lib`
```python
soup = BeautifulSoup(r.content, 'html5lib')
```
with the above change, it prints
```lang-none
[<div class="prdt Product"><!-- /cache: pl_class_46761{BPCwo} --><div><h3 class="Title"><a href="https://www.maquillalia.com/apieu-mascarilla-icing-sweet-bar-sheet-mask-sandia-p-46761.html">A'pieu - Mascarilla Icing Sweet Bar sheet Mask - Sandía</a></h3><div class="Image"><figure><a href="https://www.maquillalia.com/apieu-mascarilla-icing-sweet-bar-sheet-mask-sandia-p-46761.html"><img alt="A'pieu - Mascarilla Icing Sweet Bar sheet Mask - Sandía" border="0" class="prdct-img" height="220" src="images/productos/thumbnails/a-pieu-mascarilla-icing-sweet-bar-sheet-mask-sandia-1-46761_thumb_220x220.jpg" title="A'pieu - Mascarilla Icing Sweet Bar sheet Mask - Sandía" width="220"/></a></figure></div><div class="Description">Mascarilla anatómica de algodón con vitaminas y oligoelementos que hidratan y recuperan la piel dañada.

Con extracto de Sandía que hidrataa y cuida la piel.

 <a class="MoreLink" href="https://www.maquillalia.com/apieu-mascarilla-icing-sweet-bar-sheet-mask-sandia-p-46761.html">Ver +</a></div><div class="ProductBot"><div class="Price" data-price="1.90"><strong>1,90€</strong></div><div class="Rating"><span class="Stars" data-rating="5.00"><span class="BgicoN-star On" title="5"></span><span class="BgicoN-star On" title="4"></span><span class="BgicoN-star On" title="3"></span><span class="BgicoN-star On" title="2"></span><span class="BgicoN-star On" title="1"></span><span class="Active" style="width: 100%"></span></span><span class="Num">(3)</span></div><div class="BuyCn"><!-- cache: pl_boton_46761{BPCwo} --><a class="Button Buy" data-atribute="" data-href="https://www.maquillalia.com/apieu-mascarilla-icing-sweet-bar-sheet-mask-sandia-p-46761.html" data-id="46761" data-qty="6" href="javascript:void(0);" rel="nofollow" title="Comprar A'pieu - Mascarilla Icing Sweet Bar sheet Mask - Sandía">Comprar<span style="position: absolute;top: 0;left: 0;width:100%;height: 100%;"></span></a><!-- /cache: pl_boton_46761{BPCwo} --><a class="BgicoB-Fav Button fvrt Fav" data-cid="0" data-list="" data-login="0" data-pid="46761" href="javascript:void(0);"></a><div class="taxtx"><span>IVA Incl.</span><span>Precio por 100 Gr: 9,05€</span></div></div></div></div></div>]
```

<hr>

Btw, to find any `div` with both `prdt` and `Product` classes, but not necessarily *just* those, you can use
```python
soup.find_all('div', {'class':'prdt', 'class':'Product'})
```
or preferably
```python
soup.select('div.prdt.Product')
```
and then divs with class `prdt Product Agotado`,`Product prdt`,etc will also be included.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Troy McLure](https://stackoverflow.com/users/19690963)** (2022-11-02): Awesome! You are the best :D it works perfectly, and you read my mind about including both categories. Thank you so much mate!
- **[Troy McLure](https://stackoverflow.com/users/19690963)** (2022-11-05): Hi drift, just a question again: now I'm trying to get the rating values, so the inspected element is this https://prnt.sc/k4YaALUle05z but when I write soup.find('span', class_='Stars').attrs  , I get an array {'data-rating': '4.67', 'class': ['Stars']} instead the number 4.67, that it is what I need. I have tried lot of combinations from the documentation, but I can't extract just the number... do you know how to get it??
- **me** (2022-11-05): @TroyMcLure why not just use `.get`? like `soup.find('span', class_='Stars').get('data-rating')` - it's the same as `soup.find('span', class_='Stars').attrs['data-rating']`, but with `.get` you'll get `None` instead of an error if `data-rating` isn't in the array
- **[Troy McLure](https://stackoverflow.com/users/19690963)** (2022-11-09): You are right @Driftr95 , I didn't know that! I read alternatives by using "try:" but yours is much better (actually, the right mode i think xD). Thank you again!!
