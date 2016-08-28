class Item:
        Name=""
        Damage=0
        Value=0
        
        def __init__(self, arg1, arg2):
            # constructor
            self.Name = arg1
            self.Damage = arg2

            # accessors
        def getName():
            return self.Name
        def getDamage():
            return self.Damage

class Weapon(Item):
        def __init__(self, arg1, arg2):
            # constructor
            self.Name = arg1
            self.Damage = arg2

class Potion(Item):
        def __init__(self, arg1, arg2):
            # constructor
            self.Name = arg1
            self.Value = arg2
            def restoreHealth():
                return self.Value
