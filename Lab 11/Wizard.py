# Made by Jasque Saydyk and Miguel Quinones
# Lab 11 - RPG
# Section 2, April 19, 2017
# Description - Represents a Wizard class
# Encapsulates a Wizard class, inheriting from Adventurer.
from Adventurer import *
from Attack import *


class Wizard(Adventurer):
    """
    Wizards have 20 HP, defense of 4, and magic defense of 10, all
    stored as class variables using the same naming conventions as Fighter.
    """
    _HP = 20
    _DEF = 4
    _MAG_DEF = 10

    def __init__(self, name, initiative):
        """
        Creates a Wizard object. This is done in exactly the same way as
        it was done in the Fighter class.

        Calls the superclass init method with name, HP,
        DEF, MAG DEF, and initiative.

        Also adds a variable spell that references an instance of the
        Attack class. For our simple game, this lets us create fixed
        attacks such as Attack(”Fireball”, 3, 6, ”magic”).
        """
        super().__init__(name, Wizard._HP, Wizard._DEF, Wizard._MAG_DEF,
                         initiative)
        self._melee = Attack("Fireball", 3, 6, "magic")

    def cast(self):
        """
        Calculates and returns information about a spell from this object.

        Returns a tuple, consisting of a damage value and a damage type. The
        values are obtained by calling get damage() and get attack type() on
        spell.

        Also prints out information about the attack, much like in Fighter’s
        attack method.
        """
        damage = self._melee.get_damage()
        attack_type = self._melee.get_type()

        print(str(self.get_name()) + " attacks with " +
              str(self._melee.get_name()) + " for " + str(damage) + " " +
              str(attack_type) + " damage.")

        return (damage, attack_type)

    def __str__(self):
        """
        Returns a string representation of this object, much like
        in Fighter’s str method.
        """
        s = (str(self.get_name()) + " with " + str(self._HP) +
             " hit points and a " + str(self._melee.get_name()) +
             " attack (" + str(self._melee.get_number()) + "d" +
             str(self._melee.get_sides()) + ")")
        return s
