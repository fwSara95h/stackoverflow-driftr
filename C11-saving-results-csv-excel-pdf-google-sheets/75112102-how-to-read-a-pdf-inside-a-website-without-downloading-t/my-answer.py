# Code from my Stack Overflow answer https://stackoverflow.com/a/75115427 (posted 2023-01-14), extracted verbatim; may need the question's context to run.
# import io, tabula
pdfUrl = 'https://www.premera.com/documents/052166_2023.pdf'
r = requests.get(pdfUrl, headers={'user-agent': 'Mozilla/5.0'})
r.raise_for_status()
tabula.read_pdf(io.BytesIO(r.content), pages='6')[0]
