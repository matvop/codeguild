'use strict;'


function createDelLink(tileElement) {
    var delLink = $('<a></a>').text('X').attr('href', '');
    delLink.on('click', function (event) {
        event.preventDefault();
        tileElement.remove('.die');
    });
    return delLink;
}

function createDieTileElement(dieNumber) {
    var dieElement =  $('<div></div>').toggleClass('die').text('dieNumber');
    var tileElement = $('<div></div>').toggleClass('tile').append(dieElement);
    var delLink = createDelLink(tileElement);
    var flexDivElement = $('<div></div>').toggleClass('removeDie').append(delLink);
    tileElement.append(flexDivElement);
    return tileElement;
}

function updateTileCount() {
    var tileCount = $('.tile').length;
    return $('.dynamic').text('Media tiles in your gallery: ' + tileCount);
}

function getDieNumber() {
    return $("#dice-quantity").val();
}

function getUrlAndAddImgToGrid(imgURL) {
    var tileElement = createImgTileElement(imgURL);
    return $('section').append(tileElement);
}

function main() {
    var designation = getDieNumber();


}

function registerGlobalEventHandlers() {
    updateTileCount();
    $("form").on("submit", function (event) {
        event.preventDefault();
        getUploadedMediaType(); //added to test mediaURL
        updateTileCount();
        $('#url-input').val('');
    });
}
