// Code from my Stack Overflow answer https://stackoverflow.com/a/73832607 (posted 2022-09-23), extracted verbatim; may need the question's context to run.
function decodeUrlDefensev3() {
    var link = document.getElementById('textbox1').value;
    var matches = link.match(new RegExp('v3/__(.+?)__;(.*?)!'))

    /*if (!matches || matches.length < 3) {
        alert("Invalid input, could not decode");
        return null;
    }*/

    // love me a mutable array
    var decode_pile = Array.from(matches[1]);
    var chars_pile = Array.from(atob(matches[2])).reverse();

    for (var match of link.matchAll(/\*/g)) {
        decode_pile[match.index] = match.pop()
    }

    return decode_pile.join('')
}
