const menus = {
  omletteMenu: {
    "ham and cheese" : 3,
    "diablo"         : 4,
    "Denver"         : 3,
    "JS special"     : 5
  },

  lunchMenu    : {
    "grilled cheese" : 1,
    "big burger"     : 5,
    "little burger"  : 3,
    "pulled porkwich": 5
  },

  dinnerMenu   : {
    "grilled cheese" : 2,
    "big burger"     : 6,
    "little burger"  : 4,
    "pulled porkwich": 6
  },

  sideMenu     : { 
    "french fries"   : 1, 
    "salad"          : 1, 
    "bread"          : 1, 
    "mashed potatoes": 1
  }
}

const waiterBotSpeech = {
  "ham and cheese"    : 'Very classic, very cool.',
  "diablo"            : 'When they say spicy, they mean spicy.',
  "denver"            : 'They say that is the place to get your drugs.',
  'js special'        : 'It is a program with no real food.',
  'grilled cheese'    : 'Very classic, very cool.',
  'big burger'        : 'This burger will make you full.',
  'little burger'     : 'This burger will make a baby full.',
  'pulled porkwich'   : 'We will pull the pork just for you.',
  'french fries'      : 'Oui.',
  'salad'             : 'Some rabbit food for you',
  'bread'             : 'We only have pumpernikle and you are okay with that.',
  'mashed potatoes'   : 'Oh, actually, we can not mash those, it will be whole.'
}

const whichMenu = () => {
  let menuChoice = prompt('Which menu are we looking at?\nbreakfast,\nlunch,\nor dinner?', 'breakfast');
  if (menuChoice === 'breakfast') {
    getMenuItems(menus.omletteMenu);
  } else if (menuChoice === 'lunch') {
    getMenuItems (menus.lunchMenu);
  } else if (menuChoice === 'dinner') {
    getMenuItems (menus.dinnerMenu);
  } else {
    alert("That's not a choice, try again.");
    whichMenu();
  }
}

const getMenuItems = (menu) => {
  let menuItems = Object.keys(menu);
  if (menu === menus.sideMenu) {
    getSides(menuItems);
  } else {
    getEntree(menuItems);
  }
};

const getEntree = (menuItems) => {
  menuItemsString = "";
  for (let i of menuItems) {
    menuItemsString += i + "\n";
    }
  const entree = prompt(
    `These are our specials, today:\n\n${menuItemsString}\nWhat can I get for you?`,
    "grilled cheese"
  );
  entreeResponse(entree.toLowerCase());
};

const entreeResponse = (customerSpeech) => {
  alert(`Oh, ${customerSpeech}? ${waiterBotSpeech[customerSpeech]}`);
  getMenuItems (menus.sideMenu)
};

const getSides = (menuItems) => {
menuItemsString = "";
for (let i of menuItems) {
  menuItemsString += i + "\n";
}
const side1 = prompt(`And your two sides? I do recommend the french fries.\n\n${menuItemsString}\nFirst Side:\n`, 'french fries');
sideResponse(side1.toLowerCase());
const side2 = prompt(`And the other?\n\n${menuItemsString}\nSecond Side:\n`, 'mashed potatoes')
sideResponse(side2.toLowerCase());
}

const sideResponse = (customerSpeech) => {
alert(`Okay, ${customerSpeech}. ${waiterBotSpeech[customerSpeech]}`);
};

whichMenu();