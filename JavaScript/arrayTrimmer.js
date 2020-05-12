const numArray = [1, 2, 3, 4, 5];

const arrayTrimmer = function (someArray) {
    someArray.pop();
    someArray.shift();
    return someArray;
}

console.log(arrayTrimmer(numArray));