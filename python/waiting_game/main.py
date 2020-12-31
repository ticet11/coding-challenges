import time
import keyboard

"""
* Pick a number that the user will try to stop at.
You can either pick this number for them or you can ask the user to input a target time.

* Once they press Enter to begin,
the timer will start and the user will have to "guess" when that amount of time has passed and press Enter again.

* Print out the elapsed time and tell the user if they won or by how much they were over or under
"""

start_has_run = False
end_has_run = False


def waiting_game():
    print('Press "s" to begin the timer.')

    while start_has_run == False:
        keyboard.add_hotkey('s', lambda: print(start_timer()), )

    print('press "s" to end')
    while end_has_run == False:
        keyboard.add_hotkey('e', lambda: print(end_timer()))


def start_timer():
    start_time = time.time()
    start_has_run = True
    return start_time, start_has_run


def end_timer():
    stop_time = time.time()
    end_has_run = True
    return stop_time


print(waiting_game())

# def waiting_game(target_time):
#     input('Press "Enter" to start.')
#     start_time = time.time()s

#     input('Press "Enter" to stop.')
#     end_time = time.time()

#     time_lapsed = end_time - start_time
#     difference = target_time - time_lapsed

#     print(f'{round(time_lapsed, 3)} seconds have elapsed.')
#     print(f'You were {round(difference, 3)} seconds off.')
#     if difference < 1:
#         print('You win!')
#     else: 
#         print('You lose!')


# waiting_game(3)


