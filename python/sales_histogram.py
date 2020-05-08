sales = {
    'google' : 15,
    'facebook': 25,
    'twitter': 6,
    'offline': 12
}

def salesHistogram(salesData):
    multiLineString = '\n'
    for key, value in salesData.items():
        multiLineString += (key[0] + value*'$' + '\n')
    return multiLineString

print(salesHistogram(sales))