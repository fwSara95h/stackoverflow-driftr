# Code from my Stack Overflow answer https://stackoverflow.com/a/75896900 (posted 2023-03-31), extracted verbatim; may need the question's context to run.
getSingle = lambda l: l[0] if isinstance(l,list) and len(l)==1 else l
getName = lambda x: ','.join([getSingle(dict_name.get(c,c)) for c in x.split(',')])
for_ag_pivot['name_cod'] = for_ag_pivot['cod_last'].apply(getName)
