---
title: "Python HTML parsing getting only first element without childs"
site: stackoverflow
question_id: 74108012
url: https://stackoverflow.com/q/74108012
asked: 2022-10-18T08:35:14Z
asked_by: "NukeSkull"
asked_by_url: https://stackoverflow.com/users/16664550
last_edited: never
tags: [python, html, beautifulsoup, python-requests]
score: 0
views_at_snapshot: 212
answer_count: 1
accepted_answer_id: 74119968
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5034238c8fd13488de95be96d036b758eca3d1c3acadc27666ec1eb73407fcae
---

# Python HTML parsing getting only first element without childs

Asked by [NukeSkull](https://stackoverflow.com/users/16664550) on Stack Overflow, <https://stackoverflow.com/q/74108012>, 2022-10-18. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So basically I'm trying to parse a website and the result is not the whole html, just some elements. The webpage I'm trying to parse to practice is https://dre.pt/dre/detalhe/anuncio-concurso-urgente/491-2022-201313437 (inspect webpage to check html).

At first, tried parsing with BeatifulSoup4, but since I was not getting all the html I tried doing it with the requests package. This is the code I used:

```python
import requests

page = requests.get(https://dre.pt/dre/detalhe/anuncio-concurso-urgente/491-2022-201313437)
print(page.text)
```

And this is the result of the print:

```
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="format-detection" content="telephone=no" />
        <script type='text/javascript'>window.OutSystemsApp = { basePath: '/dre/' };</script>
        <meta http-equiv="Content-Security-Policy" content="base-uri 'self'; child-src * gap:; frame-src * gap:; connect-src *; default-src 'self' 'unsafe-inline' *.google-analytics.com *.hotjar.com *.googletagmanager.com *.dre.pt *.hotjar.io *.doubleclick.net *.knightlab.com *.google.com *.google.pt gap: 'unsafe-inline' 'unsafe-eval'; font-src 'self' data:; img-src * blob:; script-src 'unsafe-inline' * 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; frame-ancestors *.incm.pt *.dre.pt 'self' gap:; report-uri /SecurityUtils/rest/Report/ReportViolations?Params=6ynyp6xeJpZnfxI6yAFDPT6aME%2BSwVNSjUa7DbEWDtGj%2BeYOS2vlfnuZj5cBszGf0z2tYxgp5XrpqwJyMUUnTw%3D%3D; " />
<meta http-equiv="X-Content-Security-Policy" content="base-uri 'self'; child-src * gap:; frame-src * gap:; connect-src *; default-src 'self' 'unsafe-inline' *.google-analytics.com *.hotjar.com *.googletagmanager.com *.dre.pt *.hotjar.io *.doubleclick.net *.knightlab.com *.google.com *.google.pt gap: 'unsafe-inline' 'unsafe-eval'; font-src 'self' data:; img-src * blob:; script-src 'unsafe-inline' * 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; frame-ancestors *.incm.pt *.dre.pt 'self' gap:; report-uri /SecurityUtils/rest/Report/ReportViolations?Params=6ynyp6xeJpZnfxI6yAFDPT6aME%2BSwVNSjUa7DbEWDtGj%2BeYOS2vlfnuZj5cBszGf0z2tYxgp5XrpqwJyMUUnTw%3D%3D; " />
<meta http-equiv="X-WebKit-CSP" content="base-uri 'self'; child-src * gap:; frame-src * gap:; connect-src *; default-src 'self' 'unsafe-inline' *.google-analytics.com *.hotjar.com *.googletagmanager.com *.dre.pt *.hotjar.io *.doubleclick.net *.knightlab.com *.google.com *.google.pt gap: 'unsafe-inline' 'unsafe-eval'; font-src 'self' data:; img-src * blob:; script-src 'unsafe-inline' * 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; frame-ancestors *.incm.pt *.dre.pt 'self' gap:; report-uri /SecurityUtils/rest/Report/ReportViolations?Params=6ynyp6xeJpZnfxI6yAFDPT6aME%2BSwVNSjUa7DbEWDtGj%2BeYOS2vlfnuZj5cBszGf0z2tYxgp5XrpqwJyMUUnTw%3D%3D; " />

        
        <meta name="viewport" content="viewport-fit=cover, width=device-width, initial-scale=1" />
<script type="text/javascript">
(function () {
    function appendMetaTagAttributes(metaTag, attribute, values) {
        var elem = document.querySelector("meta[name=" + metaTag + "]");

        if (elem) {
            var attrContent = elem.getAttribute(attribute);
            elem.setAttribute(attribute, (attrContent ? attrContent + "," : "") + values.join(","));
        }
    }

    if (navigator && /OutSystemsApp/i.test(navigator.userAgent)) {
        // If this app is running on the native shell, we want to disable the zoom
        appendMetaTagAttributes("viewport", "content", ["user-scalable=no", "minimum-scale=1.0"]);
    }
})();</script>

        <script type="text/javascript" src="/dre/scripts/OutSystemsManifestLoader.js?Uno7DkMuu4+3RKfSExTIUg"></script>
<script type="text/javascript" src="/dre/scripts/OutSystems.js?eq9LGmzdgJbMq6dbNoVMvQ"></script>
<script type="text/javascript" src="/dre/scripts/OutSystemsReactView.js?DtzHEvOePADFJAVO+XYgVg"></script>
<script type="text/javascript" src="/dre/scripts/cordova.js?7KqI9_oL9hClomz1RdzTqg"></script>
<script type="text/javascript" src="/dre/scripts/NullDebugger.js?ivgNSF0_ZARULD3LtoI2HA"></script>
<script type="text/javascript" src="/dre/scripts/DRE.appDefinition.js?otw_Nv9Nr+Q7EbWK92qVcw"></script>
<script type="text/javascript" src="/dre/scripts/OutSystemsReactWidgets.js?E4SSw3FwbHWsyMMUPr64mg"></script>
<link type="text/css" rel="stylesheet" href="/dre/css/_Basic.css?EqGzAe81QbZLXJyfY3oLwA"></link>

        <script type="text/javascript">OSManifestLoader.indexVersionToken = "o1jW2zcC1fbJz1ZC8XfM8g";
</script>
    </head>
    <body>
        <div id="reactContainer"></div>
        <noscript><span>JavaScript is required</span></noscript>

        <script type="text/javascript" src="/dre/scripts/DRE.index.js?lmc__VYpxdf3u6qXtN7E9w"></script>

    </body>
</html>
```

As you can see I'm getting all the head from the html, but in the body section I only recieve the reactContainer div but none of it's childs, where the information is, how should I get the html to get the childs too?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[chitown88](https://stackoverflow.com/users/7752296)** (2022-10-18): The page is dynamic/rendered through js. Doing a simple request will only return the static, non-rendered html. If you want the rendered data, you need to see a) if it comes directly from the api, which if it does, request that endpoint, b) it may be in json format in the html `<script>` tag, or c) use slenium to allow the page to render, then parse it
- **[NukeSkull](https://stackoverflow.com/users/16664550)** (2022-10-18): Thanks! I managed to get the info using ScrapingAnt, tried with Selenium but didn't figure out how.
- **[Andriy Stolyar](https://stackoverflow.com/users/5952509)** (2022-10-18): You can either replicate all of the api requests or use browser automation. Try Playwright, go to the url, wait till page loads and then just get the full page source with ```page.content()```
