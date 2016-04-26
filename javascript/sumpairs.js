// Practice: Sum Pairs
// Write a function named find_sum_pairs. It takes two arguments: a list of ints to search, and a sum to find.
//
// Go through the search list and find all pairs of numbers that would add together to the sum.
//
// Example output:
//
// >>> find_sum_pairs([-1, 0, 1, 2], 3)
// [[1, 2]]
// >>> find_sum_pairs([-1, 0, 1, 2], 1)
// [[-1, 2], [0, 1]]
// >>> find_sum_pairs([2, -1, 2], 1)
// [[2, -1], [-1, 2]]
// >>> find_sum_pairs([-1, 1, 2, 2], 3)
// [[1, 2], [1, 2]]

"use strict";

var testList = [-1, 1, 2, 0, 3, -4, -11, 6, -2, 8, 10, 4, -8, 13, -4, 2];
var testSum = 2;

var find_sum_pairs = function(intList, sum) {
    var pairsArray = [];
    for (var i = 0; i < (intList.length - 1); i++) {
        var intOne = intList[i];
        for (var j = i+1; j < intList.length; j++) {
            var intTwo = intList[j];
            if (intOne + intTwo === sum) {
                pairsArray.push([intOne, intTwo]);
            }
        }
    }
    return pairsArray;
};


console.log(find_sum_pairs(testList, testSum));
