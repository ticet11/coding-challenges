/* Write a JavaScript function to capitalize the first letter of a string or argument.
ex: capitalizeString(“hi there”) // returns “Hi there” */

function uppercaseFirstLetter(stringToUp) {
    console.log(stringToUp.charAt(0).toUpperCase() + stringToUp.slice(1));
  }