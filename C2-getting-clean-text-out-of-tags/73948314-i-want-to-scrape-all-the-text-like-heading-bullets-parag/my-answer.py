# Code from my Stack Overflow answer https://stackoverflow.com/a/73952457 (posted 2022-10-04), extracted verbatim; may need the question's context to run.
for items in soup.select('article.article'):
tags = [
      t for t in items.find_all(["h6","h5","h4","h3","h2","h1","p","li"]) 
      if not (t.name in ['p', 'li'] and (
          ('class' in t.attrs and t.attrs['class']) or
          ('id' in t.attrs and t.attrs['id'])
      ))
  ] # filtered out "Share..." and "Last Updated..."
  tLen = len(tags)
  for i in list(range(tLen))[::-1]: #counting down from last tag
    if tags[i].name == 'h3': 
      tags = tags[:i]
      break

  articleText = '\n'.join([t.text for t in tags])
  print(articleText)
