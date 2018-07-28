import random

random_number = random.randint(1, 9)
tries = 1
print(random_number)
guess = int(input('-Random number has been chosen between 1 and 9.\n-Have a guess which number is it! :)\n-'))

if guess == random_number:
    print('-WOW! You guessed the number exactly right! Nice Job :)')

while guess < random_number or guess > random_number:
    tries += 1
    if guess > random_number:
        int(input('Too high, Guess lower'))

    elif guess < random_number:
        int(input('Too low, Guess higher'))

    elif guess == random_number:
        print('Congratulations you nailed it!')
        break
