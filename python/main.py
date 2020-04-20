def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('Correct!')
      return False
    else:
      print(f'No go, buddy. {guess} is wrong. Try again.')

guessing_game()