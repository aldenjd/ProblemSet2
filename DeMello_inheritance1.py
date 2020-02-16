# Name: Alden DeMello
# File Name: DeMello_inheritance.py
# Date: 2/13/2020
# Description:


class BaseCharacter: # Base Class Character
    def __init__(self, name, health):  # Initialize Function
        self.name = name  # Name of Character
        self.health = health  # Health of Character

    def printName(self):  # Print Name of Character
        print(self.name)


class NPC(BaseCharacter):  # Class Non-Playable Character
    def __init__(self, name, health):  # Initialize Function
        super(NPC, self).__init__(name, health)


class PC(BaseCharacter):  # Class Playable Character
    def __init__(self, name, health, weapon):  # Initialize Function
        super(PC, self).__init__(name, health)
        self.weapon = weapon


class Friendly(NPC):  # Class Friendly Character
    def __init__(self, name, health):  # Initialize Function
        super(Friendly, self).__init__(name, health)


class Enemy(NPC):  # Class Enemy Character
    def __init__(self, name, health, attackDamage):  # Initialize Function
        super(Enemy, self).__init__(name, health)
        self.attackDamage = 5


class Archer(PC):  # Class Archer
    def __init__(self, name, health, weapon):  # Initialize Function
        super(Archer, self).__init__(name, health, weapon)


class GreenLantern(PC):  # Class Green Lantern
    def __init__(self, name, health, weapon):  # Initialize Function
        super(GreenLantern, self).__init__(name, health, weapon)


class Butcher(PC):  # Class Butcher
    def __init__(self, name, health, weapon):  # Initialize Function
        super(Butcher, self).__init__(name, health, weapon)


class WeaponClass:  # Class Weapon
    def __init__(self, name):  # Initialize Function
        self.name = name
