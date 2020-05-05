import classChallenge, { welcome, summer } from './classChallenge'

let sum = 0;
const sampleArray = [1, 2, 3];

const forSum = (anArray) => {
    let sum = 0;
    for (let num in anArray) {
        sum += anArray[num];
    }
    return sum;
};

console.log(forSum(sampleArray));

function whileSum(anArray) {
    let num = 0;
    while (num < anArray.length) {
        sum += anArray[num];
        num++;
    }
    return sum;
}

console.log(whileSum(sampleArray));

function doWhileSum(anArray) {
    let sum = 0;
    let num = 0;
    do {
        sum += anArray[num];
        num++;
    } while (num < anArray.length);
    return sum;
}

console.log(doWhileSum(sampleArray));

console.log(classChallenge());
console.log(welcome());
console.log(summer(2, 3));
