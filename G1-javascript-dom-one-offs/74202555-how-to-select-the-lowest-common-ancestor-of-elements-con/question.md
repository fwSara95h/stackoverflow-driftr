---
title: "How to select the lowest common ancestor of elements containing specific text?"
site: stackoverflow
question_id: 74202555
url: https://stackoverflow.com/q/74202555
asked: 2022-10-26T03:59:46Z
asked_by: "Damzaky"
asked_by_url: https://stackoverflow.com/users/7552340
last_edited: never
tags: [javascript, html, xpath]
score: 1
views_at_snapshot: 258
answer_count: 3
accepted_answer_id: 74203457
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b148ca7c203b4c09ec2a691ef4c20b24204a8018ab81ec7173cc652ea1fd5071
---

# How to select the lowest common ancestor of elements containing specific text?

Asked by [Damzaky](https://stackoverflow.com/users/7552340) on Stack Overflow, <https://stackoverflow.com/q/74202555>, 2022-10-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm not sure if "lowest common ancestor" is the right term, I also think that this problem should be quite common, I have tried to find the solutions online, but couldn't find it.

So I have below structure:
```
<div> <!-- A -->
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
</div>

```
My goal is to select that first/lowest element (in this case it's div C) that contains all children/descendants that contain string "SOMETHING".

The closest solution that I got was using xpath: `//*[contains(text(),"SOMETHING")]/ancestor::*`, but using this will return basically any elements that contain "SOMETHING" (it does return the div C, but also returns other elements, I only want to get the div C).

The solution doesn't have to be using xpath, but vanilla javascript is preferrable, also it doesn't have to be very efficient. Thanks in advance.
