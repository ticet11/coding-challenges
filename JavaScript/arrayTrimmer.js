const numArray = [1, 2, 3, 4, 5];
// // Basic functioning trimmer.
// const arrayTrimmer = function (someArray) {
//     someArray.pop();
//     someArray.shift();
//     return someArray;
// }

// // Cleaner version
// const arrayTrimmer = function (someArray) {
//     return someArray.slice(1, -1);
// }

// Checks for incorrect inputs.
const arrayTrimmer = function (someArray) {
    if (Array.isArray(someArray) === false) return "Please enter an array.";
    if (someArray.length < 3)
      return "Please enter an array with at least 3 items.";
    return someArray.slice(1, -1);
  };

console.log(arrayTrimmer(numArray));