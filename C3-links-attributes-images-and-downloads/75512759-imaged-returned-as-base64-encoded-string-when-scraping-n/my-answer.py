# Code from my Stack Overflow answer https://stackoverflow.com/a/75515179 (posted 2023-02-20), extracted verbatim; may need the question's context to run.

# --- block 1 ---
import requests, json
from bs4 import BeautifulSoup

#################################################
# for printing and returning in one statement ###
def vRet(toPrint, toRet=[]):                   ##
    print(toPrint)                             ##
    return toRet                               ##
                                               ##
## extract a nested value with a list of keys ###
def valgetter(obj, *keys, defaultVal=None):    ##
    try:                                       ##
        for k in keys: obj = obj[k]            ##
    except: return defaultVal                  ##
    return obj                                ###
#################################################


def get_team_stories(team_endpt):
    teamUrl = f'https://www.espn.com/nba/team/_/name/{team_endpt}'
    resp = requests.get(teamUrl)
    rMsg = f'[Received <{resp.status_code} {resp.reason}> from {resp.url}]\n'
    if not resp.ok: return vRet(f'{rMsg}! Failed to scrape {teamUrl}')

    soup = BeautifulSoup(resp.content, 'html.parser')
    try:
        pgData = json.loads(soup.find(
            'script', string=lambda s: s and ''.join(
                s.split()).startswith("window['__espnfitt__']=")
        ).text.split('=', 1)[-1].strip().strip(';'))['page']

        team_heading = pgData['meta']['title'].split('-')[0].strip()
        clubhouseCols = pgData['content']['clubhouse']['columns']
        articles = clubhouseCols['middleColumn']['clubhouse']['feed']
    except Exception as e: return vRet(repr(e))

    if not isinstance(articles, list): 
        return vRet(f'{rMsg}Expected list of articles, not {type(articles)}')
    if not articles: return vRet(f'{rMsg}No articles for {team_endpt}')

    def formLink(l):
        if not isinstance(l, str): return l 
        if l.startswith('/espn/'): 
            return l.replace('/espn/', 'https://www.espn.com/', 1)
        if l.startswith('/'): return f'https://www.espn.com{l}'
        return l

    rData = [{
        'team_heading': team_heading, 'headline': a['headline'], 
        'link': formLink(a['link']), 'img_url': valgetter(a,'image','url')
    } for a in articles if isinstance(a, dict) and 'headline' in a]
    if len(rData) != len(articles): 
        print(f'! Could only extract {len(rData)} of {len(articles)} articles')
    return rData

# --- block 2 ---
team_endpoints = ['bos/boston-celtics', 'phi/philadelphia-76ers', 
                  'bkn/brooklyn-nets', 'ny/new-york-knicks']
team_stories = []
for te in team_endpoints: team_stories += get_team_stories(te)

print(len(team_stories), 'articles collected\n')
