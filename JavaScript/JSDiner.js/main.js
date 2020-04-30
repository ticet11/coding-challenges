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
      "fries"          : 1, 
      "salad"          : 1, 
      "bread"          : 1, 
      "mashed potatoes": 1
    }
  }
  
  const waiterBotSpeech = {
    "ham and cheese"    : 'very classic, very cool.',
    "diablo"            : 'when they say spicy, they mean spicy.',
    "Denver"            : 'they say that is the place to get your drugs.',
    'JS Special'        : 'it is a program with no real food.',
    'grilled cheese'    : 'very classic, very cool.',
    'big burger'        : 'this burger will make you full.',
    'little burger'     : 'this burger will make a baby full.',
    'pulled porkwich'   : 'we will pull the pork just for you.',
    'fries'             : 'oui.',
    'salad'             : 'you think you are better than me?',
    'bread'             : 'we only have pumpernikle and you are okay with that.',
    'mashed potatoes'   : 'oh, actually, we can not mash those, it will be whole.'
  }
  
  const whichMenu = () => {
    let menuChoice = prompt('Which menu are we looking at?\nbreakfast,\nlunch,\ndinner', 'breakfast');
    if (menuChoice = 'breakfast') {
      getMenuItems(menus.omletteMenu);
    } else if (menuChoice = 'lunch') {
      getMenuItems (menus.lunchMenu);
    } else if (menuChoice = 'dinner') {
      getMenuItems (menus.dinnerMenu);
    } else {
      alert("That's not a choice, try again.");
      whichMenu();
    }
  }
  const getMenuItems = (menu) => (menuItems = Object.keys(menu));
  const getEntree = (menuItems) => {
    menuItemsString = "";
    for (let i of menuItems) {
      menuItemsString += i + "\n";
    }
    const entree = prompt(
      `These are our specials today:\n\n${menuItemsString}\nWhat can I get for you?`,
      "grilled cheese"
    );
    entreeResponse(entree);
  };
  
  const entreeResponse = (customerSpeech) => {
    alert(`${customerSpeech}? ${waiterBotSpeech[customerSpeech]}`);
  };
  
  whichMenu();
  getEntree(menuItems);
  
  