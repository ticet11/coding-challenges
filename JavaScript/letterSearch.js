const letterSearch = (someString) => {
    const alphabet = "abcdefghijklmnopqrstuvwxyz";
    let binaryOutput = "";

    for (letter of alphabet) {
        if (someString.toLowerCase().includes(letter)) {
            binaryOutput += "1";
        } else {
            binaryOutput += "0";
        }
    }
    return binaryOutput;
};

console.log(letterSearch('ABCDkkDsl'))