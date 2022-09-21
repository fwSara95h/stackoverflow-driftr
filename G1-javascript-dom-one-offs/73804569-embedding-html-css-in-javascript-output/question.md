---
title: "Embedding html/css in javascript output"
site: stackoverflow
question_id: 73804569
url: https://stackoverflow.com/q/73804569
asked: 2022-09-21T17:07:57Z
asked_by: "Ringthane"
asked_by_url: https://stackoverflow.com/users/20007308
last_edited: 2022-09-21T17:33:29Z
tags: [javascript, html]
score: 0
views_at_snapshot: 65
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e9c37af371ac63c61fa2c8c37f05b3b773d5eba7e369248a4f1ba46b736b2a84
---

# Embedding html/css in javascript output

Asked by [Ringthane](https://stackoverflow.com/users/20007308) on Stack Overflow, <https://stackoverflow.com/q/73804569>, 2022-09-21, last edited 2022-09-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

All, I have this output that I am exporting `onclick` to excel:
    
    const final = totalBatches.reduce((AB, now, idx) => {
    let A1 = z(AB, 8);
    let A2 = z(AB + now / 2 - 1, 8);
    let B1 = z(AB + now / 2, 8);
    let B2 = z(AB + now - 1, 8);
    output += `Batch ${z(idx + 1, 2)}A | ${prefix} ${A1} - ${prefix} ${A2}\n`;
    output += `Batch ${z(idx + 1, 2)}B | ${prefix} ${B1} - ${prefix} ${B2}\n`;
    return AB + now;
    }, init);

    outputEl.innerHTML = output;
    }

The problem is, it needs to be formatted into separate columns so the excel sheet is formatted properly. So I added the following to `output +=`:

    output += `\<tr\>\<td\>Batch ${z(idx + 1, 2)}A \</td\>\<td\>${prefix} ${A1} \</td\>\<td\>${prefix} ${A2}\</td\>\</tr\>\n`;
    output += `\<tr style="border-bottom: 1px solid black;"\>\<td\>Batch ${z(idx + 1, 2)}B \</td\>\<td\>${prefix} ${B1} \</td\>\<td\>${prefix} ${B2}\</td\>\</tr\>\n`;

This (mostly) works. My excel export is now formatted into separate columns. But there are at least two problems. 1, it's ugly/clunky and hard to read... there has to be a more efficient way of doing this.

2, I haven't figured out a way for this output to have inline style for the user to have visual cues on the html page before export (I want every other row to be underlined or colored for ease of reading).

I'm kindergarten level Javascript... do I use `encodeURIComponent()` or another global method?

Could I do something like 

    let TD = fancy.encoded.stringInColumn;

To make this cleaner and format properly? Thanks for any input it's greatly appreciated.

To clarify: this also needs to be displayed in a html page as well as export to Excel.

----------

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Roko C. Buljan](https://stackoverflow.com/users/383904)** (2022-09-21): why don't you use CSV instead of formatting your data into a HTML table
- **[Ringthane](https://stackoverflow.com/users/20007308)** (2022-09-21): I didn't use CSV so the end user wouldn't have to import into Excel.
- **[Roko C. Buljan](https://stackoverflow.com/users/383904)** (2022-09-21): I've read many times your question and I'm still unable to understand your problem. And the desired output string.
- **[Ringthane](https://stackoverflow.com/users/20007308)** (2022-09-21): The problems:   1. the code itself is hard to read. I'm asking if there's a cleaner way.  2. Inline style isn't rendering correctly so I'm not escaping it properly, the second output row doesn't display a bottom border.
