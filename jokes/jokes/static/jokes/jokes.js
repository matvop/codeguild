'use strict';


function registerGlobalEventHandlers() {
    $('.joke-tile').on('click', function (event) {
        $(event.target).children().css('visibility', 'visible');
    });
}

function setFocusToTextBox() {
    $('.setup').focus();
}

function genRandomIndex() {
    var randNum = Math.floor(Math.random() * (6));
    return randNum;
}

function genRandomID() {
    var prefixList = ['blue', 'red', 'green', 'purple', 'orange', 'cyan'];
    console.log(genRandomIndex());
    var randID = prefixList[genRandomIndex()];
    return randID;
}

function assignRandIDToTile() {
    $('article').each(function() {
        var id = genRandomID();
        $(this).attr('id', id);
    });
}


$(document).ready(function () {
    registerGlobalEventHandlers();
    assignRandIDToTile();
    setFocusToTextBox();
});
