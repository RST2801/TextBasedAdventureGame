import attackModule as a, random as r, collections

currentEntityIDCount = 0
currentEntities = []
currentEntitiesDic = collections.OrderedDict() 

class EntityType:

    def __init__ (self, _init_entityTypeName, _init_entityTypeID, _init_possibleAttacks, _init_baseHealth, _init_attackNumber):
        self.entityTypeName = _init_entityTypeName
        self.entityTypeID = _init_entityTypeID
        self.possibleAttacks = _init_possibleAttacks
        self.baseHealth = _init_baseHealth
        self.attackNumber = _init_attackNumber
        self.entityOfTypeCount = 0

    def entityGen(self, entityGenNum):
        global currentEntityIDCount
        for x in range(1,entityGenNum+1):

            currentEntityIDCount += 1
            self.entityOfTypeCount += 1
            entityIDX = currentEntityIDCount
            entityHealthX = round(self.baseHealth * (r.uniform(0.5,2)))
            entityAttackListX = r.sample(self.possibleAttacks, self.attackNumber)
            entityNameX = ("{0} {1}".format(self.entityTypeName, x))
            currentEntitiesDic[entityNameX] = Entity(self, entityIDX, entityNameX, entityHealthX, entityAttackListX)
                      
            

class Entity:
    def __init__ (self, _init_entityType, _init_entitiyID,  _init_entityName, _init_entityHealth, _init_entityAttackList):

        self.enitityType = _init_entityType
        self.entityID = _init_entitiyID
        self.entityName = _init_entityName
        self.health = _init_entityHealth #doesnt have entityHealth so that attackModule methods work on entitites too
        self.entityAttackList = _init_entityAttackList
        self.alive = True
        self.isTurn = False

    



    

class PlayerData:
    def __init__ (self,_init_playerName):
        self.playerName = _init_playerName
        self.health = 100
        self.attack = 20 #currently useless
        self.attackList = [a.punchAttack, a.fireballAttack, a.selfDestructAttack]

    
        
        


##print("\n{0} Has {1} health. Choose your move on {0}".format(enemy.entityName, enemy.health))
##
##                    attackNum = 0
##
##                    for x in allies[0].attackList:
##                        attackNum += 1
##                        print(" {0}.{1} ({2})".format(attackNum, x.attackName, x.attackDamage))
##
##                    attackChoiceNum = int(input("")) - 1
##                    attackChoice = allies[0].attackList[attackChoiceNum]
##                    a.Attack.applyDamage(attackChoice, enemy)
##
##                    print("You used {0} on {1} for {2} damage!".format(attackChoice.attackName,enemy.entityName, attackChoice.attackDamage))
##                    print("{0} now has {1} health".format(enemy.entityName, enemy.health))

boar = EntityType("boar", 1, [a.chargeAttack, a.biteAttack, a.scratchAttack], 20, 2)

bird = EntityType("bird", 2, [a.wingAttack, a.peckAttack], 5, 1)


