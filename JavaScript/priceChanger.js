function priceChanger(originalPrice, newCents) {
    const flooredOriginal = Math.floor(originalPrice);
    const newPrice =
        newCents < 1 ? 
          flooredOriginal + newCents : 
          flooredOriginal + newCents / 100;
    return newPrice;
}
console.log(priceChanger(1.5, 23));
