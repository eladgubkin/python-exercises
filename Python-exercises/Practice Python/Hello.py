# TODO: Make heal function #done!

import random
name = input("What's your name?")

hp_player = 100
hp_bot = 100


def attack(hp):
    damage = random.randint(0, 30)
    return hp - damage


def heal(hitpoints):
    hp = random.randint(10, 30)
    return hitpoints + hp


while hp_player > 0 and hp_bot > 0:
    print(name, ":", hp_player)
    print("Barbarian : ", hp_bot)

    action = input("Your turn, What would you like to do? \n - Attack\n - Heal\n - Nothing\n")

    if action.lower() == "attack":
        hp_bot = attack(hp_bot)
        print("Congratulations!, You attacked a barbarian")

    elif action.lower() == "heal":
        hp_player = heal(hp_player)

        if hp_player > 100:
            hp_player = 100
        print("you healed yourself")

    elif action.lower() == "nothing":
        print("You did nothing")

    else:
        print("invalid action")

    bot_action = random.randint(0, 2)
    if bot_action == 0:
        hp_player = attack(hp_player)
        print("Barbarian attacked you")

    elif bot_action == 1:
        hp_bot = heal(hp_player)

        if hp_bot > 100:
            hp_bot = 100
        print("Barbarian healed himself")

    elif bot_action == 2:
        print("Barbarian did nothing")

if hp_player <= 0:
    print(name, "Died! :(")

if hp_bot <= 0:
    print("Barbarian Died! :(")

