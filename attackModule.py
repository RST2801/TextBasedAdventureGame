class PlayerData: #move to entity module?
    def __init__(self):
        self.health = 100
        self.attack = 20
        self.attackList = ["punch", "fireball", "selfDestruct"]

class AttackMove:
    def __init__(self,_init_attackName, _init_attackDamage, _init_attackDamageType):
        self.attackName = _init_attackName
        self.attackDamage = _init_attackDamage
        self.attackDamageType = _init_attackDamageType
        
class Attack:
    def __init__ (self,_init_attackMove, _init_attackTarget):
        self.attackMove = _init_attackMove
        self.attackTarget = _init_attackTarget

    def applyDamage(attackMove, attackTarget,): #do something with attack types and multipliers
        attackTarget.health -= attackMove.attackDamage

    
        
    
punchAttack = AttackMove("Punch", 20, "blunt") #this is how to create a new attack move

fireballAttack = AttackMove ("Fireball", 40, "burn")

selfDestructAttack = AttackMove("Self Destruct", 100, "explosion")

chargeAttack = AttackMove ("Charge", 10, "blunt") #will have to change attack type from string to new type

biteAttack = AttackMove ("Bite" , 20, "sharp")

scratchAttack = AttackMove ("Scratch", 15, "sharp")

wingAttack = AttackMove ("Wing Attack", 20, "blunt")

peckAttack = AttackMove ("Peck", 5, "sharp")

#Attack.applyDamage(punchAttack, player) #this is how to execute an attack



#Attack.applyDamage(fireballAttack, player)

#print("The player was attacked by a fireball! they now have {0} health".format(player.health))
