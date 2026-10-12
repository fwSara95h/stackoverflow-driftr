# Code from my Stack Overflow answer https://stackoverflow.com/a/75645726 (posted 2023-03-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> in _all_strings
>     (types is not None and type(descendant) not in types)):
> TypeError: argument of type 'object' is not iterable
>

# --- block 2 ---
class MyBeautifulSoup(BeautifulSoup):
    def _all_strings(self, strip=False, types=(NavigableString, CData)):
        # verify types [ADDED]
        if hasattr(types,'__iter__'):
            types = tuple([t for t in types if isinstance(t,type)])
        if types is None: types = NavigableString
        if not types or not isinstance(types, (type, tuple)):
            types = (NavigableString, CData)

        for descendant in self.descendants:
            # return "a" string representation if we encounter it

            if isinstance(descendant, Tag) and descendant.name == 'a':
                yield str('<{}> '.format(descendant.get('href', '')))

            # skip an inner text node inside "a"
            if isinstance(descendant,NavigableString) and descendant.parent.name == 'a':
                continue

            if not isinstance(descendant, types): continue # default behavior [EDITED]

            if strip:
                descendant = descendant.strip()
                if len(descendant) == 0:
                    continue
            yield descendant

# --- block 3 ---
# from urllib.parse import urljoin

class MyBeautifulSoup(BeautifulSoup):
    def _all_strings_plus(  self, strip=True, types=NavigableString, 
                            aRef={'a': lambda a: f"<{a.get('href', '')}>"}, 
                            skipTags=['script', 'style']    ):
        # verify types
        if hasattr(types,'__iter__') and not isinstance(types,type):
            types = tuple([t for t in types if isinstance(t, type)])
        if not (types and isinstance(types,(type,tuple))): types = NavigableString

        # skip text in tags included in aRef
        # skipTags += list(aRef.keys())

        for descendant in self.descendants:
            # yield extra strings according to aRef
            if isinstance(descendant, Tag) and descendant.name in aRef:
                extraStr = aRef[descendant.name](descendant)
                if isinstance(extraStr, str): yield extraStr

            # skip text nodes DIRECTLY inside a Tag in aRef
            # if descendant.parent.name in aRef: continue

            # skip ALL text nodes inside skipTags 
            if skipTags and descendant.find_parent(skipTags): continue

            # default behavior
            if not isinstance(descendant, types): continue

            if strip:
                descendant = descendant.strip()
                if len(descendant) == 0: continue
            yield descendant

    def get_text_plus(self, separator=" ", srcUrl=None, **aspArgs):
        if srcUrl and isinstance(srcUrl, str):
            def hrefStr(aTag):
                href = aTag.get('href')
                if not (href is None or href.startswith('javascript:')):
                    return f"<{urljoin(srcUrl, href)}>"
            aspArgs.setdefault('aRef', {})
            aspArgs['aRef']['a'] = hrefStr

        return separator.join(self._all_strings_plus(**aspArgs))
