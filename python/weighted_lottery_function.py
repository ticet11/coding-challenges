import random

weights = {
    'win' : 1,
    'break even' : 5,
    'lose' : 6
}

def weighted_lottery(weights):
    hat_container = []
    key_container = list(weights)
    win_count = weights['win']
    draw_count = weights['break even']
    lose_count = weights['lose']

    for win in range(win_count):
        hat_container.append(key_container[0])

    for draw in range(draw_count):
        hat_container.append(key_container[1])

    for lose in range(lose_count):
        hat_container.append(key_container[2])

    outcome = random.choice(hat_container)
    print(f'You {outcome}')

weighted_lottery(weights)