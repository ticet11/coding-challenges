function randomColor() {
    const digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    let hex = '#';

    for (let i = 0; i < 6; i++) {
        hex += digits[Math.floor(Math.random() * 16)];
    }

    return hex;
}

console.log(randomColor())
