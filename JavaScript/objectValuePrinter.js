function objectValuePrinter(someObject) {
    for (var key in someObject) {
      console.log(someObject[key]);
    }
  }
  
  objectValuePrinter({ hungry: "hippo", angry: "beavers" });
  