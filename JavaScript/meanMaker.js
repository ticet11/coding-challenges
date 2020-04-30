// Takes array of numbers as input. Finds the mean of the numbers in the array.
const meanMaker = coolArray => coolArray.reduce((a, b) => a + b) / coolArray.length;

meanMaker([1, 2, 3]);
