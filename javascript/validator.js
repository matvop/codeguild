"use strict";


function validateForm() {
    if (validateName() === false) {
        alert("Name must be filled out");
        return false;
    }
    if (validateDate() === false) {
        alert("Date of birth must be filled out");
        return false;
    }
    if (validatePhone() === false) {
        alert("Phone number must be filled out");
        return false;
    }
}

function isAlphaOrSpace(str) {
    return /^[a-z ]+$/i.test(str);
}

function isValidDate(str) {
    var dateVal = str;
    if (dateVal === null) {
        return false;
    }
    var validatePattern = /^(\d{4})(\/|-)(\d{1,2})(\/|-)(\d{1,2})$/;
    var dateValues = dateVal.match(validatePattern);
    if (dateValues === null) {
        return false;
    }
    var dtYear = dateValues[1];
    var dtMonth = dateValues[3];
    var dtDay=  dateValues[5];
    if (dtMonth < 1 || dtMonth > 12) {
        return false;
    }
    else if (dtDay < 1 || dtDay > 31) {
        return false;
    }
    else if ((dtMonth === 4 || dtMonth === 6 || dtMonth === 9 || dtMonth === 11) && dtDay === 31) {
        return false;
    }
    else if (dtMonth === 2) {
        var isleap = (dtYear % 4 === 0 && (dtYear % 100 != 0 || dtYear % 400 === 0));
        if (dtDay> 29 || (dtDay === 29 && !isleap)) {
            return false;
        }
    }
     return true;
}

function isValidPhone(str) {
    return /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/.test(str);
}

function isValidNameCount(str) {
    var nameArray = str.split(" ");
    return nameArray.length === 2;
}

function validateName() {
    var nameString = document.getElementById("name").value;
    var countCheck = isValidNameCount(nameString);
    var nameArray = nameString.split(" ");
    var lastName = nameArray[0];
    var firstName = nameArray[1];
    var responseFirst = isAlphaOrSpace(lastName);
    var responseLast = isAlphaOrSpace(firstName);
    if (responseLast === true && responseFirst === true && countCheck === true) {
        document.getElementById("name").style.backgroundColor = "lightgreen";
    }
    else if (responseLast === false || responseFirst === false || countCheck === false) {
        document.getElementById("name").style.backgroundColor = "pink";
        return false;
    }
}

function validateDate() {
    var dateString = document.getElementById("dob").value;
    var response = isValidDate(dateString);
    if (response === true) {
        document.getElementById("dob").style.backgroundColor = "lightgreen";
    }
    else if (response === false) {
        document.getElementById("dob").style.backgroundColor = "pink";
        return false;
    }
}

function validatePhone() {
    var phoneString = document.getElementById("phone-num").value;
    var response = isValidPhone(phoneString);
    if (response === true) {
        document.getElementById("phone-num").style.backgroundColor = "lightgreen";
    }
    else if (response === false) {
        document.getElementById("phone-num").style.backgroundColor = "pink";
        return false;
    }
}
