

class Entity:
    def __init__ (self, _init_entityType, _init_entityName, _init_entitiyID, _init_entityHealth, _init_entityAttackList):

        self.enitityType = _init_entityType
        self.entityID = _init_entitiyID
        self.entityName = _init_entityName
        self.health = _init_entityHealth #replace name of attributes, take away the "entity" part, so that attack methods work on entitys too
        self.entityAttackList = _init_entityAttackList
        self.alive = True
        self.isTurn = False


entityType = "boar"
entityTypeName = "boar"
entityIDX = 3
entityHealthX = 23
entityAttackListX = ["charge","bite"]
currentEntityTypeCount = 2
x = '{0}{1} = Entity({2}, {0}{1}, {3} , {4}, {5} )'.format(entityTypeName,currentEntityTypeCount,str(entityType), entityIDX, entityHealthX, entityAttackListX)
exec(x)
print(boar2.entityName)



==========================================================================================

#Notes on dicitionary and dinamic creation of variables
currentEntitiesDic = {}
entityIDCount = 0
entityTypeName = "boar"
class Entity:
    def __init__ (self, _init_entityType, _init_entitiyID, _init_entityHealth, _init_entityAttackList):

        self.enitityType = _init_entityType
        self.entityID = _init_entitiyID
        self.health = _init_entityHealth #replace name of attributes, take away the "entity" part, so that attack methods work on entitys too
        self.entityAttackList = _init_entityAttackList
        self.alive = True
        self.isTurn = False

for x in range (1,10):
    entityIDCount += 1
    entityName = ''.join([entityTypeName, str(x)])
    currentEntitiesDic[entityName] = Entity("boar", entityIDCount, 20, ["scratch", "bite"])

print (currentEntitiesDic)

print(currentEntitiesDic['boar1'].health)



