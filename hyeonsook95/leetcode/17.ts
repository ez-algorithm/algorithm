function letterCombinations(digits: string): string[] {
    var results = [];
    const digitsObjects = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    };

    const combination = function (idx, result) {
        if (digits.length === result.length) {
            return results.push(result);
        }
        var chars = digitsObjects[digits[idx]];
        for (var char in chars) {
            combination(idx + 1, result + chars[char]);
        }
    };

    var chars = digitsObjects[digits[0]];
    for (var char in chars) {
        combination(1, chars[char]);
    }
    return results;
};