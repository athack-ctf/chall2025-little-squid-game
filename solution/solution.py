import random

# TODO: Update generated_numbers with the numbers you get.
generated_numbers = [
    39475,
    21199
]

MIN_NUMBER = 0
MAX_NUMBER = 54321

possible_seeds = []
for seed in range(0, 1_000_000):

    is_possible_seed = True
    random.seed(seed)
    for number in generated_numbers:
        if number == random.randint(MIN_NUMBER, MAX_NUMBER):
            continue
        else:
            is_possible_seed = False
            break
    if is_possible_seed:
        possible_seeds.append(seed)

if len(possible_seeds) == 1:
    random.seed(possible_seeds.pop())
    for i in range(len(generated_numbers)):
        random.randint(MIN_NUMBER, MAX_NUMBER)

    print(f'Next number to guess is {random.randint(MIN_NUMBER, MAX_NUMBER)}')

else:
    print(f'Bad news: multiple ({len(possible_seeds)}) possible seeds were found :(')
    print(f"Seeds: f{possible_seeds}")
    print(f'You gotta add extra generated numbers.')
