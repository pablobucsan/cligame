import time
import errors
string = "hello world"

def myprint(string):
    for char in string:
        print(char, end='')
        time.sleep(.01)


def decision(player,command):
    keywords=['stats()']
    
    while command not in keywords:
        command=input('Comando no reconocido, intenta otra vez: ')
    
    exec(f'{player}.{command}')
    
def test(func):
    def inside():
        valid_commands=['hola']
        command=input('input command: ')

        if errors.InvalidCommand(valid_commands).check(command)!=None:
            print('invalid command')
        
        else:
            func()
    return inside
    

@test
def le():
    print('hola bo dia')    
    

le()

    

