'use strict;'


function createDelLink(tileElement) {
    var delLink = $('<a></a>').text('X').attr('href', '').toggleClass('delLink');
    delLink.on('click', function (event) {
        event.preventDefault();
        removeTileElement(tileElement);
        main();
    });
    return delLink;
}

function reRollDie() {

}

function removeTileElement(tile) {
    return tile.remove();
}

function updateDiceArray() {
    var diceArray = [];
    $(".tile").each(function() {
        diceArray.push(this.id);
    });
    return diceArray.map(Number);
}

function getSum(total, num) {
    return total + num;
}

function getScore(array) {
    return array.reduce(getSum, 0);
}

function updateScore(score) {
    return $('.dynamic').text('Your score: ' + score);
}

function getDieImgURL(dieNumber) {
    if (dieNumber < 7) {
        var urlPrefix = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Dice-';
        var dieImageURL = (urlPrefix + dieNumber + '.svg/200px-Dice-' + dieNumber + '.svg.png')
        return dieImageURL;
    }
    else if (dieNumber === 7) {
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Dice-7a.svg/200px-Dice-7a.svg.png';
    }
    else if (dieNumber === 8) {
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Dice-8a.svg/200px-Dice-8a.svg.png';
    }
    else if (dieNumber === 9) {
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Dice-9a.svg/200px-Dice-9a.svg.png';
    }
}

function getNumberOfDice() {
    return $("#dice-quantity").val();
}

function getSides() {
    return $("#number-of-sides").val();
}

function genDieNumber(max) {
    var dieNumber = Math.floor(Math.random() * (max - 1 + 1)) + 1;
    return dieNumber;
}

function createDieTileElement(dieNumber) {
    var imageURL = getDieImgURL(dieNumber);

    var dieImageElement = $('<img></img>');
    dieImageElement.toggleClass('die');
    dieImageElement.attr('src', imageURL);

    var divForDie = $('<div></div>');
    divForDie.toggleClass('div-for-die');
    divForDie.append(dieImageElement);

    var removeDieLinkElement = $('<div></div>');
    removeDieLinkElement.toggleClass('removeDie');

    var tileElement = $('<div></div>');
    tileElement.toggleClass('tile');
    tileElement.append(divForDie);
    tileElement.attr('id', dieNumber);

    var delLink = createDelLink(tileElement);
    removeDieLinkElement.append(delLink);
    tileElement.prepend(removeDieLinkElement);

    return tileElement;
}

function addTileToGrid(tileElement) {
    return $('.grid').append(tileElement);
}

function main() {
    if ($('.tile').length === 0) {
        for (var quantity = getNumberOfDice(); quantity > 0; quantity--) {
            var numberOfSides = getSides();
            var dieNumber = genDieNumber(numberOfSides);
            var dieTileElement = createDieTileElement(dieNumber);
            addTileToGrid(dieTileElement);
        }
    }
    diceArray = updateDiceArray();
    var score = getScore(diceArray);
    updateScore(score);
}

function registerGlobalEventHandlers() {
    $("form").on("submit", function (event) {
        event.preventDefault();
        $('.tile').remove();
        main();
    });
}

function setFocusToTextBox(){
    $('#number-of-sides').focus();
}

$(document).ready(function () {
    registerGlobalEventHandlers();
    setFocusToTextBox();
});
