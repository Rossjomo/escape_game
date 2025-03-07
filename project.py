import random
import time
import re
from pyfiglet import Figlet
from tabulate import tabulate


CHARACTERS = {
            "brave": {"attack": 1, "defence": 3, "health": 9},
            "strong": {"attack": 2, "defence": 2, "health": 10},
            "fast": {"attack": 3, "defence": 1, "health": 8}
            }

opponents = [["an empty hallway", 0, 0],
            ["a Troll", 10, 6],
            ["an empty hallway", 0, 0],
            ["an Ogre", 12, 4],
            ["an empty hallway", 0, 0],
            ["a Gremlin", 8, 8]]

bld = Figlet(font='sblood')
goth = Figlet(font='gothic')


def main():
    intro()
    name = get_name()
    attack, defence, warrior_health = choose_char(name)
    still_alive = True

    turns = 3
    while turns > 0:
        time.sleep(1)
        door, monster = choose_door()
        monster, monster_health, monster_attack = monster
        print("")
        time.sleep(1)
        print(f"Behind the {door} door is {monster}")
        time.sleep(1)
        if monster == "an empty hallway":
            time.sleep(1)
            print(tabulate([["You pass quickly and safely through the passage and then..."]]))
        else:
            warrior_health, still_alive = fight(attack, defence, warrior_health, still_alive, monster[2:], monster_health, monster_attack)
        if still_alive is False:
            print(bld.renderText("Game Over!"))
            time.sleep(1)
            print(bld.renderText("You died"))
            time.sleep(1)
            print(bld.renderText("Better luck next time..."))
            break
        turns -= 1
    if still_alive == True:
        print("")
        print(goth.renderText("Success!"))
        time.sleep(1)
        print("")
        print(goth.renderText("You escaped the dungeon!"))
        time.sleep(1)
        print("")
        print(goth.renderText("This time.. "))


def intro():
    print(goth.renderText("Welcome Warrior"))
    time.sleep(1)
    table1 = [["You are in a dungeon\nYou must choose your own way out."]]
    print(tabulate(table1))
    time.sleep(1)
    table2 = [["You must fight and use your cunning,\nif you are to escape."]]
    print(tabulate(table2))
    time.sleep(1)


def validate_name(name):
    if name.isalpha():
        return name
    else:
        raise ValueError

def get_name():
    while True:
        try:
            name = input("What is your name? ").capitalize().strip()
            return validate_name(name)
        except ValueError:
            print("\nPlease warrior, tell me...")


def valid_char(char):
    if char in CHARACTERS:
        return char
    else:
        raise ValueError


def get_char_stats(char):
    if char in CHARACTERS:
        return CHARACTERS[char]["attack"], CHARACTERS[char]["defence"], CHARACTERS[char]["health"]
    else:
        raise ValueError


def choose_char(name):
    time.sleep(1)
    print("")
    print(f"Tell me {name}, what kind of warrior are you?")
    time.sleep(1)
    while True:
        char = input("Are you: Brave, Strong or Fast? (b/s/f) ").lower().strip()
        char = "brave" if char == "b" else char
        char = "strong" if char == "s" else char
        char = "fast" if char == "f" else char
        try:
            valid_char(char)
            attack, defence, health = get_char_stats(char)
            break
        except ValueError:
            print("Please choose wisely!")
    print(goth.renderText(f"Welcome {name},"))
    time.sleep(1)
    print(goth.renderText(f"the {char} warrior"))
    print("Your character stats are:")
    time.sleep(1)
    table = [["Attack", attack],["Defence",defence],
          ["Health",health]]
    print(tabulate(table))
    time.sleep(1)
    print(f"Good luck {name}")
    print("")
    time.sleep(1)
    print(("you'll need it..."))
    print("")
    return attack, defence, health


def valid_door(door):
    pattern = r"^(left|right|l|r)$"
    matches = re.search(pattern, door)
    if matches:
        return "left" if str(matches.group(1)) == "l" else "right" if str(matches.group(1)) == "r" else door
    return None


def choose_door():
    left_door = choose_opponent()
    right_door = choose_opponent()
    print("You are faced with two doors, which door will you choose?")
    while True:
        door_input = input("Left or Right? (l/r) ").lower().strip()
        door = valid_door(door_input)
        if door:
            break
        else:
            print("There is no way back, you must choose left or right!")
    if door == "left":
        return door, left_door
    else:
        return door, right_door


def choose_opponent():
    global opponents
    rand_index = random.randint(0, len(opponents)-1)
    monster = opponents.pop(rand_index)
    return monster


def fight(attack, defence, warrior_health, still_alive, monster, monster_health, monster_attack):
    monster_alive = True
    while monster_alive is True:
        print(tabulate([["You attack\nRoll the dice to decide your attack..."]]))
        hit = ready_to_fight()
        print("")
        print(f"You rolled a {hit}")
        monster_health -= (hit + attack)
        if monster_health < 1:
            print(goth.renderText(f"The {monster} is defeated!"))
            print("")
            time.sleep(1)
            print(f"The {monster} is down and you can continue")
            time.sleep(1)
            print("You walk down the corridor and then...")
            print("")
            monster_alive = False
            break
        time.sleep(1)
        print(tabulate([[f"The {monster}'s health is now: {monster_health}\nThe {monster} takes a swing at you..."]]))
        monster_hit = monster_attack_strength(monster_attack)
        print("")
        time.sleep(1)
        print(f"The monster strikes with a {monster_hit}")
        damage_taken = max(monster_hit - defence, 0)
        warrior_health -= damage_taken
        if warrior_health < 1:
            still_alive = False
            break
        time.sleep(1)
        print(f"Your health is now: {warrior_health}")
        time.sleep(1)
    return warrior_health, still_alive


def roll_dice(num=7):
    return random.choice(range(1, num))


def ready_to_fight():
    time.sleep(1)
    while True:
        decide = input("Are you ready to roll the dice? (y/n) ").lower()
        if decide in ["y", "yes"]:
            return roll_dice()
        else:
            print("Prepare yourself, it is time to battle!")


def monster_attack_strength(num):
    time.sleep(1)
    while True:
        decide = input("Are you ready to take a hit? (y/n) ").lower()
        if decide in ["y", "yes"]:
            return roll_dice(num)
        else:
            print("Are you too scared?")


if __name__ == "__main__":
    main()
