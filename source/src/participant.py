import random
import time

def main():
    random.seed(time.localtime().tm_sec)

    print("Welcome to the Number Guessing Game!")
    while True:

        number = random.randint(0, 100000000) 

        attempts = 3
        print(f"I've chosen a number. You have {attempts} attempts to guess it.")

        for i in range(attempts):
            while True:  
                try:
                    guess = int(input(f"Attempt {i + 1}: Enter your guess: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
  
            if  guess == number:
                print("Congratulations! You guessed the number!")
                with open('flag.txt', "r") as f:
                    flag = f.read()
                    print(flag)

                return
            else:
                print("Incorrect guess.")
                
        print(f"You ran out of attempts. The number was {number}.")
        print("Better luck next time!")
        print("You've attempted 3 times already. Sleeping for 5 seconds...")
        time.sleep(5)

if __name__ == "__main__":
    main()
