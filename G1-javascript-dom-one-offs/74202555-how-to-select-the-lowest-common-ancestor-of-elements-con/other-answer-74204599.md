---
title: "How to select the lowest common ancestor of elements containing specific text?"
site: stackoverflow
question_id: 74202555
answer_id: 74204599
url: https://stackoverflow.com/a/74204599
author: "Martin Honnen"
author_url: https://stackoverflow.com/users/252228
posted: 2022-10-26T08:15:05Z
last_edited: never
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 337955743220da9c662b03d9e2d56f26349a007f0bfdeaa328557df66ea5ec82
role: another answer on the same question, kept as context; not my work
---

# Answer by [Martin Honnen](https://stackoverflow.com/users/252228) — 2022-10-26

Posted on Stack Overflow, <https://stackoverflow.com/a/74204599>, 2022-10-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

XPath 3.1 can express it declaratively:

    let $text-nodes := //text()[contains(., 'SOMETHING')]
    return innermost(//*[every $text in $text-nodes satisfies descendant::text() intersect $text])

XPath 3.1 is supported in the browser through the [SaxonJS library][1] from Saxonica, documented at https://www.saxonica.com/saxon-js/documentation2/index.html.

Example use


<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    const htmlSnippet = `<div> <!-- A -->
      <div> <!-- B -->
        <div> <!-- C: I need to select this element -->
          <div>
            <div>
              <div>
                random string
                <div>
                  <div>
                    SOMETHING
                  </div>
                  <div>
                    SOMETHING
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div>
            <div>
              <div>
                SOMETHING
              </div>
            </div>
          </div>
          <div>
            <div>
              <div>
                SOMETHING
              </div>
            </div>
          </div>
          <div>
            <div>
              <div>
                SOMETHING
              </div>
            </div>
          </div>
          <div>
            <div>
              <div>
                SOMETHING
              </div>
            </div>
          </div>
        </div>
        <div>
          random string
        </div>
      </div>
      <div>
        random string
      </div>
    </div>`;

    var searchText = 'SOMETHING';

    const htmlDoc = new DOMParser().parseFromString(htmlSnippet, 'text/html');

    const xpathResult = SaxonJS.XPath.evaluate(
      `let $text-nodes := //text()[contains(., $search-text)]
    return innermost(//*[every $text in $text-nodes satisfies descendant::text() intersect $text])`, 
      htmlDoc, 
      { params : { 'search-text' : searchText } }
    );

    console.log(xpathResult);

<!-- language: lang-html -->

    <script src="https://martin-honnen.github.io/Saxon-JS-2.5/SaxonJS2.rt.js"></script>

<!-- end snippet -->


  [1]: https://www.saxonica.com/saxon-js/index.xml
