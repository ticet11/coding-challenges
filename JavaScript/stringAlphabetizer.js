function stringAlphabetizer(someString) {
    let newString = someString.split('').sort().toString().split(',').join('').trim();
    return newString;
}