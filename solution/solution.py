"""
For an initial incorrect guess of 81790898, we try all possible 1_000_000 seeds, and see if any of them havea a randint result of 3105130.

If only one of them does, we know the seed. And now we just have to do an *additional* randint with this seed, and that's the answer (the next 'random' number).
If there are multiple possible seeds, we should go through all of them, and do 2 randint calls the second time.
If there are again multiple possible seeds, we should do so again, etc.
Until we only have one possible seed, at which point we can print out what the next number is :party:
"""
import random


# update this each time
number_wrong_guesses = 1
# update this each time
latest_wrong_result = 81790898
possible_seeds = []

# in try N (if there are multiple possible seeds in try N-1), replace range(1_000_000) with possible_seeds.copy()
for seed_guess in range(1_000_000):
    random.seed(seed_guess) 
    for i in range(number_wrong_guesses):
        result = random.randint(0, 100_000_000)
    # change this to the latest wrong result
    if result == latest_wrong_result:
        possible_seeds.append(seed_guess)
print(possible_seeds)
if len(possible_seeds) == 1:
    random.seed(possible_seeds[0])
    for i in range(number_wrong_guesses):
        random.randint(0, 100_000_000)
    print(f'Next number with this seed is {random.randint(0, 100_000_000)}')