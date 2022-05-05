import random


class Creature:
    def __init__(self, name="default", health=10, damage=1, chance=50):
        self.name = name
        self.health = health
        self.damage = damage
        self.chance = chance

    def heal(self, heal_points):
        if heal_potion == True:
            self.health += heal_points

    def attack(self, target):
        target.health -= (self.damage * possibility(self))


class Wizard(Creature):
    def wiz_lightning(self, target_1, target_2):
        chance = possibility(self)
        target_1.health -= (self.damage * chance)
        target_2.health -= (self.damage * chance)


class Warrior(Creature):
    def ax(self, target):
        target.health -= (2 * self.damage * possibility(self))


class Ranger(Creature):
    def boaw_arrow(self, target):
        target.health -= (self.damage * possibility(self))
        target.health -= (self.damage * possibility(self))


def possibility(self):
    rn = random.randint(1, 100)
    return(rn >= self.chance)


heal_potion = False
x = Creature("test", 11, 2, 50)
y = Creature("bot", 5, 3, 75)
w = Wizard("wiz", 8, 4, 25)

hero_name = input("please type your characters name : ")
hero_class = input("please type class; wizard, warrior, or ranger : ")
if hero_class.lower() == "warrior":
    hero = Warrior(hero_name, 10, 5)
elif hero_class.lower() == "wizard":
    hero = Wizard(hero_name, 8, 3, 25)
elif hero_class.lower() == "ranger":
    hero = Ranger(hero_name, 10, 4, 33)
else:
    pass

# test the features code

# print("bot health", y.health)
# print("test health", x.health)
# w.wiz_lightning(x, y)
# print("bot health after attack", y.health)
# print("test health after attack", x.health)
# print("bot health", y.health)
# x.attack(y)
# print("bot health after attack", y.health)
# print("test health", x.health)
# x.heal(heal_potion)
# print("test health after heal", x.health)
# print(hero.name)
# print(hero.health)
# print(hero.damage)
# print(hero.chance)
