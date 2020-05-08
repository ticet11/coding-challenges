const sales = {
    google: 10,
    facebook: 20,
    twitter: 6,
    offline: 15
  };
  
  const salesHistogram = function (salesData) {
    const platformsArray = Object.keys(salesData);
    let multiLineString = `\n`;
    for (let i = 0; i < platformsArray.length; i++) {
      let dollarSymbols = '$'.repeat(salesData[platformsArray[i]]);
      multiLineString += `${platformsArray[i].charAt(0)} ${dollarSymbols}\n`;
    }
    return multiLineString;
  };
  
  console.log(salesHistogram(sales));
