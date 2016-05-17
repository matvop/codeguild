'use strict';


function registerGlobalEventHandlers() {
    $('.setup').on('click', function (event) {
        $(event.target).siblings().css('visibility', 'visible');
    });
}

function setFocusToTextBox() {
    $('.setup').focus();
}

$(document).ready(function () {
    registerGlobalEventHandlers();
    setFocusToTextBox();
});
