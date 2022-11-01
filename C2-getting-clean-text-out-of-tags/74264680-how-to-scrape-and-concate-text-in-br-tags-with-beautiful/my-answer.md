---
title: "How to scrape and concate text in <br> tags with Beautiful Soup"
site: stackoverflow
question_id: 74264680
answer_id: 74277990
url: https://stackoverflow.com/a/74277990
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T15:10:11Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74277990/revisions
accepted: true
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: [br-splitting function]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7a3ad1a28c4ea4dd22a65ea793559f49e0a86a20e6130852d8baaaa88dcd1f1f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74277990>, 2022-11-01; **accepted**; score 1. Text as retrieved 2026-10-12.

If you just use the `separator` argument of `get_text`
```python 
print(souped.find(class_="propertyItem_13").get_text('\n').strip())
```
you'll get
```lang-none
Beschreibung:


Zustand siehe Bild. Zusätzlich: Ecken und Kanten leicht bestoßen. Seiten und Buchschnitt altersbedingt leicht verfärbt. Buchschnitt fleckig, siehe Bilder. Ab der Hälfte des Buches sind die Seiten oben leicht gebogen.
 
 
Die deutsche Sprache kennt zwar nur vier Fälle, dafür aber über tausend Zweifelsfälle. Heißt es Pizzas oder Pizzen? Gewinkt oder gewunken? Wann schreibt man Storys und wann Stories? Hat der Genitiv noch eine Chance — trotz des Dativs und dem Dativ zum Trotz?
 
Dieses Buch präsentiert die großartige SPIEGEL¬ONLINE-Kolumne »Zwiebelfisch«, die Woche für Woche Leser amüsiert, schockiert, belehrt und begeistert.
 
»Man spürt das Vergnügen, das der Umgang mit gutem Deutsch bereitet.« FAZ
 
»Wo der Duden nicht weiter weiß, weiß Sick Rat.« Saarbrücker Zeitung
 
Über das Buch:
 
Die oder das Nutella — diese Frage hat schon viele Gemüter am Frühstückstisch bewegt. Der, die, das — wieso, weshalb, warum? Ob Nutella nun weiblich oder sächlich ist, ist sicherlich keine Frage auf Leben und Tod, aber eine Antwort hätten wir schon gern. Wir? Ja, wir hilflos Verlorenen im Labyrinth der deutschen Sprache. Wir, die wir unsere liebe Not mit der deutschen Sprache haben. Und leichter, verständlicher oder zumindest nachvollziehbarer ist es nach der Rechtschreibreform auch nicht geworden.
In seinen hinreißend komischen und immer klugen Kolumnen bringt Bastian Sick Licht ins Dunkel der deutschen Sprachregelungen und sortiert den Sprachmüll. Ist der inflationären Verwendung von Binde-strichen noch Einhalt zu gebieten, angesichts von Spar-Plänen und Quoten-Druck? Versinken wir sprachlich gesehen nicht längst im Hagel der Apostrophe, wenn Känguru's plötzlich in den Weiten Australien's leben? Derlei Unsinn scheint nicht mehr aufhaltbar, wenn es nicht dieses Buch gäbe. Darauf zwei Espressis!
 
Der Autor:
 
Bastian Sick, Jahrgang 1965, Studium der Geschichtswissenschaft und Romanistik, Tätigkeit als Lektor und Übersetzer; von 1995-1998 Dokumentationsjournalist beim SPIEGEL-Verlag, ab Januar 1999 Mitarbeiter der Redaktion von SPIEGEL ONLINE. Seit Mai 2003 dort Autor der Kolumne »Zwiebelfisch«.
```

<hr>

But if you want to target the `<br>`s specifically, you can copy [this function](https://gist.github.com/Driftr95/8b799ab0c235dab90c69f875c99a9f81) into your code and use it like
```python
print(html_to_text(souped.find(class_="propertyItem_13"))[1])
``` 
and that will give you
```lang-none
Beschreibung:Zustand siehe Bild. Zusätzlich: Ecken und Kanten leicht bestoßen. Seiten und Buchschnitt altersbedingt leicht verfärbt. Buchschnitt fleckig, siehe Bilder. Ab der Hälfte des Buches sind die Seiten oben leicht gebogen.


Die deutsche Sprache kennt zwar nur vier Fälle, dafür aber über tausend Zweifelsfälle. Heißt es Pizzas oder Pizzen? Gewinkt oder gewunken? Wann schreibt man Storys und wann Stories? Hat der Genitiv noch eine Chance — trotz des Dativs und dem Dativ zum Trotz?

Dieses Buch präsentiert die großartige SPIEGEL¬ONLINE-Kolumne »Zwiebelfisch«, die Woche für Woche Leser amüsiert, schockiert, belehrt und begeistert.

»Man spürt das Vergnügen, das der Umgang mit gutem Deutsch bereitet.« FAZ

»Wo der Duden nicht weiter weiß, weiß Sick Rat.« Saarbrücker Zeitung

Über das Buch:

Die oder das Nutella — diese Frage hat schon viele Gemüter am Frühstückstisch bewegt. Der, die, das — wieso, weshalb, warum? Ob Nutella nun weiblich oder sächlich ist, ist sicherlich keine Frage auf Leben und Tod, aber eine Antwort hätten wir schon gern. Wir? Ja, wir hilflos Verlorenen im Labyrinth der deutschen Sprache. Wir, die wir unsere liebe Not mit der deutschen Sprache haben. Und leichter, verständlicher oder zumindest nachvollziehbarer ist es nach der Rechtschreibreform auch nicht geworden.
In seinen hinreißend komischen und immer klugen Kolumnen bringt Bastian Sick Licht ins Dunkel der deutschen Sprachregelungen und sortiert den Sprachmüll. Ist der inflationären Verwendung von Binde-strichen noch Einhalt zu gebieten, angesichts von Spar-Plänen und Quoten-Druck? Versinken wir sprachlich gesehen nicht längst im Hagel der Apostrophe, wenn Känguru's plötzlich in den Weiten Australien's leben? Derlei Unsinn scheint nicht mehr aufhaltbar, wenn es nicht dieses Buch gäbe. Darauf zwei Espressis!

Der Autor:

Bastian Sick, Jahrgang 1965, Studium der Geschichtswissenschaft und Romanistik, Tätigkeit als Lektor und Übersetzer; von 1995-1998 Dokumentationsjournalist beim SPIEGEL-Verlag, ab Januar 1999 Mitarbeiter der Redaktion von SPIEGEL ONLINE. Seit Mai 2003 dort Autor der Kolumne »Zwiebelfisch«.
```

<hr>

In this case , the difference is barely noticeable, but if you had more tags, you'd definitely notice that the first method spaces out *everything*, not just `br`; but if this is all you need it for, then the first method is much simpler.
