# Code from my Stack Overflow answer https://stackoverflow.com/a/74655334 (posted 2022-12-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
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

# --- block 3 ---
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
>

# --- block 4 ---
print(pandas.DataFrame(
    [tuple(a) for a in allData], columns=colHeaders
) .set_index('listingId').to_markdown(index=False))
# remove index=False to include listingId
