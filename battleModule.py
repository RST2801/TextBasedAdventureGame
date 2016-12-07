import attackModule as a, copy, collections

class Battles:
    def __init__ (self, _init_enemies, _init_allies,_init_deadEnemies):
        self.enemies = _init_enemies
        self.allies = _init_allies
        self.deadEnemies = _init_deadEnemies
        self.livingEnemies = copy.deepcopy(self.enemies)
        self.livingAllies = copy.deepcopy(self.allies)
        self.livingEnemiesList = list(self.livingEnemies.values())
        self.livingAlliesList = list(self.livingAllies.values())
        self.battleDone = False

    def death(self, entity):
        enemyIndex = self.livingEnemiesList.index(entity)
        del self.livingEnemies[entity.entityName]
        del self.livingEnemiesList[enemyIndex]
        self.deadEnemies[entity.entityName] = entity #this is no longer used
        entity.alive = False

           
        
    def battle(self):
        
        alliesList = list(self.allies.values())
        enemiesList = list(self.enemies.values())
        
                
        for item in list(self.enemies.keys()):
            print("You have entered a battle with {0}".format(item))
                     
        while self.battleDone == False:
            
            self.playerBattleAction(alliesList[0])
                    

                    
    def playerBattleAction(self, player):

            print("Choose the target of your move:")
            
            
            while True:
                enemyNum = 0
                for x in self.livingEnemiesList:
                    enemyNum += 1
                    print("{0}.{1}({2} health)".format(enemyNum,x.entityName, x.health))
                    
                try:
                    enemyChoiceIndex = int(input("")) - 1
                    enemy = self.livingEnemiesList[enemyChoiceIndex]
                    break
                    
                except IndexError:
                    print("Please enter a number matching the indexes on the list")
                except ValueError:
                    print("Please enter a number matching the indexes on the list")

            print("Choose your move:")
           
            
            
            while True:
                attackNum = 0
                for x in player.attackList:
                    attackNum += 1
                    print(" {0}.{1} ({2})".format(attackNum,x.attackName,x.attackDamage))
                    
                try: 
                    attackChoiceIndex = int(input("")) - 1
                    attackChoice = player.attackList[attackChoiceIndex]
                    break
                
                except IndexError:
                    print("Please enter a number matching the indexes on the list")
                except ValueError:
                    print("Please enter a number matching the indexes on the list")
                    
            a.Attack.applyDamage(attackChoice, enemy)
            

            print("You used {0} on {1} for {2} damage! \n {1} now has {3} health".format(attackChoice.attackName, enemy.entityName, attackChoice.attackDamage, enemy.health))
            

            if enemy.health <= 0:
                 
                print("You defeated {0}".format(enemy.entityName))
                self.death(enemy)
                                    
            if len(self.livingEnemies) == 0: 
                print("Congratulations you won the battle!") 
                self.battleDone = True

            if len(self.allies) == 0:
                print("You lost!")
                tba.Game.newGame

            
