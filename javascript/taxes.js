"use strict";

var oregonTax = function(amount) {
    var tax;
    if (amount >= 125001) {
        tax = ((amount - 125000) * .099) + (116559 * .09) + (5049 * .07) + (3350 * .05);
    }
    else if (amount >= 8401 && amount < 125001) {
        tax = ((amount - 8400) * .09) + (5049 * .07) + (3350 * .05);
    }
    else if (amount >= 3351 && amount <= 8400) {
        tax = ((amount - 3350) * .07) + (3350 * .05);
    }
    else {
        tax = (amount * .05);
    }
    return Math.ceil(tax);
}

console.log(oregonTax(50000));
