# Code from my Stack Overflow answer https://stackoverflow.com/a/75925193 (posted 2023-04-04), extracted verbatim; may need the question's context to run.
import itertools

def get_compositions(raw_materials:list, factor_x:int,lim_y:int,col_prefix='Material '):
    multiples = [factor_x*i for i in range(int(lim_y/factor_x)+1)]
    cart_prod = itertools.product(multiples, repeat=len(raw_materials))
    composites = [c for c in cart_prod if sum(c)<=lim_y] ## filter

    composite_labels = [f'Composite{i}' for i in range(1, len(composites)+1)]
    material_labels = [f'{col_prefix}{m}' for m in raw_materials]

    return pd.DataFrame(composites, index=composite_labels, columns=material_labels)
