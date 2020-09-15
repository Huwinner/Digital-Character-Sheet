import math



# Class for the Player and everything they can do
class Player:
    def __init__(self, same, health_max, health, quit):
        self.name = "Lentil"
        self.health = 1
        self.health_max = 1
        self.quit = True

    def stop(self):
        print("Discontinuing Adventure...")
        self.quit = False

    def take_damage(self):
        damage = int(input("Type Damage Taken: "))
        self.health = self.health - damage

    def heal_damage(self):
        heal = int(input("Type HP Healed: "))
        self.health = self.health + heal

    def status(self):
        print(self.name + " " + str(self.health) + " / " + str(self.health_max))




# Character Stats Class
class Character_Stat:
    def __init__(self, name, stat, roll):
        self.name = name # Name of stat
        self.stat = stat # Raw Stat
        self.roll = roll # Ability Rolls

    def Modifier(self): # Gives Stat Modifier (rounded down)
        mod = math.floor(((self.stat)-10)/2)
        return mod

# Spells Class
class Spells:
    def __init__(self, name, level, description, damage):
        self.name = name # Name of Spell
        self.level = level # Spell Level
        self.description = description # Spell Description
        self.damage = damage # Spell Damage

    def cast_spell(self): # Casts Spell - Prints the description of the spell and the damage done
        print(self.description)
        print("Damage : " + str(self.damage))


