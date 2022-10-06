---
title: "How to get data from a combobox using Beautifulsoup and Python?"
site: stackoverflow
question_id: 73979130
url: https://stackoverflow.com/q/73979130
asked: 2022-10-06T19:29:26Z
asked_by: "AjaxPain"
asked_by_url: https://stackoverflow.com/users/20092462
last_edited: 2022-10-06T19:40:36Z
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 322
answer_count: 1
accepted_answer_id: 73980579
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6187f22ad010b269f21091986751318b0eaf3b611a60db3533743cf81388e8d6
---

# How to get data from a combobox using Beautifulsoup and Python?

Asked by [AjaxPain](https://stackoverflow.com/users/20092462) on Stack Overflow, <https://stackoverflow.com/q/73979130>, 2022-10-06, last edited 2022-10-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Im trying to get the selected text from a combobox.
I was using asfad to search the text for the "selected" state but in the source code there are two items with that state, and I only want the one that is selected.

I am using the following code to search for it by the "span" and the id but I get the following:

    login_request = session.post(url,data=payload, headers=headers, 
    cookies=cookies)
    sexo = BeautifulSoup(login_request.text, 'lxml').find("span",id="sexo- 
    button").get_text(strip=True)
    print(sexo)


> Error: 'NoneType' object has no attribute 'get_text'

And it was also looking for it in the following way, obtaining a "none"

    login_request = session.post(url,data=payload, headers=headers, 
    cookies=cookies)
    sexo = BeautifulSoup(login_request.text, 'lxml').select('select[name=sexo] option[selected]') 
    [0].value
    print(sexo)


Origin:

    <tr class="FacetFilaTD"><td class="FacetDataTDPADL5">Sexo</td><td colspan="3" 
    class="FacetFieldCaptionTD">
    <div class="control-valid"><select name="sexo" style="width: 140px; display: none;" id="sexo" 
    class="clasecombo_valid" tabindex="0" aria-disabled="false">
    <option selected="" value="">[SELECCIONAR]</option><option value="M" 
    selected="">Masculino</option><option value="F">Femenino</option></select><span><a class="ui- 
    selectmenu ui-widget ui-state-default ui-selectmenu-dropdown ui-state-active ui-corner-top" 
    id="sexo-button" role="button" href="#nogo" tabindex="0" aria-haspopup="true" aria-owns="sexo- 
    menu" aria-disabled="false" style="width: 140px;"><span class="ui-selectmenu- 
    status">Masculino</span><span class="ui-selectmenu-icon ui-icon ui-icon-triangle-1-s"></span> 
    </a></span><span class="requerido">*</span></div>                                                                      
    </td></tr>

I just want to get the selected item which in this case is "Masculino"
