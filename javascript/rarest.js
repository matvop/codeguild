// Practice: Rarest
// Given an object that maps names to ages, find the rarest age.

"use strict";

var namesToAges = {
    "Alyssa": 22,
    "Charley": 25,
    "Dan": 25,
    "Jeff": 20,
    "Kasey": 20,
    "Kim": 20,
    "Morgan": 25,
    "Ryan": 25,
    "Stef": 22
};

var findAges = function(namesWithAges) { // creates an array of all the ages
    var ages = [];
    for (name in namesWithAges) {
        var age = namesWithAges[name];
        ages = ages.concat(age);
    }
    return ages;
};

var createFreqObj = function(agesArray) { // creates an obj of ages and frequency of occurance
    var agesFrequency = {};
    for (var age in agesArray) {
        agesFrequency[agesArray[age]] = (agesFrequency[agesArray[age]] || 0) + 1; // increment frequency.
    }
    return agesFrequency;
};

var pairsArray = function(agesWithFreq) { // creates array of key/value pairs and sorts by least frequent
    var sortable = [];
    for (var age in agesWithFreq) {
        sortable.push([age, agesWithFreq[age]]);
    }
    return sortable.sort();
};

console.log(pairsArray(createFreqObj(findAges(namesToAges)))[0]);
