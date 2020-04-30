function stringHyphenAlphabetizer(someString) {
    let newString = someString.split('-').sort().toString().split(',').join('-');
    return newString;
}