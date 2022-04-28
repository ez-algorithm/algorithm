function isValid(s) {
    var parentheses = { ")": "(", "]": "[", "}": "{" };
    var temp = [];

    for (var char of s) {
        if ("([{".indexOf(char) > -1) {
            temp.push(char);
        }
        else {
            if (temp.length === 0) {
                return false;
            }
            var top = temp.pop();
            if (top !== parentheses[char]) {
                return false;
            }
        }
    }

    if (temp.length !== 0) {
        return false;
    }
    return true;
};

console.log(isValid(')'));