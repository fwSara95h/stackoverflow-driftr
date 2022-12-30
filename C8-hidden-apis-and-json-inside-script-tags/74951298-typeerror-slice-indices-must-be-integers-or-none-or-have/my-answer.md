---
title: "TypeError: slice indices must be integers or None or have an __index__ method error in scraping a help page"
site: stackoverflow
question_id: 74951298
answer_id: 74961326
url: https://stackoverflow.com/a/74961326
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-30T12:03:55Z
last_edited: 2022-12-30T14:20:21Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74961326/revisions
accepted: true
score: 1
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-json-in-script
helpers_referenced: [findObj_inJS]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e2acdf8fc241587c123ebf5a3cc2f38233c4e2490ff90949f9932955f90c7403
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74961326>, 2022-12-30, last edited 2022-12-30; **accepted**; score 1. Text as retrieved 2026-10-12.

**Note:** Since I'm unfamiliar with and failed to install `Essentials`, and also because *`""https://www.facebook.com:443/help""`* **raises a syntax error** (there should only be one quote on each side of the string), I changed the `requests` line in my code. 

```python
        cont = requests.get('https://www.facebook.com:443/help', headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})
```

---

> ```python
> TypeError: slice indices must be integers or None or have an __index__ method
> ```

You've initiated `start` as a string [*`start = ""`*] and it needs to be an integer. Unless the *`if text[i].get_text().find('__bbox":') != -1....`* block is entered, `start` remains a string.

if you just want to not get this error, you could just exit the program if `start` hasn't been updated [indicating that `__bbox":` wasn't found in any of the `script` tags].

```python
        print('start:', start)
        if start == "":
            print('{__bbox":} not found')
            return

        count = 0
```

But that still leaves the problem of `__bbox":` not being found; I'm not sure *why*, but the issue is resolved for me if I don't use the `html5lib` parser - just changing to **`BeautifulSoup(cont.content)`** resolved *this* issue.

```python
        # soup = bs4.BeautifulSoup(cont.content, "html5lib")
        soup = bs4.BeautifulSoup(cont.content) # don't define the parser 
        # soup = bs4.BeautifulSoup(cont.content, "html.parser") # you could also try other parsers
```

---
---

#### Other suggestions

Your code will probably work without these, but you might want to consider these suggested improvements for error-handling:

---

***Filter the `script` Tags***

If the `text` ResultSet only has `script` tags that contain `__bbox":`, you avoid looping unnecessarily through the 100+ other `script`s, and you won't have to check with `if....find('__bbox":')` anymore.

```python
        text = soup.find_all(lambda t: t.name == 'script' and '"__bbox"' in t.get_text())

        for mystr in [s.get_text() for s in text]:
            print("this is: ", mystr.find('__bbox":'))
            txtstr += mystr
            start = mystr.find('__bbox":') + len('__bbox":') 
```

---

***Initiate `end`***

You should initiate the `end` variable [like `end = 0`] before the *`for end, char ...`* loop because you're using it after the loop as well.

> ```python
>         print('end:', end)
> ```
> ```python
>         data = json.loads(txtstr[start:end+1])
> ```

If `txtstr[start:]` is empty somehow, these lines will raise error/s since `end` would not be defined yet.

---

***Use a JavaScript Parser***

This will make the previous suggestions unnecessary, but as it is `json.loads` will raise an error if `txtstr[start:end+1]` is empty somehow, or if it contains any unpaired [and likely escaped] `}`or`{`. So, it might be more reliable to use a parser rather than just trying to walk through the string.

I have [this function](https://pastebin.com/UVcLniSG) that uses [`slimit`](https://pypi.org/project/slimit/) to find values from strings containing JavaScript code. (It's far from perfect, but it seems to for this script, at least.) `GetIDs()` could be re-written as below.

```python
# import json, requests, bs4, slimit
# from slimit.visitors import nodevisitor 
# def findObj_inJS... ## PASTE FROM https://pastebin.com/UVcLniSG

# class CmsIDs:
    def GetIDs():
        # cont=requests.get('https://www.facebook.com:443/help',headers=Static.headers)
        cont = requests.get('https://www.facebook.com:443/help', headers={
            'accept': ';'.join(
                [ 'text/html,application/xhtml+xml,application/xml',
                  'q=0.9,image/avif,image/webp,image/apng,*/*',
                  'q=0.8,application/signed-exchange',
                  'v=b3', 'q=0.9'  ])})

        ## in case of request errors ##
        try: cont.raise_for_status()
        except Exception as e:
            print('failed to fetch page HTML -', type(e), e)
            return
        print('fetched', cont.url, 'with', cont.status_code, cont.reason)

        soup = bs4.BeautifulSoup(cont.content)
        scrCond = lambda t: t.name == 'script' and '"__bbox"' in t.get_text()
        jScripts = [s.get_text() for s in soup.find_all(scrCond)] 
        print(f'Found {len(jScripts)} script tags containing {{"__bbox"}}')

        data = [findObj_inJS(s,'"__bbox"') for s in jScripts]
        print('--- search ---')
        CmsIDs.search(data) 

    # def search(data)....
```

---

***Return the Data***

This isn't for error-handling, but if you return the data printed by `CmsIDs.search` you could save it for further use.

```python
    def search(data):
        rList, dKeys = [], ['cms_object_id', 'cmsID', 'name']
        if isinstance(data, dict):
            dObj = {k: data[k] for k in dKeys if k in data}
            rList += [dObj] if dObj else []

            for k, v in dObj.items(): print(k, v)
            if dObj: print('---')

            for val in data.values(): rList += CmsIDs.search(val)
        if isinstance(data, list):
            for val in data: rList += CmsIDs.search(val)
        return rList
```

The [printed result](https://i.sstatic.net/tzO2v.png) will be the same as before, but if you **change the last line of `GetIDs`** to 

```python
        return CmsIDs.search(data)
```

and then define a variable *`cmsList = CmsIDs.GetIDs()`* then `cmsList` will be a [list of dctionaries](https://i.sstatic.net/wAknk.png), which you could then [for example] save to csv with [`pandas`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) and view as a table on a spreadsheet.

```python
# import pandas
pandas.DataFrame(cmsList).to_csv('CmsIDs_GetIDs.csv', index=False)
```

or [print the markdown](https://i.sstatic.net/u8xh4.png) for the table [of the results I got] below

```python
print(pandas.DataFrame(cmsList, dtype=str).fillna('').to_markdown())
```


| [index]    | cms_object_id    | name                                                                    | cmsID            |
|----:|:-----------------|:------------------------------------------------------------------------|:-----------------|
|   0 |                  | Використання Facebook                                                   |                  |
|   1 | 570785306433644  | Створення облікового запису                                             |                  |
|   2 | 396528481579093  | Your Profile                                                            |                  |
|   3 |                  | Додати й редагувати інформацію у своєму профілі                         | 1017657581651994 |
|   4 |                  | Ваші основна світлина й обкладинка                                      | 1217373834962306 |
|   5 |                  | Поширення дописів у своєму профілі та керування ними                    | 1640261589632787 |
|   6 |                  | Усунення проблем                                                        | 191128814621591  |
|   7 | 1540345696275090 | Додавання в друзі                                                       |                  |
|   8 |                  | Додавання друзів                                                        | 246750422356731  |
|   9 |                  | Люди, яких ви можете знати                                              | 336320879782850  |
|  10 |                  | Control Who Can Friend and Follow You                                   | 273948399619967  |
|  11 |                  | Upload Your Contacts to Facebook                                        | 1041444532591371 |
|  12 |                  | Видалення з друзів чи блокування користувача                            | 1000976436606344 |
|  13 | 312959615934334  | Facebook Dating                                                         |                  |
|  14 | 753701661398957  | Ваша головна сторінка                                                   |                  |
|  15 |                  | How Feed Works                                                          | 1155510281178725 |
|  16 |                  | Control What You See in Feed                                            | 964154640320617  |
|  17 |                  | Like and React to Posts                                                 | 1624177224568554 |
|  18 |                  | Пошук                                                                   | 821153694683665  |
|  19 |                  | Translate Feed                                                          | 1195058957201487 |
|  20 |                  | Memories                                                                | 1056848067697293 |
|  21 | 1071984682876123 | Повідомлення                                                            |                  |
|  22 |                  | Надсилання повідомлень                                                  | 487151698161671  |
|  23 |                  | Переглянути повідомлення й керувати ними                                | 1117039378334299 |
|  24 |                  | Поскаржитися на повідомлення                                            | 968185709965912  |
|  25 |                  | Відеовиклики                                                            | 287631408243374  |
|  26 |                  | Fix a Problem                                                           | 1024559617598844 |
|  27 | 753046815962474  | Reels                                                                   |                  |
|  28 |                  | Watching Reels                                                          | 475378724739085  |
|  29 |                  | Creating Reels                                                          | 867690387846185  |
|  30 |                  | Managing Your Reels                                                     | 590925116168623  |
|  31 | 862926927385914  | Розповіді                                                               |                  |
|  32 |                  | Як створити розповідь і поширити її                                     | 126560554619115  |
|  33 |                  | View and Reply to Stories                                               | 349797465699432  |
|  34 |                  | Page Stories                                                            | 425367811379971  |
|  35 | 1069521513115444 | Світлини й відео                                                        |                  |
|  36 |                  | Світлини                                                                | 1703757313215897 |
|  37 |                  | Відео                                                                   | 1738143323068602 |
|  38 |                  | Going Live                                                              | 931327837299966  |
|  39 |                  | Albums                                                                  | 490693151131920  |
|  40 |                  | Додавання позначок                                                      | 267689476916031  |
|  41 |                  | Усунення проблеми                                                       | 507253956146325  |
|  42 | 1041553655923544 | Відео у Watch                                                           |                  |
|  43 |                  | Перегляд шоу та відео                                                   | 401287967326510  |
|  44 |                  | Fix a Problem                                                           | 270093216665260  |
|  45 | 2402655169966967 | Gaming                                                                  |                  |
|  46 |                  | Gaming on Facebook                                                      | 385894640264219  |
|  47 |                  | Платежі в іграх                                                         | 248471068848455  |
|  48 | 282489752085908  | Сторінки                                                                |                  |
|  49 |                  | Interact with Pages                                                     | 1771297453117418 |
|  50 |                  | Створити сторінку й керувати нею                                        | 135275340210354  |
|  51 |                  | Імена й імена користувачів                                              | 1644118259243888 |
|  52 |                  | Керування налаштуваннями сторінки                                       | 1206330326045914 |
|  53 |                  | Customize a Page                                                        | 1602483780062090 |
|  54 |                  | Publishing                                                              | 1533298140275888 |
|  55 |                  | Messaging                                                               | 994476827272050  |
|  56 |                  | Insights                                                                | 794890670645072  |
|  57 |                  | Banning and Moderation                                                  | 248844142141117  |
|  58 |                  | Усунути проблему                                                        | 1020132651404616 |
|  59 | 1629740080681586 | Групи                                                                   |                  |
|  60 |                  | Join and Choose Your Settings                                           | 1210322209008185 |
|  61 |                  | Post, Participate and Privacy                                           | 530628541788770  |
|  62 |                  | Create, Engage and Manage Settings                                      | 408334464841405  |
|  63 |                  | Керування групою для адміністраторів                                    | 1686671141596230 |
|  64 |                  | Community Chats                                                         | 3397387057158160 |
|  65 |                  | Pages in Groups                                                         | 1769476376397128 |
|  66 |                  | Fix a Problem                                                           | 1075368719167893 |
|  67 | 1076296042409786 | Події                                                                   |                  |
|  68 |                  | Create and Manage an Event                                              | 572885262883136  |
|  69 |                  | View and Respond to Events                                              | 1571121606521970 |
|  70 |                  | Facebook Classes                                                        | 804063877226739  |
|  71 | 833144153745643  | Fundraisers and Donations                                               |                  |
|  72 |                  | Creating a Fundraiser                                                   | 356680401435429  |
|  73 |                  | Пожертва в рамках збору коштів                                          | 1409509059114623 |
|  74 |                  | Особисті збори коштів                                                   | 332739730519432  |
|  75 |                  | For Nonprofits                                                          | 1640008462980459 |
|  76 |                  | Fix a Problem                                                           | 2725517974129416 |
|  77 | 1434403039959381 | Meta Pay                                                                |                  |
|  78 |                  | Платежі в іграх                                                         | 248471068848455  |
|  79 |                  | Payments in Messages                                                    | 863171203733904  |
|  80 |                  | Пожертва в рамках збору коштів                                          | 1409509059114623 |
|  81 |                  | Квитки на заходи                                                        | 1769557403280350 |
|  82 |                  | Monetization and Payouts                                                | 1737820969853848 |
|  83 | 1713241952104830 | Marketplace                                                             |                  |
|  84 |                  | Як працює Marketplace                                                   | 1889067784738765 |
|  85 |                  | Buying on Marketplace                                                   | 272975853291364  |
|  86 |                  | Продаж на Marketplace                                                   | 153832041692242  |
|  87 |                  | Sell with Shipping on Marketplace                                       | 773379109714742  |
|  88 |                  | Using Checkout on Facebook                                              | 1411280809160810 |
|  89 |                  | Групи з купівлі й продажу                                               | 319768015124786  |
|  90 |                  | Get Help with Marketplace                                               | 1127970530677256 |
|  91 | 1642635852727373 | Додатки                                                                 |                  |
|  92 |                  | Manage Your Apps                                                        | 942196655898243  |
|  93 |                  | Видимість і конфіденційність додатка                                    | 1727608884153160 |
|  94 | 866249956813928  | Додатки Facebook для мобільних пристроїв                                |                  |
|  95 |                  | Додаток для Android                                                     | 1639918076332350 |
|  96 |                  | iPhone and iPad Apps                                                    | 1158027224227668 |
|  97 |                  | Facebook Lite App                                                       | 795302980569545  |
|  98 | 273947702950567  | Спеціальні можливості                                                   |                  |
|  99 |                  | Керування обліковим записом                                             |                  |
| 100 | 1573156092981768 | Вхід і пароль                                                           |                  |
| 101 |                  | Вхід в обліковий запис                                                  | 1058033620955509 |
| 102 |                  | Змінення пароля                                                         | 248976822124608  |
| 103 |                  | Виправлення проблеми із входом                                          | 283100488694834  |
| 104 |                  | Завантаження посвідчення особи                                          | 582999911881572  |
| 105 | 239070709801747  | Налаштування облікового запису                                          |                  |
| 106 |                  | Як змінити налаштування облікового запису                               | 1221288724572426 |
| 107 |                  | Ваше ім’я користувача                                                   | 1740158369563165 |
| 108 |                  | Спадкоємці                                                              | 991335594313139  |
| 109 | 1090831264320592 | Імена у Facebook                                                        |                  |
| 110 | 1036755649750898 | Сповіщення                                                              |                  |
| 111 |                  | Push, Email and Text Notifications                                      | 530847210446227  |
| 112 |                  | Виберіть, про що отримувати сповіщення                                  | 269880466696699  |
| 113 |                  | Усунення проблем                                                        | 1719980288275077 |
| 114 | 109378269482053  | Налаштування реклами                                                    |                  |
| 115 |                  | Як працює реклама у Facebook                                            | 516147308587266  |
| 116 |                  | Контроль реклами, яку ви бачите                                         | 1075880512458213 |
| 117 |                  | Ваша інформація та реклама у Facebook                                   | 610457675797481  |
| 118 | 1701730696756992 | Доступ до вашої інформації та її завантаження                           |                  |
| 119 | 250563911970368  | Деактивація або видалення облікового запису                             |                  |
| 120 |                  | Конфіденційність і безпека                                              |                  |
| 121 | 238318146535333  | Ваша конфіденційність                                                   |                  |
| 122 |                  | Керуйте тим, хто може переглядати контент, який ви поширюєте у Facebook | 1297502253597210 |
| 123 |                  | Керування своїми дописами                                               | 504765303045427  |
| 124 |                  | Control Who Can Find You                                                | 1718866941707011 |
| 125 | 592679377575472  | Безпека                                                                 |                  |
| 126 |                  | Джерела щодо боротьби з жорстоким поводженням                           | 726709730764837  |
| 127 |                  | Ресурси з допомоги для протидії самогубству та самоушкодженню           | 1553737468262661 |
| 128 |                  | Crisis Response                                                         | 141874516227713  |
| 129 |                  | Ресурси з правил безпеки для допомоги батькам                           | 1079477105456277 |
| 130 |                  | Інформація для правоохоронних органів                                   | 764592980307837  |
| 131 | 235353253505947  | Захист облікового запису                                                |                  |
| 132 |                  | Функції безпеки та поради з її забезпечення                             | 285695718429403  |
| 133 |                  | Сповіщення про вхід і двоетапна перевірка                               | 909243165853369  |
| 134 |                  | Уникайте спаму та шахрайства                                            | 1584206335211143 |
| 135 | 236079651241697  | Безпека під час здійснення покупок                                      |                  |
| 136 |                  | Розпізнавання шахрайства                                                | 1086141928978559 |
| 137 |                  | Уникнення шахрайства                                                    | 2374002556073992 |
| 138 |                  | Купівля на Marketplace                                                  | 721562085854101  |
| 139 |                  | Поради щодо безпечної купівлі                                           | 123884166448529  |
| 140 |                  | Купуйте впевнено                                                        | 1599248863596914 |
| 141 |                  | Політики та скарги                                                      |                  |
| 142 | 1753719584844061 | Скарга на порушення                                                     |                  |
| 143 |                  | Як поскаржитися на щось?                                                | 1380418588640631 |
| 144 |                  | Don't Have an Account?                                                  | 1723400564614772 |
| 145 | 1126628984024935 | Як повідомити про проблему у Facebook                                   |                  |
| 146 | 186614050293763  | Being Your Authentic Self on Facebook                                   |                  |
| 147 | 1561472897490627 | Повідомлення про порушення конфіденційності                             |                  |
| 148 | 1216349518398524 | Зламані та фальшиві облікові записи                                     |                  |
| 149 | 275013292838654  | Керування обліковим записом померлої людини                             |                  |
| 150 |                  | About Memorialized Accounts                                             | 1017717331640041 |
| 151 |                  | Request to Memorialize or Remove an Account                             | 1111566045566400 |
| 152 | 399224883474207  | Інтелектуальна власність                                                |                  |
| 153 |                  | Авторське право                                                         | 1020633957973118 |
| 154 |                  | Торговельна марка                                                       | 507663689427413  |
| 155 | 1735443093393986 | Про наші політики                                                       |                  |

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[hanan](https://stackoverflow.com/users/11885361)** (2022-12-30): Can you summarize this in one code pls.
- **me** (2022-12-30): @hanan the only corrections you MUST try to make the code work at all are to get fix the syntax error in `requests.get` and to get rid of the `"html5lib"` part, but this is the full code I ran to get the table: https://pastebin.com/Q4hrMHK6
- **[hanan](https://stackoverflow.com/users/11885361)** (2022-12-30): thanks for the replies but `slimit` is causing me issues,  import slimit   `File "C:\Python310\lib\site-packages\slimit\__init__.py", line 27, in <module>     from minifier import minify` `ModuleNotFoundError: No module named 'minifier'` tried`pip install minifier` but  it seems no version is found.
- **[hanan](https://stackoverflow.com/users/11885361)** (2022-12-30): forget about it. resolved this error.
- **[hanan](https://stackoverflow.com/users/11885361)** (2022-12-30): in the dataFrame `cmsID` if I wanted to print the number of data contained, I'm getting some error. help me with this
- **me** (2022-12-31): @hanan what error are you getting? please include the line (or preferably a screenshot)
- **[hanan](https://stackoverflow.com/users/11885361)** (2023-01-10): I was trying to save it in a `csv` file, this is the error `AttributeError: 'str' object has no attribute 'to_csv'`. how can I save this into `csv` file?
- **me** (2023-01-10): you're getting the error on the line with *`pandas.DataFrame(cmsList).to_csv('CmsIDs_GetIDs.csv', index=False)`*? may I see a screenshot?
- **[hanan](https://stackoverflow.com/users/11885361)** (2023-01-10): That is correct. I was using wrongly that what caused to the error. thanks for correction though. and if I wanted to update the `CmsIDs_GetIDs.csv` with no duplicate values only added new values what can I do? Thanks
- **me** (2023-01-10): @hanan you can call `.to_csv` in append mode by passing **`mode='a'`** to not over-write previous file data (but keep in mind that if you don't set `header=False`, the header row will be repeated before the new rows), but if you want to avoid duplicates, you'll probably have to load the previous data to check against - if you need more details it'd be better to post another q. I can't fit more into comments, but maybe look into [`.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)&[`.update`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.update.html)
- **[hanan](https://stackoverflow.com/users/11885361)** (2023-01-12): tried to different approaches, still no luck. for example: `old_data = pandas.read_csv("./CmsIDs_GetIDs.csv")` `n= pandas.DataFrame(cmsList).to_csv('data.csv', index=False) new_data = pandas.read_csv("./data.csv")` and then tried to compare each as: `old_data.compare(new_data)` but unfortunately I am getting an error : `ValueError: Can only compare identically-labeled DataFrame objects` what can I do this to solve  this?
- **me** (2023-01-12): @hanan you can't `.compare` with a DataFrame that has a different length - they have to have the same shape, index and header. The error is likely due to `new_data` having more or less rows than `old_data`...you can try `old_data.merge(new_data, how='outer')`
- **[hanan](https://stackoverflow.com/users/11885361)** (2023-01-13): but I also wanted to print the new row on the console.
- **me** (2023-01-13): you could add empty rows to the whichever is shorter before comparing the old and merged
- **[hanan](https://stackoverflow.com/users/11885361)** (2023-01-13): well, they update their web but how can I know how much empty rows would I need in this case.
- **me** (2023-01-13): @hanan just check their [length](https://stackoverflow.com/q/15943769/6146136) and get the difference. whichever is shorter add that many empty rows to it
- **[hanan](https://stackoverflow.com/users/11885361)** (2023-01-13): I tried this : [shared On pastebin](https://pastebin.com/DwUuVNay)  but I still get same error `ValueError: Can only compare identically-labeled DataFrame objects` please help with this.
- **[hanan](https://stackoverflow.com/users/11885361)** (2023-01-13): Let us [continue this discussion in chat](https://chat.stackoverflow.com/rooms/251114/discussion-between-hanan-and-driftr95).
- **me** (2023-01-13): @hanan can you post a new question?
- **[hanan](https://stackoverflow.com/users/11885361)** (2023-01-16): currently I am thinking about how can I structure the question.
- **[hanan](https://stackoverflow.com/users/11885361)** (2023-01-16): and I feel it is hard though
