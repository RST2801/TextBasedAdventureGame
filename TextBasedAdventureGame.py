import time as t, attackModule as a, battleModule as b, characterModule as c, random as r, collections   
##TO DO:
##CREATE A BATTLE GENERATOR THAT CHOOSER RANDOM ENTITY TYPES 
##CREATE ENTITY AI MODULE/ACTION METHOD AND ADD THEIR ACTION TO THE BATTLE WHILE LOOP 
##maybe create a method that automatically creates menus for me, to save up on time

class Game:
    def newGame():

        c.currentMobIDCount = 0
        _init_playerName = input("How should we call you adventurer? \n")
        Player1 = c.PlayerData(_init_playerName)
        print("Hello {0}!".format(Player1.playerName)) 
        print("You have encountered a pack of wild {0}s! It's a fight!!".format(c.boar.entityTypeName)) #change boars to entityTypeName of the gen
        enemyGenRand = r.randint(2,2) #add dificulty class that dictamines span number, mob health variation and attack dmg multipliers
        print("You have encountered a pack of {1} wild {0}s! It's a fight!!".format(c.boar.entityTypeName, enemyGenRand))
        c.boar.entityGen(enemyGenRand)
        _init_enemies = c.currentEntitiesDic
        _init_allies = collections.OrderedDict()
        _init_allies["Player 1"] = Player1
        _init_deadEnemies = collections.OrderedDict()
        Battle1 = b.Battles(_init_enemies, _init_allies, _init_deadEnemies)
        Battle1.battle()
    
        
        

def startMenu():
    print("Press Enter to play")
    input("")
    Game.newGame()
startMenu()

