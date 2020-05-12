const numArray = [1, 2, 3, 4, 5];

// const arrayTrimmer = function (someArray) {
//     someArray.pop();
//     someArray.shift();
//     return someArray;
// }

// Cleaner version
const arrayTrimmer = function (someArray) {
    return someArray.slice(1, -1);
}

console.log(arrayTrimmer(numArray));