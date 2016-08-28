class Character:
    Name="CharacterName"
    Species=["Monster", "Orc", "Goblin"]
    Health=10
    Strength=1
    Magic=1
    Archery=1
    Alive=True
    EXP=0
    EXP_LVLUP=28
    LVL=1
    Gold=0
    def __init__(self, name, health, strength, magic, archery, alive):
        self.Health = health
        self.Strength = strength
        self.Magic = magic
        self.Archery = archery
        self.Name = self.Species[name]
        self.Alive = alive

    def setName(self, _name):
        self.Name = _name
        return
    def setEXP(self, _EXP):
        self.EXP = _EXP
        return
    def setGold(self, _Gold):
        self.Gold = _Gold
        return

    def update(self):
        if self.Health <= 0:
            self.Alive = False
        return self.Alive

    def printCharacterStats(self):
        print "< General >"
        print "Name: " + self.Name
        print "Level: " + str(self.LVL) +" | "+ "EXP: " + str(self.EXP) +" | "+ "Next Level: " + str(self.EXP_LVLUP) 
        print "Gold: " + str(self.Gold)
        print " "
        print "< Skills >"
        print "Health: " + str(self.Health)
        print "Strength: " + str(self.Strength)
        print "Magic: " + str(self.Magic)
        print "Archery: " + str(self.Archery)
        return
    def printCharacterInventory(self):
        print "No items in inventory! ... yet"
        return

    def addEXP(self, arg1):
        print "Awarded " + str(arg1) + " EXP!"
        _EXP_LVLUP = float(self.EXP_LVLUP) * 1.44# next level exp increase by 44%
        self.EXP += arg1 #add exp
        #<level check>
        if self.EXP >= self.EXP_LVLUP:
            self.LVL+=1#level up
            _EXP=self.EXP_LVLUP
            self.EXP_LVLUP = int(_EXP + _EXP_LVLUP)#set next level up xp
            print "Level Up!\n You are now level: " + str(self.LVL)
        #</level check>
        return
    def addItem(self, arg1, arg2, arg3):
        g=" gold!"
        if arg2 != "":
            print "Found " + str(arg1) + g
            print "Found " + arg3 + " item!"
            return
        print "Found " + str(arg1) + g
        return
