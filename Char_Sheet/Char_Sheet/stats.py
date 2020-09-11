import math







#Calculation of Stat modifiers from stat array
def mod_calc(raw):
    mod = [math.floor((x-10)/2) for x in raw]


    return mod

def mod_calc_sing(raw):
    mod = math.floor((raw-10)/2)

    return mod



class Character_Stat:
    def __init__(self, name, stat, roll):
        self.name = name
        self.stat = stat
        self.roll = roll

    def Modifier(self):
        mod = math.floor(((self.stat)-10)/2)
        return mod

#class Roll(Character_Stat):
#    def __init__(self, prof):
#        self.prof = prof
#    def value(self):
#        roll_value = 
