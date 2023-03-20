
from items import *
from test import myprint

class Player():
    def __init__(self,command):
        if (command=='godsword'):
            self.attack=60
            self.defense=30
            self.hp=100
            self.inventory=['godsword','','']
            
        elif (command=='escudo'):
            self.attack=30
            self.defense=50
            self.hp=120     
            self.inventory=['escudo','','']      

        else:
            self.attack=20
            self.defense=20
            self.hp=20
            self.inventory=['dildo','','']
    
    def stats(self):
        print(f'Ahora mismo tes {self.attack} de ataque, {self.defense} de defensa e {self.hp} de vida')
        
    def show(self,item):
        while (item not in self.inventory):
            myprint('que cona dis se non tes ese item')
            c=input('que ques facer: ')
        
        print(exec(item).showattributes())
        
        #item=items.AttackItem(item)
        
    
        