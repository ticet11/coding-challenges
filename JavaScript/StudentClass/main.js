class Student {
    constructor({ name, email, favProgLanguage = "Plankalkül", age }) {
      this.name = name;
      this.email = email;
      this.favProgLanguage = favProgLanguage;
      this.age = age;
    }
  
    renderContactInfo() {
      console.log(`You can reach ${this.name} at ${this.email}. If you care, their favorite progrmming language is ${this.favProgLanguage}.`);
    }
  
    renderFavProgLanguage() {
      console.log(
        `${this.name}'s favorite programming language is ${this.favProgLanguage}.`
      );
    }
  
    static irrelivant() {
      console.log("This has nothing to do with the Student class.");
    }
  
    static canPython(student) {
      if (student.favProgLanguage === 'python' && student.age >= 18) {
        console.log('This student can TA in python class.');
      } else if (student.age < 18) {
        console.log('This is a child!')
      } else if (student.favProgLanguage !== 'python') {
        console.log('How can you teach a language that you do not love?')
      }
      
    }
  }
  
  const brian = new Student({ name: 'Brian', email: 'brian@gmail.com', favProgLanguage: 'python', age: 6});
  
  brian.renderContactInfo();
  brian.renderFavProgLanguage();
  Student.irrelivant();
  Student.canPython(brian);
  