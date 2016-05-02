"use strict";

function getImageUrl() {
    return $("#url-input").val();
}

function createDelLink(tileElement) {
    var delLink = $("<a></a>").text("X").attr("href", "");
    delLink.on("click", function (event) {
        event.preventDefault();
        tileElement.remove("div");
        includeTileCount();
    });
    return delLink;
}

function createImageElement(url) {
    var imageElement =  $("<img></img>").attr("src", url);
    var tileElement = $("<div></div>").append(imageElement).toggleClass("tile");
    var paraElement = $("<p></p>").text(url);
    var delLink = createDelLink(tileElement);
    var flexDivElement = $('<div></div>').toggleClass("flex").append(paraElement).append(delLink);
    tileElement.append(flexDivElement);
    return tileElement;
}

function getUrlAndAddToGrid() {
    var imgUrl = getImageUrl();
    var imageElement = createImageElement(imgUrl);
    return $('section').append(imageElement);
}

function includeTileCount() {
    var tileCount = $('.tile').length;
    return $("h2").text('Images uploaded: ' + tileCount);
}

function registerGlobalEventHandlers() {
    $("form").on("submit", function (event) {
        event.preventDefault();
        getUrlAndAddToGrid();
        includeTileCount();
    });
}

$(document).ready(function () {
    registerGlobalEventHandlers();
});
