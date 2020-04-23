class Item:
    """An item we sell at our store."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

def cents_changer(Item, new_cents):
    old_price = Item.price
    if new_cents > .99: 
        Item.price = int(Item.price) + new_cents/100
    else:
        Item.price = int(Item.price) + new_cents
        
    print (f'You have changed the price of {Item.name}s from ${old_price} to ${Item.price}!')

item1 = Item('book', 5.51)
item2 = Item('pencil', 1.22)

cents_changer(item1, 99)