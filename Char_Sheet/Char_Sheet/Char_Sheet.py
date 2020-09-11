import stats
import math
# Char_Sheet
# Phase 1
# Alec Huynh
# 9/10/20
# Creating Basic Functions for calculations

# CHARACTER STATS
# ==================================
# Note: 
# Edit here to make changes to character stats for now
# For saves and ability checks 1 = proficiency

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

# END CHARACTER STATS
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
for obj in STAT_LIST:
    print(obj.name, end =" ") 
    print(obj.stat, end =" ")
    print(obj.roll)




"""
Note: 9/10/20
So far, all of the mat for the ability scores have been determined. 
We will not be including any level up capabilities in the near future
Next goals:
Add game loop with next functionality:


"""










