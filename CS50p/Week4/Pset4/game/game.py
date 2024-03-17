import random
import sys

start_lvl = 1

def main():
    lvl = get_lvl()
    n = random.randint(start_lvl, lvl)
    get_guess(n)


def get_lvl():
    while True:
        lvl = input("Level: ").strip()
        if lvl.isdigit():
            lvl = int(lvl)
            if lvl > 0:
                return lvl


def get_guess(n):
    while True:
        guess = input("Guess: ").strip()
        if guess.isdigit():
            guess = int(guess)
            if guess > 0:
                verify_guess(guess, n)
                break


def verify_guess(guess, n):
    if guess < n:
        print("Too small!")
        get_guess(n)
    elif guess > n:
        print("Too large!")
        get_guess(n)
    else:
        print("Just right!")
        sys.exit()

main()
