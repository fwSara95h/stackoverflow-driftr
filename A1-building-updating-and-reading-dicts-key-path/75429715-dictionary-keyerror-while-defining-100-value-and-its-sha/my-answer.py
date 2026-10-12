# Code from my Stack Overflow answer https://stackoverflow.com/a/75441653 (posted 2023-02-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
output = [sha256(str(n).encode('utf-8')) for n in range(100)]
dictionary = dict([(str(h),i) for i, h in enumerate(output)])

# --- block 2 ---
> {'<sha256 HASH object @ 0x7fbf1cf33cd0>': 0,
>  '<sha256 HASH object @ 0x7fbf1cf33c90>': 1,
>  '<sha256 HASH object @ 0x7fbf1cf33ad0>': 2,
>  '<sha256 HASH object @ 0x7fbf1cf33c30>': 3,
>  '<sha256 HASH object @ 0x7fbf1cf33a30>': 4,
>               ......
>               
>  '<sha256 HASH object @ 0x7fbf1e066790>': 95,
>  '<sha256 HASH object @ 0x7fbf1e0667b0>': 96,
>  '<sha256 HASH object @ 0x7fbf1e0667d0>': 97,
>  '<sha256 HASH object @ 0x7fbf1e066810>': 98,
>  '<sha256 HASH object @ 0x7fbf1e066830>': 99}
>

# --- block 3 ---
> {'<sha256 HASH object @ 0x7fbf1de87550>': 0,
>  '<sha256 HASH object @ 0x7fbf1de87c30>': 1,
>  '<sha256 HASH object @ 0x7fbf1de87b30>': 2,
>  '<sha256 HASH object @ 0x7fbf1de875d0>': 3,
>  '<sha256 HASH object @ 0x7fbf1de87850>': 4,
>               ......
> 
>  '<sha256 HASH object @ 0x7fbf1e066a10>': 95,
>  '<sha256 HASH object @ 0x7fbf1e066a30>': 96,
>  '<sha256 HASH object @ 0x7fbf1e066a50>': 97,
>  '<sha256 HASH object @ 0x7fbf1e066a70>': 98,
>  '<sha256 HASH object @ 0x7fbf1e066a90>': 99}
>

# --- block 4 ---
> {'5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9': 0,
>  '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b': 1,
>  'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35': 2,
>  '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce': 3,
>  '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a': 4,
>                                 ......
> 
>  'ad48ff99415b2f007dc35b7eb553fd1eb35ebfa2f2f308acd9488eeb86f71fa8': 95,
>  '7b1a278f5abe8e9da907fc9c29dfd432d60dc76e17b0fabab659d2a508bc65c4': 96,
>  'd6d824abba4afde81129c71dea75b8100e96338da5f416d2f69088f1960cb091': 97,
>  '29db0c6782dbd5000559ef4d9e953e300e2b479eed26d887ef3f92b921c06a67': 98,
>  '8c1f1046219ddd216a023f792356ddf127fce372a72ec9b4cdac989ee5b0b455': 99}
>

# --- block 5 ---
> {b"_\xec\xebf\xff\xc8o8\xd9Rxlmily\xc2\xdb\xc29\xddN\x91\xb4g)\xd7:'\xfbW\xe9": 0,
>  b'k\x86\xb2s\xff4\xfc\xe1\x9dk\x80N\xffZ?WG\xad\xa4\xea\xa2/\x1dI\xc0\x1eR\xdd\xb7\x87[K': 1,
>  b'\xd4s^:&^\x16\xee\xe0?Yq\x8b\x9b]\x03\x01\x9c\x07\xd8\xb6\xc5\x1f\x90\xda:fn\xec\x13\xab5': 2,
>  b'N\x07@\x85b\xbe\xdb\x8b`\xce\x05\xc1\xde\xcf\xe3\xad\x16\xb7"0\x96}\xe0\x1fd\x0b~G)\xb4\x9f\xce': 3,
>  b'K"ww\xd4\xdd\x1f\xc6\x1co\x88OHd\x1d\x02\xb4\xd1!\xd3\xfd2\x8c\xb0\x8bU1\xfc\xac\xda\xbf\x8a': 4,
>                                .................
> 
>  b'\xadH\xff\x99A[/\x00}\xc3[~\xb5S\xfd\x1e\xb3^\xbf\xa2\xf2\xf3\x08\xac\xd9H\x8e\xeb\x86\xf7\x1f\xa8': 95,
>  b"{\x1a'\x8fZ\xbe\x8e\x9d\xa9\x07\xfc\x9c)\xdf\xd42\xd6\r\xc7n\x17\xb0\xfa\xba\xb6Y\xd2\xa5\x08\xbce\xc4": 96,
>  b'\xd6\xd8$\xab\xbaJ\xfd\xe8\x11)\xc7\x1d\xeau\xb8\x10\x0e\x963\x8d\xa5\xf4\x16\xd2\xf6\x90\x88\xf1\x96\x0c\xb0\x91': 97,
>  b')\xdb\x0cg\x82\xdb\xd5\x00\x05Y\xefM\x9e\x95>0\x0e+G\x9e\xed&\xd8\x87\xef?\x92\xb9!\xc0jg': 98,
>  b"\x8c\x1f\x10F!\x9d\xdd!j\x02?y#V\xdd\xf1'\xfc\xe3r\xa7.\xc9\xb4\xcd\xac\x98\x9e\xe5\xb0\xb4U": 99}
>
