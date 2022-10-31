---
title: "How to scrape and concate text in <br> tags with Beautiful Soup"
site: stackoverflow
question_id: 74264680
answer_id: 74265392
url: https://stackoverflow.com/a/74265392
author: "Md. Fazlul Hoque"
author_url: https://stackoverflow.com/users/12848411
posted: 2022-10-31T15:14:54Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 452bbcf22a29e92fbb00967068fa7a9298212f02f99114c3aa551d6fdbccc600
role: another answer on the same question, kept as context; not my work
---

# Answer by [Md. Fazlul Hoque](https://stackoverflow.com/users/12848411) — 2022-10-31

Posted on Stack Overflow, <https://stackoverflow.com/a/74265392>, 2022-10-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can just invoke the `get_text()` method to grab the entire description

    from bs4 import BeautifulSoup
    import requests
    page = requests.get("https://www.booklooker.de/Bücher/Bastian-Sick+Der-Dativ-ist-dem-Genitiv-sein-Tod-Ein-Wegweiser-durch-den-Irrgarten-der-deutschen/id/A02ArCkS01ZZy")
        
    souped = BeautifulSoup(page.content, "html.parser")
    description = souped.find(class_="propertyItem_13").get_text(strip=True)
    
    print(description)

**Output:**


    Beschreibung:Zustand siehe Bild. Zusätzlich: Ecken und Kanten leicht bestoßen. Seiten und Buchschnitt altersbedingt 
    leicht verfärbt. Buchschnitt fleckig, siehe Bilder. Ab der Hälfte des Buches sind die Seiten oben leicht gebogen.Die deutsche Sprache kennt zwar nur vier Fälle, dafür aber über tausend Zweifelsfälle. Heißt es Pizzas oder Pizzen? Gewinkt oder gewunken? Wann schreibt man Storys und wann Stories? Hat der Genitiv noch eine Chance — trotz des Dativs und dem Dativ zum Trotz?Dieses Buch präsentiert die großartige SPIEGEL¬ONLINE-Kolumne »Zwiebelfisch«, die Woche für Woche Leser amüsiert, schockiert, belehrt und begeistert.»Man spürt das Vergnügen, das der Umgang mit gutem Deutsch bereitet.« FAZ»Wo der Duden nicht weiter weiß, weiß Sick Rat.« Saarbrücker ZeitungÜber das Buch:Die oder das Nutella 
    — diese Frage hat schon viele Gemüter am Frühstückstisch bewegt. Der, die, das — wieso, weshalb, warum? Ob Nutella nun weiblich oder sächlich ist, ist sicherlich keine Frage auf Leben und Tod, aber eine Antwort hätten wir schon gern. Wir? Ja, wir hilflos Verlorenen im Labyrinth der deutschen Sprache. Wir, die wir unsere liebe Not mit der deutschen Sprache haben. Und leichter, verständlicher oder zumindest nachvollziehbarer ist es nach der Rechtschreibreform auch nicht geworden.In seinen hinreißend komischen und immer klugen Kolumnen bringt Bastian Sick Licht ins Dunkel der 
    deutschen Sprachregelungen und sortiert den Sprachmüll. Ist der inflationären Verwendung von Binde-strichen noch Einhalt zu gebieten, angesichts von Spar-Plänen und Quoten-Druck? Versinken wir sprachlich gesehen nicht längst im Hagel der Apostrophe, wenn Känguru's plötzlich in den Weiten Australien's leben? Derlei Unsinn scheint nicht mehr aufhaltbar, wenn es nicht dieses Buch gäbe. Darauf zwei Espressis!Der Autor:Bastian Sick, Jahrgang 1965, Studium der Geschichtswissenschaft und Romanistik, Tätigkeit als Lektor und Übersetzer; von 1995-1998 Dokumentationsjournalist beim SPIEGEL-Verlag, ab Januar 1999 Mitarbeiter der Redaktion von SPIEGEL ONLINE. Seit Mai 2003 dort Autor der Kolumne »Zwiebelfisch«.
