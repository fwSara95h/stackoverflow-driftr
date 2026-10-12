# Code from my Stack Overflow answer https://stackoverflow.com/a/75666201 (posted 2023-03-07), extracted verbatim; may need the question's context to run.
df = pd.DataFrame.from_dict({
  'type': { 4: 'Second Product', 5: 'table', 6: 'First Product', 7: 'chair',
            8: 'Second Product', 9: 'desk', 10: 'First Product', 11: 'chair' },
  'id': { 4: 'cust1', 5: 'cust1', 6: 'cust1', 7: 'cust1',
          8: 'cust2', 9: 'cust2', 10: 'cust2', 11: 'cust2' }
})

itpZip = list(zip(df['id'][::2], df['type'][::2], [*df['type'][1::2], None]))
getProdTypes = lambda c: set(ctp[1] for ctp in itpZip if c==ctp[0])
custProdTypes = {ci: getProdTypes(ci) for ci in set(df['id'][::2])}
df = pd.DataFrame([{
    'cust': ci, **{ti:', '.join(
        p for c,t,p in itpZip if c==ci and t==ti
      ) for ti in getProdTypes(ci)}
} for ci in set(df['id'][::2])])
