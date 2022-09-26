---
title: "Embedding html/css in javascript output"
site: stackoverflow
question_id: 73804569
answer_id: 73848802
url: https://stackoverflow.com/a/73848802
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-26T01:09:20Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73848802/revisions
accepted: false
score: 1
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bc4666d7227d21c69f377cf3c51ba9ddf284644096d98f263433d375fa0cd04f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73848802>, 2022-09-26; score 1. Text as retrieved 2026-10-12.

Maybe you should have the output as a list of objects [each row as an object] and then convert to html table. You could define a function like :

    function jsonToTable(jsOp, colNames){
        var op = '', rowHtml = '';
        for (let c=0; c<colNames.length; c++) {
            rowHtml += `<th>${colNames[c]}</th>`;
        }
        op += `<tr>${rowHtml}</tr>`;
        for (let r=0; r< jsOp.length; r++){
            rowHtml = ''; var rowData = jsOp[r];
            var rowStyle = i%2==0 ? '' : ' style="border-bottom: 1px solid black;';
            for (let c=0; c<colNames.length; c++) {
                var colName = colNames[c];
                rowHtml += `<td>${rowData[colName]}</td>`;
            }
            op += `<tr ${rowStyle}>${rowHtml}</tr>`;
        }
        return `<table>${op}</table>`;
    }
and then just call as `output = jsonToTable(opObj, colHeaders);` and from what I can see from your example, your `opObj` and `colHeaders` would look like:

    var opObj = [
        {
            'col1Name': `Batch ${z(idx + 1, 2)}A`,
            'col2Name': `${prefix} ${A1}`,
            'col3Name': `${prefix} ${A2}`,
        },
        {
            'col1Name': `Batch ${z(idx + 1, 2)}B`,
            'col2Name': `${prefix} ${B1}`,
            'col3Name': `${prefix} ${B2}`,
        }
    ]
    var colHeaders = ['col1Name', 'col2Name', 'col3Name']

(As far as I can tell, '<' and '>' do not need to be escaped with backslash.)

Also, if you're willing to add a stylesheet or a style block with css, you can take a look at [this striped table example][1], and then you can forego the `rowStyle` bits.

For me, at least, that would make the code look a bit cleaner.

  [1]: https://www.w3schools.com/css/tryit.asp?filename=trycss_table_striped
