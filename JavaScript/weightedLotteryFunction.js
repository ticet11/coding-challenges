const someWeights = {
    win: 1,
    draw: 4,
    lose: 5
};

const weightedLottery = function(weights) {
    const weightsArray = [];
    for (const weight of Object.entries(weights)) {
        for (let i = 0; i < weight[1]; i++) {
          weightsArray.push(weight[0]);
        }
    };
    const solution = weightsArray[Math.floor(Math.random() * weightsArray.length)];
    return solution;
};

console.log(weightedLottery(someWeights));