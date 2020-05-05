// const exponenter = (base, exponent) => {
//     solution = base;
//     for (let i = 0; i < exponent - 1; i++) {
//         solution *= base;
//     }
//     return solution;
// }

// const exponenter = (base, exponent) => {
//     let baseArray = []
//     baseArray.length = exponent;
//     baseArray.fill(base);
//     let solution = baseArray.reduce((total, base) => total * base, 1);
//     return solution;
// }

// const exponenter = (base, exponent) => {
//     let baseArray = Array(exponent);
//     baseArray.fill(base);
//     let solution = baseArray.reduce((total, base) => total * base, 1);
//     return solution;
// }

console.log(exponenter(2, 3));