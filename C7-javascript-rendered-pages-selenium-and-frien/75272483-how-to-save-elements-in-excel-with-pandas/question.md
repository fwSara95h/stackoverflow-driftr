---
title: "How to save elements in excel with pandas?"
site: stackoverflow
question_id: 75272483
url: https://stackoverflow.com/q/75272483
asked: 2023-01-29T03:46:48Z
asked_by: "Felipe"
asked_by_url: https://stackoverflow.com/users/20021812
last_edited: 2023-01-29T04:09:09Z
tags: [python, selenium, web-scraping]
score: 0
views_at_snapshot: 58
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 87f85c37bfdf06316e8dc334ca6f1eaa9e3b9874117410a5087fc7d6237d1151
---

# How to save elements in excel with pandas?

Asked by [Felipe](https://stackoverflow.com/users/20021812) on Stack Overflow, <https://stackoverflow.com/q/75272483>, 2023-01-29, last edited 2023-01-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

My code does the following:

1st enter the site

2nd collects the links and saves in a dictionary

3rd the code enters the links saved in the dictionary to extract the elements and also saves in a dictionary

4th finally it saves the information of the elements that are in the dictionary in excel pandas

Problem:
Some pages do not contain information to be extracted, it is probably a bug on the site, so pandas does not save the information already collected.

Here's the error:

    valueerror: all arrays must be of the same length



Here's part of my code, I didn't put it in full so it wouldn't get long.

I'm using selenium.

    links = []
    imagem = []
    pacote = []
    
    counter = 1
    for linkAtual in links:
        driver.get(linkAtual)
        try:
            driver.find_element(
                By.XPATH, "//button[normalize-space()='Ir para a oferta']").click()
            sleep(2)
        except:
            print("proxima pagina")
    
        try:
            titulo = driver.find_element(By.TAG_NAME, "h1")
            print(titulo.text)
    
            pacote.append(titulo.text.replace("Pacote de Viagem - ", "").replace("+", " e ").replace("2022", "").replace(
                "2023", "").replace("2024", "").replace("2025", "").replace("(", "").replace(")", "").replace("-", ""))
    
            print("baixar imagem ")
            primeiro_caminho = driver.find_element(By. XPATH, "(//img)[2]")
            atributoSrc = primeiro_caminho.get_attribute("src")
            # file_name = f"{titulo}{counter:02d}.jpg"
            file_name = f"image{counter:02d}.jpg"
            imagem.append(atributoSrc)
            urllib.request.urlretrieve(
                atributoSrc, f"C:\\__Imagens e Planilhas Python\\Afiliacoes\\Fotos\\{file_name}")
            counter += 1
        except:
            print("não tem conteudo")
    
    
    data = {'Pacote': pacote, 'Link Afiliado': links}
    #df = pd.DataFrame.from_dict(data, orient="index")
    df = pd.DataFrame(data)
    df.to_excel(r"C:\__Imagens e Planilhas Python\Afiliacoes\pacotes.xlsx",engine='xlsxwriter')
    print(df)




Page that doesn't work I found one, it has 300 links and about 4 that don't have information:

Here is an example of an error link:

https://www.hurb.com/br/packages/la-romana-passagem-aerea-hospedagem/1416419?utm_source=Felipe-F-clubehurb&utm_medium=clubehu-promotion&utm_campaign=689696&cmp=689696

Here are examples of valid links:

https://www.hurb.com/br/packages/costa-do-sauipe-passagem-aerea-hospedagem-all-inclusive/1421105?utm_source=Felipe-F-clubehurb&utm_medium=clubehu-product&utm_campaign=689696&cmp=689696

https://www.hurb.com/br/packages/rio-de-janeiro-passagem-aerea-hospedagem/1407451?utm_source=Felipe-F-clubehurb&utm_medium=clubehu-product&utm_campaign=689696&cmp=689696

https://www.hurb.com/br/packages/pacote-aereo-hospedagem-dubrovnik/1419049?utm_source=Felipe-F-clubehurb&utm_medium=clubehu-product&utm_campaign=689696&cmp=689696

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Nehal Birla](https://stackoverflow.com/users/8953284)** (2023-01-29): For the values that were not collected while web scapping add np.nan for them
- **[Felipe](https://stackoverflow.com/users/20021812)** (2023-01-29): could you give me an example of how to do this?
- **[Nehal Birla](https://stackoverflow.com/users/8953284)** (2023-01-29): can you provide me 5-6 links (both working and not working)? I will edit and share the code.
- **[Nehal Birla](https://stackoverflow.com/users/8953284)** (2023-01-29): Just append an empty string or `np.nan` in pacote inside the second except where you are printing não tem conteudo
