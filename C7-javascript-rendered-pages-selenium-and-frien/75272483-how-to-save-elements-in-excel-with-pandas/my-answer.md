---
title: "How to save elements in excel with pandas?"
site: stackoverflow
question_id: 75272483
answer_id: 75288482
url: https://stackoverflow.com/a/75288482
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-30T18:12:07Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75288482/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 12d26cd33df5817dac8cc73ba902e11928fbed2b2fbd247396aefcab0b43ffaf
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75288482>, 2023-01-30; score 0. Text as retrieved 2026-10-12.

you could edit your 2nd `try...except` block to

```python
    titlTxt, atributoSrc = None, None # initiate/clear as null
    try:
        titulo = driver.find_element(By.TAG_NAME, "h1")
        print(titulo.text)

        # pacote.append... # outside block
        titlTxt = titulo.text.replace("Pacote de Viagem - ", "").replace("+", " e ").replace("2022", "").replace(
            "2023", "").replace("2024", "").replace("2025", "").replace("(", "").replace(")", "").replace("-", "")

        print("baixar imagem ")
        primeiro_caminho = driver.find_element(By. XPATH, "(//img)[2]")
        atributoSrc = primeiro_caminho.get_attribute("src")
        # file_name = f"{titulo}{counter:02d}.jpg"
        file_name = f"image{counter:02d}.jpg"
        # imagem.append(atributoSrc) # outside block
        urllib.request.urlretrieve(
            atributoSrc, f"C:\\__Imagens e Planilhas Python\\Afiliacoes\\Fotos\\{file_name}")
        counter += 1
    except:
        print("não tem conteudo")

    pacote.append(titlTxt)
    imagem.append(atributoSrc) 
```

so now `pacote` and `imagem` should have exactly one item [each] corresponding to each item in `links`, so all 3 lists can be expected to be of the same length. 

(If you had separate `try...except` blocks for each list, you could `append` in both `try` and in `except`; but when extracting for multiple lists in the same `try`, some of them might already be appended to before raising an exception, so appending in `except` as well risks adding to the same list twince in a single loop.)
