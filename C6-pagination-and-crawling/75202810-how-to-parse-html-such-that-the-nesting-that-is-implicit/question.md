---
title: "How to parse html such that the nesting that is implicit by header levels becomes explicit?"
site: stackoverflow
question_id: 75202810
url: https://stackoverflow.com/q/75202810
asked: 2023-01-22T18:17:22Z
asked_by: "psychicesp"
asked_by_url: https://stackoverflow.com/users/13741789
last_edited: never
tags: [python, html, json, beautifulsoup]
score: 0
views_at_snapshot: 95
answer_count: 1
accepted_answer_id: 75263236
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f4c8fdfd7452ad442567325651d7789f4606e13c8b106ffc2b00256f5aea9a7a
---

# How to parse html such that the nesting that is implicit by header levels becomes explicit?

Asked by [psychicesp](https://stackoverflow.com/users/13741789) on Stack Overflow, <https://stackoverflow.com/q/75202810>, 2023-01-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I run into the same problem in a different form while web-scraping, over and over, and for some reason I can't seem to push my head through it.

The core of it is basically this:

HTML has a relatively flat organizational structure with some nesting implicit.  I want to make that explicit.

To show what I mean consider the following fictional menu snippet:

> # Motley Mess Menu
> 
> ## Breakfast
> 
> ### Omelets
> 
> #### Cheese
> 
> $7
> 
> American style omelet containing your choice of Cheddar, Swiss, Feta,
> Colby Jack or all four!
> 
> #### Sausage Mushroom
> 
> $8
> 
> American style omelet containing sausage, mushroom and Swiss cheese
> 
> #### Build-Your-Own
> 
> $8
> 
> American style omelet containing…you tell me!
> 
> Options (+50 cents after 3):
> 
> *   Cheddar
> *   Swiss
> *   Feta
> *   Colby Jack
> *   Bacon Bits
> *   Sausage
> *   Onion
> *   Hamburger
> *   Jalapenos
> *   Hash Browns
> 
> ### Combos
> ...

When we read this menu we know that "Sausage Mushroom" is a type of "Omelet" served for "Breakfast" at the "Motley Mess."  We understand the nesting just fine, however if this were represented via html (or in markdown for that matter) all of those headers are flat, and without ading a series of divs that nesting is all implicit.  If I'm web scraping I have no control over whether or not those divs are present.

I want to parse the html to make that nesting explicit.  This is a problem I have come across time and time again scraping websites and I always find another way to solve the problem.  I feel that this should be a relatively basic problem to solve, if not simple, but for some reason I can't get past the weird dynamic recursion that ends up necessary, and I think I'm grossly overcomplicating it.

This last snippet is an html json pair which I would be happy with from a hypothetical html_unpacker function:

``` python
html_string = """
<h1>Motley Mess Menu</h1>
<h2>Breakfast</h2>
<h3>Omelets</h3>
<h4>Cheese</h4>
<p>$7</p>
<p>American style omelet containing your choice of Cheddar, Swiss, Feta, Colby Jack or all four!</p>
<h4>Sausage Mushroom</h4>
<p>$8</p>
<p>American style omelet containing sausage, mushroom and Swiss cheese</p>
<h>Build-Your-Own</h4>
<p>$8</p>
<p>American style omelet containing…you tell me!</p>
<p>Options (+50 cents after 3):</p>
<ul>
<li>Cheddar</li>
<li>Swiss</li>
<li>Feta</li>
<li>Colby Jack</li>
<li>Bacon Bits</li>
<li>Sausage</li>
<li>Onion</li>
<li>Hamburger</li>
<li>Jalapenos</li>
<li>Hash Browns</li>
</ul>
<h3>Combos</h3>
<p>Each come with your choice of two sides</p>
<h4>Eggs and Bacon</h4>
<p>$8</p>
<p>Eggs cooked your way and crispy bacon. Sausage substitution is fine</p>
<h4>Glorious Smash</h4>
<p>$10</p>
<p>Your favorite breakfast of two pancakes, two eggs cooked your way, two sausages and two bacon, free of all trademark infringement! If you think you can finish it all then you forgot about the choice of two sides!</p>

html_unpacker(html_string)
```

output:

``` json
{
    "Motley Mess Menu": {
        "Breakfast": {
            "Omelets": {
                "Cheese": {
                    "p1": "$7",
                    "p2": "American style omelet containing your choice of Cheddar, Swiss, Feta, Colby Jack or all four!"
                },
                "Sausage Mushroom": {
                    "p1": "$8",
                    "p2": "American style omelet containing sausage, mushroom and Swiss cheese"
                },
                "Build-Your-Own": {
                    "p1": "$8",
                    "p2": "American style omelet containing…you tell me!",
                    "p3": "Options (+50 cents after 3):",
                    "ul1": {
                        "li1": "Swiss",
                        "li2": "Feta",
                        "li3": "Colby Jack",
                        "li4": "Bacon Bits",
                        "li5": "Sausage",
                        "li6": "Onion",
                        "li7": "Hamburger",
                        "li8": "Jalapenos",
                        "li9": "Hash Browns"
                    }
                }
            },
            "Combos": {
                "p1": "Each come with your choice of two sides",
                "Eggs and Bacon": {
                    "p1": "$8",
                    "p2": "Eggs cooked your way and crispy bacon. Sausage substitution is fine"
                },
                "Glorious Smash": {
                    "p1": "$10",
                    "p2": "Your favorite breakfast of two pancakes, two eggs cooked your way, two sausages and two bacon, free of all trademark infringement! If you think you can finish it all then you forgot about the choice of two sides!"
                }
            }
        }
    }
}
```

I don't necessarily need that exact style of output, just something that makes the nesting explicit and maintins the type ond order on non-header elements.  I need explicit nestig to be preserved (lists within lists and whatnot) I just need to add some explicit nesting based on header levels.

I'm not asking for someone to build a function from scratch, this just seems so basic I feel like something of this nature must already exist and my google-fu must just be failing me.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Shiping](https://stackoverflow.com/users/6918481)** (2023-01-22): Probably the key is to get a function that can be called recursively for every recognized html tag, increasing indentation by one for each opening tag and reducing indentation by one for each closing tag.  Of course the function should call itself for each opening tag and return for each closing tag. BTW you have a typo at the line <h>Build-Your-Own</h4>, <h> should be <h4>, I think.
