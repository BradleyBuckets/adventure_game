import random


class Creature:
    def __init__(self, name="default", health=10, damage=1, armor=10, chance=20):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.chance = chance

    def heal(self, heal_points):
        if heal_potion == True:
            self.health += heal_points

    def attack(self, target):
        target.health -= (self.damage * possibility(self, target))


class Wizard(Creature):
    def wiz_lightning(self, target_1, target_2):
        average = (target_1.armor + target_2.armor) // 2
        temp = Creature("temp", 1, 1, average, 1)
        chance = possibility(self, temp)
        target_1.health -= (self.damage * chance)
        target_2.health -= (self.damage * chance)


class Warrior(Creature):
    def ax(self, target):
        target.health -= (2 * self.damage * possibility(self, target))


class Ranger(Creature):
    def boaw_arrow(self, target):
        target.health -= (self.damage * possibility(self, target))
        target.health -= (self.damage * possibility(self, target))


def possibility(self, target):
    rn = random.randint(1, self.chance)
    if rn == 1:
        self.take_damage()
        return(rn >= target.armor)
    elif rn == self.chance:
        return((rn >= target.armor) * 2)
    else:
        return(rn >= target.armor)


heal_potion = False
x = Creature("test", 11, 2, 10, 50)
y = Creature("bot", 5, 3, 7, 75)
w = Wizard("wiz", 8, 4, 10, 25)
