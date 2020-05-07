function priceChanger(originalPrice, newCents) {
    const newPrice = newCents < 1 ? Math.floor(originalPrice) + newCents : Math.floor(originalPrice) + (newCents/100);
   return newPrice;
 }
 console.log(priceChanger(1.50, .23));