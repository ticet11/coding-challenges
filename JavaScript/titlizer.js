const shortString = "Hi, there.";
const longString = "Wow, the quick brown fox jumps over the lazy dog.";

function titlizer(someString) {
  const splitStringArray = someString.split(" ");
  let newArray = [];
  splitStringArray.forEach((word) => {
    newArray.push(word[0].toUpperCase() + word.slice(1));
  });
  return newArray.join(' ');
}

console.log(titlizer(longString));