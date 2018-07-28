import random

name = input("-Hello I'm Adam what's your name? \n")
question = input('-Hey ' + name + ' Do you want to play with me Rock-Paper-Scissors [Yes/No]\n')

if question.lower() == 'no':
    print('Oh.. okay... :(')

elif question.lower() == 'yes':
    print("-----Here are the rules-----\n\n-Rock beats scissors\n-Scissors beats Paper\n-Paper beats rock")
    name_score = 0
    adam_score = 0

    while name_score or adam_score < 3:
        action = input("\n\nWhat would you like to pick?\n\n[Rock]\n[Paper]\n[Scissors]\n")
        random_number = random.randint(1, 12)

        if action.lower() == 'rock':
            print(name + ' picked a rock!')
            if random_number > 10:
                print('Adam picked a rock! \nIts a tie!')
            elif random_number > 6:
                print('Adam picked paper! \nAdam owned you!')
                adam_score = adam_score + 1
                print('Score of ' + name + ' :', name_score)
                print('Score of Adam :', adam_score)
                if adam_score == 3:
                    print('Congratulations to adam, He won the game!')
                    break
            elif random_number <= 6:
                print('Adam picked scissors! \nYou owned Adam!')
                name_score = name_score + 1
                print('Score of ' + name + ' :', name_score)
                print('Score of Adam :', adam_score)
                if name_score == 3:
                    print('Congratulations ' + name + ' you won the game!')
                    break

        elif action.lower() == 'paper':
            print(name + ' picked paper!')
            if random_number >= 6:
                print('Adam picked a rock! \nYou owned Adam!')
                name_score = name_score + 1
                print('Score of ' + name + ' :', name_score)
                print('Score of Adam :', adam_score)
                if name_score == 3:
                    print('Congratulations ' + name + ' you won the game!')
                    break
            elif random_number > 10:
                print('Adam picked paper! \nIts a tie!')
            elif random_number < 6:
                print('Adam picked scissors! \nAdam owned you!')
                adam_score = adam_score + 1
                print('Score of ' + name + ' :', name_score)
                print('Score of Adam :', adam_score)
                if adam_score == 3:
                    print('Congratulations to adam, He won the game!')
                    break

        elif action.lower() == 'scissors':
            print(name + ' picked scissors!')
            if random_number > 6:
                print('Adam picked a rock! \nAdam owned you!')
                adam_score = adam_score + 1
                print('Score of ' + name + ' :', name_score)
                print('Score of Adam :', adam_score)
                if adam_score == 3:
                    print('Congratulations to adam, He won the game!')
                    break
            elif random_number <= 6:
                print('Adam picked paper! \nYou owned Adam!')
                name_score = name_score + 1
                print('Score of ' + name + ' :', name_score)
                print('Score of Adam :', adam_score)
                if name_score == 3:
                    print('Congratulations ' + name + ' you won the game!')
                    break
            elif random_number > 10:
                print('Adam picked scissors! \nIts a tie!')

        else:
            print ('wrong syntax')
            break
else:
    print('Invalid syntax')