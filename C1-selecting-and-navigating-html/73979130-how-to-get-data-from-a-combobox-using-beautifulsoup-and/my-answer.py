# Code from my Stack Overflow answer https://stackoverflow.com/a/73980579 (posted 2022-10-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
sexo = BeautifulSoup(login_request.text, 'lxml').select_one('select[name=sexo] option[selected]').get_text(strip=True)

# --- block 2 ---
selectedOpts = BeautifulSoup(login_request.text, 'lxml').select('select[name=sexo] option[selected]')
selectedOpts = [s for s in selectedOpts if s.get('value')]
sexo = selectedOpts[0] if selectedOpts else None
