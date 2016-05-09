// Practice: Whack-A-Mole
// Save your solution as mole.html, mole.css, and mole.js.
//
// Make a 5x4 grid of hole images. Every second, randomly pick a hole in the
// grid and turn it's image into a mole. If the user clicks on a mole image,
// turn it back into a hole.
//
// Use the setInterval function to run a callback function periodically.
'use strict';


function createColumn() {
    var col = $('<article></article>');
    col.toggleClass('column');
    return col;
}

function createTileElement() {
    var imageElement = $('<img></img>');
    imageElement.toggleClass('hole');
    imageElement.attr('src', 'hole.png');
    var tileElement = $('<div></div>');
    tileElement.toggleClass('tile');
    tileElement.append(imageElement);
    return tileElement;
}

function createRowsAndTilesThenPopulateTheBoard() {
    var imgArray = [];
    for (var colNum = 1; colNum < 6; colNum++) {
        var articleCol = createColumn();
        $('.grid').append(articleCol);
        for (var tileNum = 1; tileNum < 5; tileNum++) {
            var tile = createTileElement();
            var tileIMG = tile.find('img');
            imgArray.push(tileIMG);
            articleCol.append(tile);
        }
    }
    return imgArray;
}

function getEmptyHole(imgArray) {
    var i = Math.round((Math.random()) * imgArray.length);
    if (i === imgArray.length) --i;
    var randomHole = $(imgArray[i]);
    return randomHole;
}

function animateTheBoard(imgArray) {
    var counter = {i : []};
    var animate = setInterval(function() {
        var i = Math.round((Math.random()) * imgArray.length);
        if (i === imgArray.length) --i;
        var randomHole = $(imgArray[i]);
        counter.i.push(randomHole);
        if (randomHole.attr('src') === 'mole.png') {
            getEmptyHole(imgArray);
        }
        randomHole.attr('src', 'mole.png');
        randomHole.on('click', function (event) {
            randomHole.attr('src', 'hole.png');
        });
    }, 1000);
    $('#stop').on('click', function (event) {
        clearInterval(animate);
        // $('article').remove();
    });
    return animate;
}


function main() {
    var hitAndMissArray = [];
    var tileElement = createTileElement();
    var imgArray = createRowsAndTilesThenPopulateTheBoard();
    animateTheBoard(imgArray);
}

function registerGlobalEventHandlers() {
    $("#start").on("click", function (event) {
        $('article').remove();
        main();
    });
    // $('#stop').on('click', function (event) {
    //     clearInterval(animateTheBoard());
    //     // $('article').remove();
    // });
}


$(document).ready(function() {
    registerGlobalEventHandlers();
})
