import random

weights_1 = {
    'win': 1,
    'break even': 5,
    'lose': 6
}


def weighted_lottery(weights):
    hat_container = []

    for outcome, odds in weights.items():
        for _ in range(odds):
            hat_container.append(outcome)
    random_outcome = random.choice(hat_container)
    print(f'You {random_outcome}!')

    play_again = (input('Play again? Yes/No:\n'))

    if play_again.lower().strip() == 'yes':
        weighted_lottery(weights)
    else:
        print('K, thx, bye.')


weighted_lottery(weights_1)
