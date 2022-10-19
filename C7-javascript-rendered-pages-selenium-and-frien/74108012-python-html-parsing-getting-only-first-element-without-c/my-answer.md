---
title: "Python HTML parsing getting only first element without childs"
site: stackoverflow
question_id: 74108012
answer_id: 74119968
url: https://stackoverflow.com/a/74119968
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-19T04:41:54Z
last_edited: 2022-10-19T19:19:27Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74119968/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [linkToSoup]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ee7bec1bb74741bde913dca9fcb6bf2864a88e6b4bb24b387f9ea6b59a34119b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-19

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74119968>, 2022-10-19, last edited 2022-10-19; **accepted**; score 1. Text as retrieved 2026-10-12.

If you're willing to give selenium another try, I use this function in several of my scraping projects:

```python
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def linkToSoup_selenium(l, ecx=None, clickFirst=None):
    try:
        driver = webdriver.Chrome('chromedriver.exe')
        # I copy chromedriver.exe to the same folder as this py file

        driver.get(l) # go to link

        # if something needs to be confirmed by click
        if clickFirst:
            WebDriverWait(driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, clickFirst))
            )
            driver.find_element(By.XPATH, clickFirst).click()

        # if some section needs to be loaded first
        if ecx:
            WebDriverWait(driver, 25).until(
                EC.visibility_of_all_elements_located((By.XPATH, ecx)))

        lSoup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.close()
        del driver
        return lSoup
    except Exception as e:
        print(str(e))
        return None
```

It's been useful for several sites protected by blockers like cloudflare, or sites like the one in your question where parts are rendered after the initial load, or where you might have to click some kind of pop up about age/cookies/etc first.

<hr>

In your case, you can use the function to get the bs4 tree after your target section has been loaded. For example if you needed something from the *"TEXTO"* section
[![enter image description here][1]][1]

you could call the function with the [xpath](https://www.guru99.com/xpath-selenium.html) for any paragraph in that section:
```python
soup = linkToSoup_selenium(
    l = 'https://dre.pt/dre/detalhe/anuncio-concurso-urgente/491-2022-201313437',
    ecx = '//div[@id="transitionContainer"]//div[@data-container]//div[@data-container]/p'
    # clickFirst argument is not necessary for this site
)
```
[If you need it, [this](https://devhints.io/xpath) is a good cheatsheet for xpath.]

Once you have `soup`, you can extract the data you need from it - for example,
```python
if soup is not None: 
    numbered = soup.find_all(lambda t: t.name == 'p' and
        t.text.count(' - ') > 0 and t.text.split(' - ')[0].isdigit())
        
    for n in numbered:
        print(n.get_text(strip=True))
```
will output
```lang-none
1 - IDENTIFICAÇÃO E CONTACTOS DA ENTIDADE ADJUDICANTE
2 - OBJETO DO CONTRATO
3 - INDICAÇÕES ADICIONAIS
4 - LOCAL DA EXECUÇÃO DO CONTRATO
5 - DIVISÃO EM LOTES, SE FOR O CASO
6 - PRAZO DE EXECUÇÃO DO CONTRATO
7 - DOCUMENTOS DE HABILITAÇÃO
8 - CONDIÇÕES DE PARTICIPAÇÃO
9 - ACESSO ÀS PEÇAS DO CONCURSO E APRESENTAÇÃO DAS PROPOSTAS
10 - PRAZO PARA APRESENTAÇÃO DAS PROPOSTAS
11 - CRITÉRIO DE ADJUDICAÇÃO
12 - IDENTIFICAÇÃO E CONTACTOS DO ÓRGÃO DE RECURSO ADMINISTRATIVO
13 - DATA E HORA DE ENVIO DO ANÚNCIO PARA PUBLICAÇÃO NO DIÁRIO DA REPÚBLICA
14 - IDENTIFICAÇÃO DO(S) AUTOR(ES) DO ANÚNCIO
```

  [1]: https://i.sstatic.net/6oACF.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[NukeSkull](https://stackoverflow.com/users/16664550)** (2022-10-19): Will give it a try since ScrapingAnt only allows for a certain number of requests before paying, thanks a lot for the code and the explanation!
- **[NukeSkull](https://stackoverflow.com/users/16664550)** (2022-10-19): A question I have about the code, what does the `del driver` before the return does? Have been thinking about it and can't figure it out, you're only declaring a variable right but not using it?
- **me** (2022-10-19): sorry about the headscratcher, that's just a paranoid thing I do. [btw I'm *deleting* driver after having extracted what I want as `lSoup`] - there was a time when my version of selenium had this weird glitch where `driver.close()`/`.quit()` wouldn't work fully and if I didn't add `del driver` the program wouldn't terminate without Ctrl+C....It's likely totally redundant here since driver is being initiated within a function, so it gets discarded at the end anyway
