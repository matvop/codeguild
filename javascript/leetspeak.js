"use strict";

var convertWordToLeetSpeak = function(originalWord) {
    var originalCharToLeetChar = {
        "o":"0",
        "l":"1",
        "e":"3",
        "a":"4",
        "t":"7",
        "s":"Z"
    }

    for (var originalChar in originalCharToLeetChar) {
        var leetChar = originalCharToLeetChar[originalChar];
        originalWord = originalWord.replace(originalChar, leetChar);
    }


    return originalWord;
}

console.log(convertWordToLeetSpeak("hello"));
