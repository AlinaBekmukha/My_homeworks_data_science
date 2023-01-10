"""Guess a number
"In this program the computer will generate the number between 1 - 100."
Then the computer will try to guess the number!"
"""

import numpy as np


def num_predict(num):

    count = 0
    low = 1
    high = 100
    guess = (low+high)//2

    while guess != num:
        count = count + 1
        guess = (low+high)//2
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1
    
    print("The computer guessed", guess, "and it was correct!")
    print("Total attempts = ", count)
    return count


def score_game(random_predict) -> int:

    count_ls = []
    np.random.seed(1) # to get the same random number
    random_array = np.random.randint(1, 101, size=(1000))  # generated list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average in: {score} guesses!")
    return score

# RUN
if __name__ == '__main__':
    score_game(num_predict)

