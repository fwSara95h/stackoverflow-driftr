# Code from my Stack Overflow answer https://stackoverflow.com/a/75623892 (posted 2023-03-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# !pip install colorama
# from colorama import Fore, Back, Style
input_dict = {'key1': 217, 'key2': 2, 'key3': 9, 'key4': 4, 'key5':6}

colored_dict = {k: f'{Fore.RED if v>5 else Fore.GREEN}{v}' for k, v in input_dict.items()}

# --- block 2 ---
> {'key1': '\x1b[31m217',
>  'key2': '\x1b[32m2',
>  'key3': '\x1b[31m9',
>  'key4': '\x1b[32m4',
>  'key5': '\x1b[31m6'}
>

# --- block 3 ---
for key in input_dict:
    if input_dict[key] > 5:
        print(repr(key)+':', Fore.RED, input_dict[key], Fore.RESET)
        # print input_dict with integer values in red color #
    else:
        print(repr(key)+':', Fore.GREEN, input_dict[key], Fore.RESET)
        # print input_dict with integer values in green color #

# --- block 4 ---
## setup
thresh, cHi, cLo = 5, Fore.RED, Fore.GREEN
cKey, cNorm = Fore.BLUE, Fore.RESET ## set Fore.RESET for cKey as well to NOT color keys
input_dict = {'key1': 217, 'key2': 2, 'key3': 9, 'key4': 4, 'key5': 6}
def colorFunc(kx, vx): 
    return cKey+repr(kx)+': '+(cHi if vx>thresh else cLo)+repr(vx)+cNorm

# --- block 5 ---
# one line:
print('{', ', '.join(colorFunc(k,v) for k,v in input_dict.items()), '}', sep='')

# --- block 6 ---
# multi-line:
print('{\n ', ',\n '.join(colorFunc(k,v) for k,v in input_dict.items()), '\n}', sep='')
