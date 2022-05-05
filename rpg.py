import random


class Creature:
    def __init__(self, name="default", health=10, damage=1, armor=10, dice=20):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.dice = dice

    def heal(self, heal_points):
        if heal_potion == True:
            self.health += heal_points
            heal_potion = False

    def attack(self, target):
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


heal_potion = False
monsters = {"test": ["test", 11, 2, 10, 20],
            "bot": ["bot", 5, 3, 7, 75],
            "blob": ["blob", 20, 1, 5, 20], }
allies = {"wiz": ["wiz", 8, 4, 10, 25]}

x = Creature(monsters["test"])
y = Creature(monsters["bot"])
z = Creature(monsters["blob"])
w = Creature(allies["wiz"])


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


fight(x, z)
