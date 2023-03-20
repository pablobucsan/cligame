

class AttackItem():
    def __init__(self, name,attackdmg,durability):
        self.name=name
        self.attackdmg=attackdmg
        self.durability=durability
        
    def showattributes(self):
        print(f'{self.name} currently has {self.attackdmg} defense points and {self.durability} durability points ')
        
class DefenseItem():
    def __init__(self, name,defense,durability):
        self.name=name
        self.defense=defense
        self.durability=durability
    
    def showattributes(self):
        print(f'{self.name} currently has {self.defense} defense points and {self.durability} durability points ')
    
godsword=AttackItem('GodSword',60,100)
godshield=DefenseItem('GodShield',20,100)

usableitems={
    'GodSword': [godsword.name,godsword.attackdmg,godsword.durability],
    'GodShield': [godshield.name,godshield.defense,godshield.durability]
    }



