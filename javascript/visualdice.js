// Practice: Visual Dice
// Save your solution as visualdice.html, visualdice.css, and visualdice.js.
//
// Give the user a number input box with a button 'roll'. When they click that button, make that many 6-sided dice appear on the screen.
//
// The dice should appear visually as dice, although for testing you can just start with numbers. Come up with any reasonable way to display the visual dice.
//
// If the user clicks any of the dice, it re-rolls just that one. If they re-click the roll button, erase the dice and roll new ones.
//
// At the bottom of the screen, show the sum of all the dice currently out.



'use strict';


function removeTileElement(tile) {
    return tile.remove();
}

function updateDiceArray() {
    var diceArray = [];
    $(".tile").each(function(index, element) {
        diceArray.push(element.id);
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

    var tileElement = $('<div></div>');
    tileElement.toggleClass('tile');
    tileElement.addClass('spinEffect');
    if (dieNumber === 6){
        tileElement.addClass('six');
    }
    tileElement.append(dieImageElement);
    tileElement.attr('id', dieNumber);
    tileElement.on('click', function (event) {
        var newDie = reRollDie();
        replaceDie(tileElement, newDie);
        main();
    });
    return tileElement;
}

function addTileToGrid(tileElement) {
    return $('.grid').append(tileElement);
}

function replaceDie(oldDie, newDie) {
    oldDie.replaceWith(newDie);
}

function reRollDie() {
    var numberOfSides = getSides();
    var dieNumber = genDieNumber(numberOfSides);
    var dieTileElement = createDieTileElement(dieNumber);
    return dieTileElement;
}

function rollDice() {
    if ($('.tile').length === 0) {
        for (var quantity = getNumberOfDice(); quantity > 0; quantity--) {
            var numberOfSides = getSides();
            var dieNumber = genDieNumber(numberOfSides);
            var dieTileElement = createDieTileElement(dieNumber);
            addTileToGrid(dieTileElement);
        }
    }
}

function main() {
    rollDice();
    var diceArray = updateDiceArray();
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
