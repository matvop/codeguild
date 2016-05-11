'use strict';

function submitJoke() {
    return true;
}

function registerGlobalEventHandlers() {
    $('form').on('submit', function (event) {
        event.preventDefault();
        submitJoke();
        $('.setup').val('');
        $('.punchline').val('');
    });
}

function setFocusToTextBox(){
    $('.setup').focus();
}


$(document).ready(function () {
    // registerGlobalEventHandlers();
    setFocusToTextBox();
});
