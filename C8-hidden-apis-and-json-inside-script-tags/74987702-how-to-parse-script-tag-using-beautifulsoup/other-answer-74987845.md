---
title: "How to parse <script> tag using beautifulsoup"
site: stackoverflow
question_id: 74987702
answer_id: 74987845
url: https://stackoverflow.com/a/74987845
author: "Youssef al-Tai"
author_url: https://stackoverflow.com/users/14174934
posted: 2023-01-02T23:21:26Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 040459f1f310cbcdbcf882cb3969307f85572deae9f16572ee2b9f8d139466f5
role: another answer on the same question, kept as context; not my work
---

# Answer by [Youssef al-Tai](https://stackoverflow.com/users/14174934) — 2023-01-02

Posted on Stack Overflow, <https://stackoverflow.com/a/74987845>, 2023-01-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Well, `json.loads()` should take a string that contains a JSON document. However, the value of `text` is not a valid JSON because of the `window.appCache=` at the beginning.

And it's not just that, I tried slicing `text` to exclude the `window.appCache=` part:

```
text = text[len("window.appCache="):]
```

and it gave me this error:

```
raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 68113 (char 68112)
```

so I checked the value of `text[68110:]` and it turns out that it was complaining because indeed `text` is not a valid JSON document:

```
undefined,"useErrorPages":true},"parsedRequest":{"urlData":{"url":"\u002FReviews\u002FAlteryx-Reviews-E351220.htm","params":{"employerId":351220,"page":null},"pagePrefix":"P","origin":"http:\u002F\u002Fwww.glassdoor.com"}},"seoConfig":{"appName":"reviews","staticPaths":[],"seoABTest":{},"pageType":"EMPLOYER_INFO","pageContentType":"REVIEWS","urlRegexMatchers":[function genericEiReviewsUrlMatcher(originalUrl) {
  var url = decodeURIComponent(originalUrl);
  var result = {
    params: {},
    helpers: {
      dos2ExperimentHelpers: _dos2ExperimentHelpers["default"]
    }
  };

  var getHumanReadableText = function getHumanReadableText(data) {
    return data.replace(/[+-]/g, ' ');
  };
```

This is the result of `text[68110:]`, it is a JavaScript object, but not a valid JSON object.

JSON values cannot be one of the following data types:
 - a function
 - a date
 - undefined

As you can see, `text` has `undefined` and a function as values for some fields.

If you want the value of a specific field ("reviews" as you mentioned for example), I recommend parsing the string manually using maybe regular expressions or something like that.
