sales = {
    'google' : 15,
    'facebook': 25,
    'twitter': 6,
    'offline': 12
}

def salesHistogram(salesData):
    for key, value in salesData.items():
        print(key[0], value*'$')

salesHistogram(sales)