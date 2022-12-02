---
title: "nested loop returns the same results for multiple rows while webscraping - beautiful soup"
site: stackoverflow
question_id: 74647356
answer_id: 74655334
url: https://stackoverflow.com/a/74655334
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-02T11:49:05Z
last_edited: 2022-12-02T18:23:49Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74655334/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: [selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 41368684bc94a1f28af4dcd4498ef0d2b90a28c0dcc21d72eedef75a5c319da2
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74655334>, 2022-12-02, last edited 2022-12-02; score 0. Text as retrieved 2026-10-12.

You should not be nesting like that. You only want one `info` list for each item in `lists`, so you should not be forming `info` inside any nested for-loops. You *could* use [`zip`](https://www.w3schools.com/python/ref_func_zip.asp) instead:

<sub>**NOTE:** It's not a good idea to use variable names like `list` and `property` since they already mean something in python...</sub>
```python
lists = soup.find_all('section', class_="placard-content")
properties = soup.find_all('li', class_="mortar-wrapper")
addresses = soup.find_all('div', class_="property-information") ## more specific

for l, prop, address in zip(lists, properties, addresses):
    price = l.find('p', class_="property-pricing").text
    beds = l.find('p', class_="property-beds").text
    location = address.find('div', class_="property-address js-url").text
    name = prop.find('span', class_="js-placardTitle title").text
    info = [name,location,beds,price]
    print(info) 
```

---

**However,** it's rather risky to use `find`+`.text` without checking if `find` returned something [to avoid raising errors when it tries to get `.text` from `None`]; also, for finding multiple details from bs4, I prefer to use [`select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS Selectors](https://facelessuser.github.io/soupsieve/selectors/basic/#universal-selectors) since it allows me to use functions [like this](https://pastebin.com/ZnZ7xM6u) with [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) like
```python 
# page = requests.get(url, headers=header)
# soup = BeautifulSoup(page.content, 'html.parser')

### FIRST PASTE FUNCTION DEFINITION ( from https://pastebin.com/ZnZ7xM6u ) ###

colHeaders = ['listingId', 'Name', 'Location', 'Beds', 'Price', 'Link']
allData = []
for ap in soup.select('li > article.placard[data-listingid]'):
    allData.append(selectForList(ap, selectors=[
        ('', 'data-listingid'), 'span.title', 'div.property-address',
        'p.property-beds', 'p.property-pricing', 
        ('a.property-link[href]', 'href')
    ], printList=True)) ## set printList=False to not print ##
```
will print
> ```python
> ['vy0ysgf', '99 West Paces Ferry', '99 W Paces Ferry Rd, Atlanta, GA 30305', '1-3 Beds', '$3,043 - 16,201', 'https://www.apartments.com/99-west-paces-ferry-atlanta-ga/vy0ysgf/']
> ['88l36f2', 'Broadstone Pullman', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825', 'https://www.apartments.com/broadstone-pullman-atlanta-ga/88l36f2/']
> ['0g6gh01', '1824 Defoor', '1824 Defoor Ave NW, Atlanta, GA 30318', 'Studio - 3 Beds', '$1,676 - 3,194', 'https://www.apartments.com/1824-defoor-atlanta-ga/0g6gh01/']
> ['4mpewpl', 'Mira at Midtown Union', '1301 Spring St NW, Atlanta, GA 30309', 'Studio - 3 Beds', '$1,705 - 6,025', 'https://www.apartments.com/mira-at-midtown-union-atlanta-ga/4mpewpl/']
> ['ldcnyed', 'Alexan Summerhill', '720 Hank Aaron Dr SE, Atlanta, GA 30315', 'Studio - 2 Beds', '$1,530 - 3,128', 'https://www.apartments.com/alexan-summerhill-atlanta-ga/ldcnyed/']
> ['n63p95m', '1660 Peachtree Midtown', '1660 Peachtree St NW, Atlanta, GA 30309', '1-2 Beds', '$1,699 - 2,499', 'https://www.apartments.com/1660-peachtree-midtown-atlanta-ga/n63p95m/']
> ['tzqfblc', '3005 Buckhead', '3005 Peachtree Rd NE, Atlanta, GA 30305', 'Studio - 3 Beds', '$1,556 - 4,246', 'https://www.apartments.com/3005-buckhead-atlanta-ga/tzqfblc/']
> ['09tx720', 'Novel O4W', '525 NE North Ave, Atlanta, GA 30308', 'Studio - 2 Beds', '$1,776 - 3,605', 'https://www.apartments.com/novel-o4w-atlanta-ga/09tx720/']
> ['bp1p51b', 'AMLI Westside', '1084 Howell Mill Rd NW, Atlanta, GA 30318', 'Studio - 2 Beds', '$1,475 - 3,344', 'https://www.apartments.com/amli-westside-atlanta-ga/bp1p51b/']
> ['thm5n1c', 'The Cliftwood', '185 Cliftwood Dr NE, Atlanta, GA 30328', 'Studio - 3 Beds', '$1,730 - 2,991', 'https://www.apartments.com/the-cliftwood-atlanta-ga/thm5n1c/']
> ['07g5143', 'Ellington Midtown', '391 17th St NW, Atlanta, GA 30363', '1-2 Beds', '$1,528 - 2,741', 'https://www.apartments.com/ellington-midtown-atlanta-ga/07g5143/']
> ['zwcyjly', 'Glenn Perimeter', '5755 Glenridge Dr, Atlanta, GA 30328', '1-3 Beds', '$1,674 - 5,115', 'https://www.apartments.com/glenn-perimeter-atlanta-ga/zwcyjly/']
> ['pfsrw7t', 'The Dagny Midtown Apartments', '888 Juniper St NE, Atlanta, GA 30309', '1-3 Beds', '$1,863 - 6,758', 'https://www.apartments.com/the-dagny-midtown-apartments-atlanta-ga/pfsrw7t/']
> ['beqvl9b', 'Pencil Factory Flats', '349 Decatur St SE, Atlanta, GA 30312', 'Studio - 3 Beds', '$1,555 - 5,636', 'https://www.apartments.com/pencil-factory-flats-atlanta-ga/beqvl9b/']
> ['betv189', 'The Boulevard at Grant Park', '1015 Boulevard SE, Atlanta, GA 30312', 'Studio - 2 Beds', 'Call for Rent', 'https://www.apartments.com/the-boulevard-at-grant-park-atlanta-ga/betv189/']
> ['nhmd47n', 'Rio At Lenox', '2716 Buford Hwy, Atlanta, GA 30324', 'Studio - 2 Beds', '$1,350 - 2,025', 'https://www.apartments.com/rio-at-lenox-atlanta-ga/nhmd47n/']
> ['t6fxcr9', 'Vue at the Quarter', '2048 Bolton Dr, Atlanta, GA 30318', '1-3 Beds', '$1,454 - 7,445', 'https://www.apartments.com/vue-at-the-quarter-atlanta-ga/t6fxcr9/']
> ['nt1x8zq', 'Lofts at Centennial Yards South', '125 Ted Turner Dr SW, Atlanta, GA 30303', 'Studio - 2 Beds', '$1,361 - 2,540', 'https://www.apartments.com/lofts-at-centennial-yards-south-atlanta-ga/nt1x8zq/']
> ['kpsw7tc', 'The Maverick Flats', '72 Milton Ave, Atlanta, GA 30315', 'Studio - 2 Beds', '$1,311 - 2,616', 'https://www.apartments.com/the-maverick-flats-atlanta-ga/kpsw7tc/']
> ['h1987t1', 'Broadstone Upper Westside', '2167 Bolton Dr NW, Atlanta, GA 30318', 'Studio - 2 Beds', '$1,279 - 3,679', 'https://www.apartments.com/broadstone-upper-westside-atlanta-ga/h1987t1/']
> ['vntq44f', 'Ella', '2201 Glenwood Ave SE, Atlanta, GA 30316', 'Studio - 3 Beds', '$1,325 - 3,055', 'https://www.apartments.com/ella-atlanta-ga/vntq44f/']
> ['9yyrgl4', 'MAA Briarcliff', '500 Briarvista Way, Atlanta, GA 30329', '1-3 Beds', '$1,365 - 5,235', 'https://www.apartments.com/maa-briarcliff-atlanta-ga/9yyrgl4/']
> ['94xq484', 'AMLI Lenox', '3478 Lakeside Dr NE, Atlanta, GA 30326', '1-3 Beds', '$1,649 - 9,095', 'https://www.apartments.com/amli-lenox-atlanta-ga/94xq484/']
> ['q9jhgvy', 'Platform at Grant Park', '290 Martin Luther King Jr Dr SE, Atlanta, GA 30312', 'Studio - 2 Beds', '$1,454 - 1,954', 'https://www.apartments.com/platform-at-grant-park-atlanta-ga/q9jhgvy/']
> ['y22d57t', 'Generation Atlanta', '369 Centennial Olympic Park Dr NW, Atlanta, GA 30313', 'Studio - 2 Beds', '$1,374 - 3,482', 'https://www.apartments.com/generation-atlanta-atlanta-ga/y22d57t/']
> ```

---

or, you could use pandas to print as table:
```python
print(pandas.DataFrame(
    [tuple(a) for a in allData], columns=colHeaders
) .set_index('listingId').to_markdown(index=False))
# remove index=False to include listingId
```
prints
> ```lang-none
> | Name                            | Location                                             | Beds            | Price           | Link                                                                           |
> |:--------------------------------|:-----------------------------------------------------|:----------------|:----------------|:-------------------------------------------------------------------------------|
> | 99 West Paces Ferry             | 99 W Paces Ferry Rd, Atlanta, GA 30305               | 1-3 Beds        | $3,043 - 16,201 | https://www.apartments.com/99-west-paces-ferry-atlanta-ga/vy0ysgf/             |
> | Broadstone Pullman              | 105 Rogers St NE, Atlanta, GA 30317                  | Studio - 2 Beds | $1,630 - 2,825  | https://www.apartments.com/broadstone-pullman-atlanta-ga/88l36f2/              |
> | 1824 Defoor                     | 1824 Defoor Ave NW, Atlanta, GA 30318                | Studio - 3 Beds | $1,676 - 3,194  | https://www.apartments.com/1824-defoor-atlanta-ga/0g6gh01/                     |
> | Mira at Midtown Union           | 1301 Spring St NW, Atlanta, GA 30309                 | Studio - 3 Beds | $1,705 - 6,025  | https://www.apartments.com/mira-at-midtown-union-atlanta-ga/4mpewpl/           |
> | Alexan Summerhill               | 720 Hank Aaron Dr SE, Atlanta, GA 30315              | Studio - 2 Beds | $1,530 - 3,128  | https://www.apartments.com/alexan-summerhill-atlanta-ga/ldcnyed/               |
> | 1660 Peachtree Midtown          | 1660 Peachtree St NW, Atlanta, GA 30309              | 1-2 Beds        | $1,699 - 2,499  | https://www.apartments.com/1660-peachtree-midtown-atlanta-ga/n63p95m/          |
> | 3005 Buckhead                   | 3005 Peachtree Rd NE, Atlanta, GA 30305              | Studio - 3 Beds | $1,556 - 4,246  | https://www.apartments.com/3005-buckhead-atlanta-ga/tzqfblc/                   |
> | Novel O4W                       | 525 NE North Ave, Atlanta, GA 30308                  | Studio - 2 Beds | $1,776 - 3,605  | https://www.apartments.com/novel-o4w-atlanta-ga/09tx720/                       |
> | AMLI Westside                   | 1084 Howell Mill Rd NW, Atlanta, GA 30318            | Studio - 2 Beds | $1,475 - 3,344  | https://www.apartments.com/amli-westside-atlanta-ga/bp1p51b/                   |
> | The Cliftwood                   | 185 Cliftwood Dr NE, Atlanta, GA 30328               | Studio - 3 Beds | $1,730 - 2,991  | https://www.apartments.com/the-cliftwood-atlanta-ga/thm5n1c/                   |
> | Ellington Midtown               | 391 17th St NW, Atlanta, GA 30363                    | 1-2 Beds        | $1,528 - 2,741  | https://www.apartments.com/ellington-midtown-atlanta-ga/07g5143/               |
> | Glenn Perimeter                 | 5755 Glenridge Dr, Atlanta, GA 30328                 | 1-3 Beds        | $1,674 - 5,115  | https://www.apartments.com/glenn-perimeter-atlanta-ga/zwcyjly/                 |
> | The Dagny Midtown Apartments    | 888 Juniper St NE, Atlanta, GA 30309                 | 1-3 Beds        | $1,863 - 6,758  | https://www.apartments.com/the-dagny-midtown-apartments-atlanta-ga/pfsrw7t/    |
> | Pencil Factory Flats            | 349 Decatur St SE, Atlanta, GA 30312                 | Studio - 3 Beds | $1,555 - 5,636  | https://www.apartments.com/pencil-factory-flats-atlanta-ga/beqvl9b/            |
> | The Boulevard at Grant Park     | 1015 Boulevard SE, Atlanta, GA 30312                 | Studio - 2 Beds | Call for Rent   | https://www.apartments.com/the-boulevard-at-grant-park-atlanta-ga/betv189/     |
> | Rio At Lenox                    | 2716 Buford Hwy, Atlanta, GA 30324                   | Studio - 2 Beds | $1,350 - 2,025  | https://www.apartments.com/rio-at-lenox-atlanta-ga/nhmd47n/                    |
> | Vue at the Quarter              | 2048 Bolton Dr, Atlanta, GA 30318                    | 1-3 Beds        | $1,454 - 7,445  | https://www.apartments.com/vue-at-the-quarter-atlanta-ga/t6fxcr9/              |
> | Lofts at Centennial Yards South | 125 Ted Turner Dr SW, Atlanta, GA 30303              | Studio - 2 Beds | $1,361 - 2,540  | https://www.apartments.com/lofts-at-centennial-yards-south-atlanta-ga/nt1x8zq/ |
> | The Maverick Flats              | 72 Milton Ave, Atlanta, GA 30315                     | Studio - 2 Beds | $1,311 - 2,616  | https://www.apartments.com/the-maverick-flats-atlanta-ga/kpsw7tc/              |
> | Broadstone Upper Westside       | 2167 Bolton Dr NW, Atlanta, GA 30318                 | Studio - 2 Beds | $1,279 - 3,679  | https://www.apartments.com/broadstone-upper-westside-atlanta-ga/h1987t1/       |
> | Ella                            | 2201 Glenwood Ave SE, Atlanta, GA 30316              | Studio - 3 Beds | $1,325 - 3,055  | https://www.apartments.com/ella-atlanta-ga/vntq44f/                            |
> | MAA Briarcliff                  | 500 Briarvista Way, Atlanta, GA 30329                | 1-3 Beds        | $1,365 - 5,235  | https://www.apartments.com/maa-briarcliff-atlanta-ga/9yyrgl4/                  |
> | AMLI Lenox                      | 3478 Lakeside Dr NE, Atlanta, GA 30326               | 1-3 Beds        | $1,649 - 9,095  | https://www.apartments.com/amli-lenox-atlanta-ga/94xq484/                      |
> | Platform at Grant Park          | 290 Martin Luther King Jr Dr SE, Atlanta, GA 30312   | Studio - 2 Beds | $1,454 - 1,954  | https://www.apartments.com/platform-at-grant-park-atlanta-ga/q9jhgvy/          |
> | Generation Atlanta              | 369 Centennial Olympic Park Dr NW, Atlanta, GA 30313 | Studio - 2 Beds | $1,374 - 3,482  | https://www.apartments.com/generation-atlanta-atlanta-ga/y22d57t/              |
> ```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **user15564501 (account no longer exists)** (2022-12-02): This is what I need.  I'm still getting an error.                                    location = address.find('div', class_="property-address js-url").text AttributeError: 'NoneType' object has no attribute 'text'
- **me** (2022-12-02): @BackToI.T. yeah that's what I was warning about when I said *"...it's rather risky to use `find`+`.text` without checking if `find` returned something..."*, the `for ap in soup.select....` version of the solution should resolve that type of issues
