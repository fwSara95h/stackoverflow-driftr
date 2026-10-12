# Code from my Stack Overflow answer https://stackoverflow.com/a/75288482 (posted 2023-01-30), extracted verbatim; may need the question's context to run.
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
