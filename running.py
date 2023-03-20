import errors
import player
from items import *
from test import myprint,decision


def intro():

    valid_commands=['godsword','escudo','polla']
    invalCommand=errors.InvalidCommand(valid_commands)


    myprint('Benvido, ahora cala a boquiña i escoita. ')
    command=input(f'Escolle a tua wea: {valid_commands} ').lower()
    
    while (invalCommand.check(command)!=None):
        command=input(f'Comando invalido, pensa ben cona: {valid_commands}')
    
    player1=player.Player(command)
    
    myprint(f'Otorgaseche {player1.attack} de ataque, {player1.defense} de defensa e {player1.hp} de vida \n')
    myprint(f'O teu inventario crack : {player1.inventory} \n')
    
    command=input('Que queres facer: \n')
    
    
    decision(player1,command)
    
    
            
def run():
    intro()
    