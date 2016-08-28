class Menu:
    menu_string=str("")
    def __init__(self):
        return

    def printMenu(self):
        print self.menu_string
        return

    def setMenuString(self, arg1):
        self.menu_string = str(arg1)

    def getMenuString(self):
        return self.menu_string

class BattleMenu(Menu):
    menu_string=("1. Attack | 2. Items | 3. Run")
    def __init__(self):
        return

class BaseMenu(Menu):
    menu_string=("b. Battle | s. Shop | i. Inventory | c. Character Info")
    def __init__(self):
        return
