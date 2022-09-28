---
title: "how to get source of img tags inside a web link with beautiful soup 4"
site: stackoverflow
question_id: 73887038
answer_id: 73887232
url: https://stackoverflow.com/a/73887232
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2022-09-28T20:06:42Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dfc1a29a6eeaa8cb7b148ed2e57a2346444e68a774b698937f060c199654de54
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2022-09-28

Posted on Stack Overflow, <https://stackoverflow.com/a/73887232>, 2022-09-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Try:

```py
from bs4 import BeautifulSoup
import requests

r = requests.get("https://welovemanga.one/2777/92578/")
soup = BeautifulSoup(r.content, "html.parser")
thumbnail_elements = soup.select("img[data-original]")

for element in thumbnail_elements:
    print(
        "https://welovekai.com/proxy.php?link="
        + element["data-original"].replace("\n", "").replace("\r", "")
    )
```

Prints:

```none
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/ec494844bf563848fce377bbac9d3bda02.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/c30814d84e53a829bd9df51c5172fbea03.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/356e0b2a3136e9e96dfb45e853b59d8804.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/9dd38d6c86ea251f7c94a8068159ef5005.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/2abc410ebd0b20a616259d8cb97346dd06.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/9c0a6b7bb3074492ee60d231ae5c274707.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/42311919da2dfe95d84bcbcfe04e7ef908.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/d9597e5c42062aaa985d30bf04c1228a09.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/6c1506e7eb266d61704d4b12d382175c10.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/81dd5dfe2b3f9342d7844bae1bfd0e7511.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/4569ec54e73e6fbfde5bba34efeb03cc12.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/5561070bf5ba4c60a6361ea0a2ea5f5413.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/eb750f3fa928772123bfd79caee9417c14.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/96eaed5a915a569c2a4801eb4cb6305d15.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/d922922310736e03e2b2d29301257d9e16.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/c3256b2c7b0fa0ee1e21c2dacab79d7b17.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/fc7d0d602d0a6af29e7a860ed755304318.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/438d5e604808145a5a6cc938f77310b719.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/a3e046e32b66eb48d71a1256a6ba867e20.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/1469b4a25095ccba7590f4ae0e9cb57221.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/4fbf57627d2738b7229fc5b71f18215a22.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/a71fc439dc40716fbfd8f570565f80bf23.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/3a49068b55e340b703722bdd61912c4924.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/30356fd4bbcf29f820f0659f48a7dc5a25.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/23f35eba985165d6ca2f24d56c12d3be26.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/88a2f7c73927cd1ec22bf09134c6930427.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/ed13005b950bcdd4411863aeecdb4c5b28.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/dbbb12f95af8242ada32c3040e9e374229.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/b75a24be2234dcb6345ac19a83eae68230.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/4aa9d31b25db17bf16c7af4962a89c9b31.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/0fdf030b478f81bd07fab8e02e3a100232.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/288c74bde23a8891c818588eae0bc00b33.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/65623e5f600e30df804d9242d3b9ae8c34.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/00f9b77c213a7bfe6e52fbdfa1418b6635.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/e6ed988baab8eaab2f3949671d6c415536.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/da888a2fcff33d94aad4c2a3ffd8c95b37.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/0287564880c8564c17232234f484f1ab38.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/b6425ffe6bc6df44c61660aac761c03239.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/6d221db676c78f6e4bc35d28d40a870040.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/b3fef706e4dd4eccc9425113360bb75541.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/9026f984ab924b8ac131509900e32efe42.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/8dbf0ccdf3827ad85dcac5558228270e43.jpg&site=mm2r.net
https://welovekai.com/proxy.php?link=https://ihlv1.xyz/images2/20220914/c31f203e603905bcdb360301b445d7e644.jpg&site=mm2r.net
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Moon](https://stackoverflow.com/users/14873033)** (2022-09-28): thanks, it worked! But why the 2 replaces?
- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2022-09-28): @Moon The attribute `data-original=` contains some special charts that I don't want to include in the final link.
