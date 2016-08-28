#!/usr/bin/env python
#Emily Hedman 2016-08-22
# Main Game Logic
from character import Character
from item import Weapon
from item import Potion
from battle import Battle
#<Menus>
from menus import Menu
from menus import BattleMenu
from menus import BaseMenu
from lazylasy import Lazy
#</Menus>
# objects
player = Character(0, 10, 1, 1, 1, True)
enemy = Character(0, 100, 1, 1, 1, False)
weapon = Weapon("Wooden Sword", 8)
battle = Battle(0,0,0,0)
battleMenu = BattleMenu()
baseMenu = BaseMenu()
lazy = Lazy(True)
# </objects>
# variables
game_over = True
game_name_set = False
switch=0
null=""
# </variables>
def main():
    lazy.line()
    print("What do you want to do?")
    baseMenu.printMenu()
    lazy.line()
    choice = raw_input("Make your choice: ")
    if choice == "b":
        return 2
    if choice == "s":
        return 3
    if choice == "i":
        return 4
    if choice == "c":
        return 5
    return 1

def game_SetName():
    print "Welcome to game. Who are you?"
    name = raw_input(">What is your name?")
    player.setName(name)
    return

game_SetName()
while game_over==True:
    switch = main()
    if switch == 2: #battle
        enemy = Character(0, 100, 1, 1, 1, True)
        enemy.setEXP(12)
        enemy.setGold(20)
        battle = Battle(player.Health, enemy.Strength, player.Strength+33, enemy.Health)
        print "You encountered an enemy!"
        while enemy.Alive == True:
            print "Enemy attacks you!"
            player.Health = battle.fight_playerTakeDamage()
            print"The enemy has " + str(enemy.Health) + " health left!"
            print"You have " + str(player.Health) + " health left!"
            battleMenu.printMenu()
            lazy.line()
            battle_choice = raw_input(">What do you want to do?")
            enemy.Health = battle.fight_enemyTakeDamage()
            print"You attack the enemy!"
            enemy.update()
            game_over = player.update()
        if enemy.Alive == False:
            print "You defeated the Enemy!"
            player.addEXP(enemy.EXP)
            player.addItem(enemy.Gold, null, null)
            lazy.line()
        # end of battle
    if switch == 3:
        print "The shop is currently closed!"
        print "But instead, let me fully heal you!"
        player.Health=10
        lazy.line()
    if switch == 4:
        lazy.line()
        player.printCharacterInventory()
        lazy.line()
    if switch == 5:
        lazy.line()
        player.printCharacterStats()
        lazy.line()
