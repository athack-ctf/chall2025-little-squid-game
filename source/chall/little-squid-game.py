#!/usr/bin/python3

import time
from datetime import datetime
import random

SLEEP_DELAY = 5
MAX_ATTEMPTS = 3


def main():
    random.seed(datetime.now().microsecond)
    game_counter = 0
    while True:
        game_counter += 1
        print(f"LITTLE くコ:彡 GAME #{game_counter}")

        number = random.randint(0, 654321)

        print(f"I've chosen a number. You have {MAX_ATTEMPTS} attempts to guess it.")

        for i in range(MAX_ATTEMPTS):
            while True:
                try:
                    print(f"Attempt {i + 1}: Enter your guess: ", end="")
                    guess = int(input())
                    break
                except ValueError:
                    print("Invalid input. Enter an integer!")

            if guess == number:
                print("You guessed right!")
                with open('flag.txt', "r") as f:
                    flag = f.read()
                    print(flag)
                return
            else:
                print("Your guess was incorrect!")
                print(f"You have {MAX_ATTEMPTS - (i+1)} attempts left.")

        print(f"The number was {number}.")
        print("Better luck next time!")
        print(f"Little くコ:彡 will take a {SLEEP_DELAY} seconds nap...")
        time.sleep(SLEEP_DELAY)
  

if __name__ == "__main__":
    main()
