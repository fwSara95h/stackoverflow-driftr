---
title: "How to select the lowest common ancestor of elements containing specific text?"
site: stackoverflow
question_id: 74202555
answer_id: 74202612
url: https://stackoverflow.com/a/74202612
author: "CertainPerformance"
author_url: https://stackoverflow.com/users/9515207
posted: 2022-10-26T04:09:47Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 73cf426fb450ba5d8fe3eb5062326041e2d0588fc207a51bf475787aa558e046
role: another answer on the same question, kept as context; not my work
---

# Answer by [CertainPerformance](https://stackoverflow.com/users/9515207) — 2022-10-26

Posted on Stack Overflow, <https://stackoverflow.com/a/74202612>, 2022-10-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

By [selecting all text nodes](https://stackoverflow.com/questions/2579666/getelementsbytagname-equivalent-for-textnodes), you can then iterate through their ancestors and keep only the one(s) that exist for all of them.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function nativeTreeWalker() {
        var walker = document.createTreeWalker(
            document.body, 
            NodeFilter.SHOW_TEXT, 
            null, 
            false
        );

        var node;
        var textNodes = [];

        while(node = walker.nextNode()) {
            textNodes.push(node);
        }
        return textNodes;
    }


    const nodes = nativeTreeWalker()
      .filter(textNode => textNode.textContent.includes('SOMETH\ING'));
    const getAncestors = elm => {
      const set = new Set();
      while (elm) {
        set.add(elm);
        elm = elm.parentElement;
      }
      return set;
    };
    const ancestors = nodes.map(getAncestors);
    const innermostExistingInAll = [...ancestors[0]].find(
      possibleParent => ancestors.every(set => set.has(possibleParent))
    );
    console.log(innermostExistingInAll);

<!-- language: lang-html -->

    <div> <!-- A -->
      <div> <!-- B -->
        <div id="c"> <!-- C: I need to select this element -->
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
    </div>


<!-- end snippet -->

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Damzaky](https://stackoverflow.com/users/7552340)** (2022-10-26): seems like this does answer my question, however I think this solution seems to be so complicated for such a simple problem, not sure if it could be improved myself though (just thought that it could be simpler). For now I will upvote your answer, if there are no other solutions that are better than this, I will accept this answer later, thanks
- **[CertainPerformance](https://stackoverflow.com/users/9515207)** (2022-10-26): Most of it is boilerplate - there are just some things (selecting text nodes, selecting all ancestors) that there aren't built-in methods for, that you have to implement yourself. Take that away, and you're left with 3 lines of code if you inline the array callbacks (depends on your linting preferences) - which is close to the best you can get, I'd think
