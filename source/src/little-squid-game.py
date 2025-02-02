import random
import time

SLEEP_DELAY = 5
MAX_ATTEMPTS = 3


def main():
    random.seed(time.localtime().tm_sec)
    game_counter = 0
    while True:

        print(f"Little くコ:彡 GAME #{game_counter + 1}")

        number = random.randint(0, 100000000)

        print(f"I've chosen a number. You have {MAX_ATTEMPTS} attempts to guess it.")

        for i in range(MAX_ATTEMPTS):
            while True:
                try:
                    guess = int(input(f"Attempt {i + 1}: Enter your guess: "))
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
                print(f"You have {MAX_ATTEMPTS - i} attempts left.")

        print(f"The number was {number}.")
        print("Better luck next time!")
        print(f"Little くコ:彡 will take a {SLEEP_DELAY} seconds nap...")
        time.sleep(SLEEP_DELAY)


if __name__ == "__main__":
    main()
