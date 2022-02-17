/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    let origin = x.toString();
    let reversed = origin.split("").reverse().join("");
    return reversed === origin;
};