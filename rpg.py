import random
import time


class Creature:
    def __init__(self, stats=["name", 10, 2, 10, 20]):
        self.name = stats[0]
        self.health = stats[1]
        self.damage = stats[2]
        self.armor = stats[3]
        self.dice = stats[4]

    def heal(self, heal_points):
        if heal_potion == True:
            self.health += heal_points
            heal_potion = False

    def attack(self, target):
        time.sleep(2)
        print(f"{self.name} attacks {target.name}!")
        target.health -= (self.damage * does_hit(self,
                          target, dice_roll(self)))

    def take_damage(self):
        self.health -= self.damage


class Monster(Creature):
    def growl(self):
        print('grrrrhhhhh')


class Wizard(Creature):
    def lightning(self, *targets):
        chance = dice_roll(self)
        for target in targets:
            target.health -= (self.damage * does_hit(self, target, chance))

    def magic_missles(self, *targets):
        for target in targets:
            target.health -= (self.damage * does_hit(self,
                              target, dice_roll(self)))


class Warrior(Creature):
    def ax(self, target):
        target.health -= (2 * self.damage *
                          does_hit(self, target, dice_roll(self)))


class Ranger(Creature):
    def boaw_arrow(self, target):
        target.health -= (self.damage * does_hit(self,
                          target, dice_roll(self)))
        target.health -= (self.damage * does_hit(self,
                          target, dice_roll(self)))


def dice_roll(self):
    return random.randint(1, self.dice)


def does_hit(self, target, rn):
    if rn == 1:
        self.take_damage()
        return(rn >= target.armor)
    elif rn == self.dice:
        return((rn >= target.armor) * 2)
    else:
        return(rn >= target.armor)


def fight(hero, villain, fight=True):
    print(f"You are fighting against {villain.name}!")
    while fight:
        block = False
        print(f"{hero.name}, {hero.health}     {villain.name}, {villain.health}")
        move = input("What is your move? :")
        if move.lower() == "attack":
            hero.attack(villain)
        elif move.lower() == "block":
            block = True
        if villain.health <= 0:
            fight = False
            print(f"You successfully killed the {villain.name}!")
        # elif block:
        #     pass
        villain.attack(hero)
        if hero.health <= 0:
            fight = False
            print(f"You were killed by the {villain.name}!")


def random_monster():
    return random.choice(list(monsters.keys()))


def gladiator_mode(hero, villain):
    while True:
        ready = input("Ready? :")
        if ready.lower().startswith("y"):
            fight(hero, villain)
            break


heal_potion = False
monsters = {"test": ["test", 11, 2, 10, 20],
            "bot": ["bot", 5, 3, 7, 15],
            "blob": ["blob", 20, 1, 5, 20], }
allies = {"wiz": ["wiz", 8, 4, 10, 25]}

instructions = "right now, all you can do is attack in the game"


def menu():
    print("Welcome to the RPG game!")
    while True:
        menu = input("Menu: ").lower()
        if menu == "done":
            break
        if menu == "game":
            enemy = Monster(monsters[random_monster()])
            hero = Creature(allies["wiz"])
            name = input("What is your name? :")
            hero_name = input(f"Hello {name}, what is your hero's name? :")
            hero.name = hero_name
            gladiator_mode(hero, enemy)
        if menu == "help":
            print(instructions)


menu()
