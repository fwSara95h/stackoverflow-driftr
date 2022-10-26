---
title: "How to select the lowest common ancestor of elements containing specific text?"
site: stackoverflow
question_id: 74202555
answer_id: 74203457
url: https://stackoverflow.com/a/74203457
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-26T06:23:56Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74203457/revisions
accepted: true
score: 0
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5a85bbdade0a1524e282ae1094beea1f37469c199f59650db9ff26b8441db176
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74203457>, 2022-10-26; **accepted**; score 0. Text as retrieved 2026-10-12.

You could just traverse downwards from the outermost element until a descendant has more than 1 child containing the text:

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    let commonAnc;
    let hasTxt = [document.getElementById('mainContainer')]; // or whatever outermost element you want 

    while(hasTxt.length == 1) {
      commonAnc = hasTxt[0]; hasTxt = []; 
      let caChilds = commonAnc.children;

      for(let i=0; i<caChilds.length; i++) {
        if (caChilds[i].textContent.includes("SOMETHING")){
          hasTxt.push(caChilds[i]); 
        } 
      }
    }

    console.log(commonAnc);

<!-- language: lang-html -->

    <div id="mainContainer"> 
    <div id="a"> <!-- A -->
      <div id="b"> <!-- B -->
        <div id="c"> <!-- C: I need to select this element -->
          <div id="d">
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
    </div>


<!-- end snippet -->

Feels rather inefficient, but [I think] it's the simplest way, considering that there seems to be no in-built methods for getting the closest common ancestor...
