import math



# Class for the Player and everything they can do
class Player:
    def __init__(self, name, AC, health_max, health, quit):
        self.name = "Lentil"
        self.AC = AC
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
        print(self.name + ", AC: " + str(self.AC) + " HP: " + str(self.health) + " / " + str(self.health_max))



# Character Stats Class
class Character_Stat:
    def __init__(self, name, stat, roll):
        self.name = name # Name of stat
        self.stat = stat # Raw Stat
        self.roll = roll # Ability Rolls

    def Modifier(self): # Gives Stat Modifier (rounded down)
        mod = math.floor(((self.stat)-10)/2)
        return mod

# Spell Classes
#~~~~~~~~~~~~~~

#Parent Spell Class
class Spells:
    def __init__(self, name, level, description):
        self.name = name # Name of Spell
        self.level = level # Spell Level
        self.description = description # Spell Description

#Spell Subclass with Attack Roll
class Spell_Attack(Spells):
    def __init__(self, name, level, description, roll, damage, damage_type):
        Spells.__init__(self, name, level, description)
        self.roll = roll
        self.damage = damage
        self.damage_type = damage_type
    
    def cast_spell(self):
        print(self.description)
        print("Roll: " + str(self.roll))
        print("Damage:" + str(self.damage) + " " + self.damage_type)
        print(" ")

#Spell Subclass with Attack DC
class Spell_Damage(Spells):
    def __init__(self, name, level, description, DC, DC_type, damage, damage_type):
        Spells.__init__(self, name, level, description)
        self.DC = DC
        self.DC_type = DC_type
        self.damage = damage
        self.damage_type = damage_type

    def cast_spell(self):
        print(self.description)
        print("DC: " + self.DC_type + " " + str(self.DC))
        print("Damage:" + str(self.damage) + " " + self.damage_type)
        print(" ")

#Spell Subclass with non damaging DC
class Spell_Effect(Spells):
    def __init__(self, name, level, description, DC, DC_type):
        Spells.__init__(self, name, level, description)
        self.DC = DC
        self.DC_type = DC_type
    
    def cast_spell(self):
        print(self.description)
        print("DC: " + self.DC_type + " " + str(self.DC))
        print(" ")

#Spell Subclass with non damaging roll (or no roll)
class Spell_Utility(Spells):
    def __init__(self, name, level, description, roll):
        Spells.__init__(self, name, level, description)
        self.roll = roll

    def cast_spell(self):
        print(self.description + " " + str(self.roll))
        print(" ")



