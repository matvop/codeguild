"use strict";

function getImageUrl() {
    return $("#url-input").val();
}

function createDelLink(tileElement) {
    var delLink = $("<a></a>").text("X").attr("href", "");
    delLink.on("click", function (event) {
        event.preventDefault();
        tileElement.remove("div");
        updateTileCount();
    });
    return delLink;
}

function createTileElement(url) {
    var imageElement =  $("<img></img>").attr("src", url);
    var fullSizeLink = $("<a></a>").attr("href", url).append(imageElement).toggleClass("image-popup-no-margins");
    var tileElement = $("<div></div>").append(fullSizeLink).toggleClass("tile");
    var paraElement = $("<p></p>").text(url);
    var delLink = createDelLink(tileElement);
    var flexDivElement = $('<div></div>').toggleClass("flex").append(paraElement).append(delLink);
    tileElement.append(flexDivElement);
    return tileElement;
}

function getUrlAndAddToGrid() {
    var imgUrl = getImageUrl();
    var imageElement = createTileElement(imgUrl);
    return $('section').append(imageElement);
}

function updateTileCount() {
    var tileCount = $('.tile').length;
    return $('.dynamic').text('Images in your album: ' + tileCount);
}

function registerGlobalEventHandlers() {
    updateTileCount();
    $("form").on("submit", function (event) {
        event.preventDefault();
        getUrlAndAddToGrid();
        updateTileCount();
        $('form').children('#url-input').val('');
        $('.image-popup-no-margins').magnificPopup({
    		type: 'image',
    		closeOnContentClick: true,
    		closeBtnInside: false,
    		fixedContentPos: true,
    		mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
    		image: {
    			verticalFit: true
    		},
    		zoom: {
    			enabled: true,
    			duration: 1000 // don't foget to change the duration also in CSS
    		}
        });
    });
}


$(document).ready(function () {
    registerGlobalEventHandlers();
});
