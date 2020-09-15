
# Digital Character Sheet Challenge
# Ground Level - Level 0
# Alec Huynh

#Challenge Deadline: January 1st, 2021. 


# Goal:
# The goal of the Level 0 Digital Character Sheet program is to lay the groundwork for the basic math and 
# organization of code for future levels. This will run in the command prompt. In the future this may be 
# run in the terminal. However, the terminal program may also be in level 1. 

# List of edits:
# 0.1 9/10/2020
# 0.2 9/13/2020
"""
Log 0.2
Added basic game loop and command options for groundlevel text based system. Revamped character class to accomodate this. 
    Will need to add AC attribute to Character class
Began adding spell class and spell dictionary. 
    Will need to create spell list command options

Features to keep in mind
 - Inventory
    + Consumables
 - Character Features
 - Class Features
 - Spell Slots
 - EXP/Level Up
 - HP Bar
 - Using a .txt file which the program saves to and reads from for data (allows for easy editing of character)


Going forward
 - AC attribute to Character Class
 - Broaden spell list to include level 1 and level 2 spells
 - Add spell list command functionality to game loop
 - Begin investigating low level game options
    + ex. being able to select listed text options with a cursor controlled by arrow keys


"""

# Import Libraries
import stats # Local library must be in same directory. 
import math
from random import randint


# Start Up
# =========================

def main():
    pass

if __name__ == '__main__':
    main()



# CHARACTER 9/13/20
# ==================================
# Note: 
# Edit here to make changes to the character for now
# For saves and ability checks 1 = proficiency


Name = "Lentil the Grand Wizard"
HP_max = 50
HP_current = HP_max


#Proficiency Modifier
Prof_Mod = 2

STR = 9
save_STR = 0
Athletics = 0

DEX = 12
save_DEX = 0
Acrobatics = 0 
Sleight_Hand = 0
Stealth = 0

CON = 9
save_CON = 0

INT = 20
save_INT = 1
Arcana = 1
History = 1
Investigation = 1 
Nature = 0
Religion = 1

WIS = 12
save_WIS = 1
Animal_Handling = 0
Insight = 0
Medicine = 0
Perception = 0
Survival = 0

CHA = 11
save_CHA = 0
Deception = 0
Intimidation = 0
Performance = 0
Persuasion = 0

stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
char_stats = [STR, DEX, CON, INT, WIS, CHA]

#print(char_stats)

# END CHARACTER
# =================================


# SPELL LIST
# =================================
# Note: 
# Edit Spell Lists here from now on 
# Consider extracting method and setting this as a new function, that way it only loads 
# the spell book when it's needed and not holding all the memory constantly


Spells = {



# Cantrips
# ~~~~~~~~~~~~~~~~~~~~~~~~

"Firebolt" : stats.Spells("Firebolt", \
                        0,\
                       "You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn't being worn or carried.", \
                       randint(1,10)) #1d10
                        
                       

# 1
# ~~~~~~~~~~~~~~~~~~~~~~~~



# 2
# ~~~~~~~~~~~~~~~~~~~~~~~~



# 3
# ~~~~~~~~~~~~~~~~~~~~~~~~



# 4
# ~~~~~~~~~~~~~~~~~~~~~~~~



# 5
# ~~~~~~~~~~~~~~~~~~~~~~~~



# 6
# ~~~~~~~~~~~~~~~~~~~~~~~~



# 7
# ~~~~~~~~~~~~~~~~~~~~~~~~



# 8
# ~~~~~~~~~~~~~~~~~~~~~~~~



# 9
# ~~~~~~~~~~~~~~~~~~~~~~~~



}
# END SPELL LIST
# =================================

# Calculating Stats!
# ==================================
# Note: 
# This section is the engine behind how stats are calculated
# and organized into classes.

# Creating the Stat List
# ----------------------------------
STAT_LIST = []

# Assigning stat names to objects
for x in stat_names:
    STAT_LIST.append ( stats.Character_Stat(x, 0, 0) )

# Assigning stat values to objects
for obj, x in zip(STAT_LIST,char_stats):
    obj.stat = x
  


# Setting Saves and Ability Checks

# Str
STAT_LIST[0].roll = {"Save" : save_STR,\
                     "Athletics" : Athletics}
# Dex
STAT_LIST[1].roll = {"Save" : save_DEX,\
                     "Acrobatics" : Acrobatics,\
                     "Sleight of Hand" : Sleight_Hand,\
                     "Stealth" : Stealth}
# Con
STAT_LIST[2].roll = {"Save" : save_CON}

# Int
STAT_LIST[3].roll = {"Save" : save_INT,\
                     "Arcana" : Arcana,\
                     "History" : History,\
                     "Investigation" : Investigation,\
                     "Nature" : Nature,\
                     "Religion" : Religion}
# Wis
STAT_LIST[4].roll = {"Save" : save_WIS,\
                     "Animal Handling" : Animal_Handling,\
                     "Insight" : Insight,\
                     "Medicine" : Medicine,\
                     "Perception" : Perception,\
                     "Survival" : Survival}
# Cha
STAT_LIST[5].roll = {"Save" : save_CHA,\
                     "Deception" : Deception,\
                     "Intimidation" : Intimidation,\
                     "Performance" : Performance,\
                     "Persuasion" : Persuasion}

# Applies proficiency modifiers
i = 0
while i < len(STAT_LIST):
    for obj in STAT_LIST[i].roll:
        STAT_LIST[i].roll[obj] = STAT_LIST[i].roll[obj]*Prof_Mod + STAT_LIST[i].Modifier()
    i += 1


# Print to make sure everything is gucci
#for obj in STAT_LIST:
#    print(obj.name, end =" ") 
#    print(obj.stat, end =" ")
#    print(obj.roll)

#print(STAT_LIST[0].roll["Athletics"])



# Commands for Text Based Character Sheet
Commands = {
    'quit' : stats.Player.stop,
    'damage' : stats.Player.take_damage,
    'heal' : stats.Player.heal_damage,
    #'status' : stats.Player.status
    }


# Game Loop
# ======================

# Instantiating Player as object
p = stats.Player("Lentil", 50, 50, True)
p.name = Name
p.health_max = HP_max
p.health = HP_current

#Spells["Firebolt"].cast_spell()

while(p.quit):
    p.status() # Always describe player status
    line = input("> ")
    args = line.split() # Extracts each individual word (or string of text separated by space)
    if len(args) > 0: # If you entered anything...
        commandFound = False 
        for c in Commands.keys(): # Scroll through every Key
            if args[0] == c[: len(args[0])]: # If first argument is the same as the [I have no clue]
                #print("Command understood! Beginning Command.")
                #print(Commands[c])
                Commands[c](p) # Run the list according to the instatiated object p (stat.Player)
                commandFound = True
        if not commandFound:
            print("Command not found.")




