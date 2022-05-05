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

    def attack(self, target):
        target.health -= (self.damage * does_hit(self,
                          target, dice_roll(self)))

    def take_damage(self):
        self.health -= self.damage


class Wizard(Creature):
    def lightning(self, *targets):
        chance = dice_roll(self)
        for target in targets:
            target.health -= (self.damage * does_hit(self, target, chance))


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
x = Creature("test", 11, 2, 10, 50)
y = Creature("bot", 5, 3, 7, 75)
w = Wizard("wiz", 8, 4, 10, 25)
