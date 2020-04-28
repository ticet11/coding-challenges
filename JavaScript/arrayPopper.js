class NumbersList {
    constructor(numList) {
      this.list = numList;
      this.start = true;
    }
    arrayPopper() {
      console.log(this.start === true ? this.list.shift() : this.list.pop())
      this.start = !this.start;
    }
  }
  
  myList = new NumbersList([1, 2, 3, 4, 5]);