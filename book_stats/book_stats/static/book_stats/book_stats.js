'use strict';


function getTitle() {
    $.ajax({
        url: '/title',
        type: 'GET',
        success: function(result) {
            $('#book-title').text(result);
        }
    });
}

function getCount() {
    $.ajax({
        url: '/count',
        data: {'word': $('#word-input').val().toLowerCase()},
        type: 'GET',
        success: function(result) {
            $('#word-and-count').text(result);
        }
    });
}

function getTop10() {
    $.ajax({
        url: '/top10',
        type: 'GET',
        success: function(result) {
            var top10 = $('<article></article>').attr('id', 'top10-list');
            $('.main').append(top10);
            top10.text(result);
        }
    })
}

function registerGlobalEventHandlers() {
    $('form').on('submit', function (event) {
        event.preventDefault();
        $('article').remove();
        getCount();
        if ($('#checkbox').is(':checked')) {
            getTop10();
        }
        $('#word-input').val('');
        $('#checkbox').val('');
    });
}

function setFocusToTextBox(){
    $('#word-input').focus();
}


$(document).ready(function () {
    getTitle();
    registerGlobalEventHandlers();
    setFocusToTextBox();
});
