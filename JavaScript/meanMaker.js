meanMaker = (coolArray) => {
    return coolArray.reduce((a, b) => a + b, 0) / coolArray.length;
};

meanMaker([1, 2, 3]);
