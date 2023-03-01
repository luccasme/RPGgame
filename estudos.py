
print ('-- BEM-VINDO À SELVA --\n')

print ('** FASE 1 **\n')


class Char: 
    def __init__(self, name, strength, agility, intell):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intell = intell

    def info(self):
        print(f'Olá, você um {self.name}! Sua força é {self.strength}, sua agilidade é {self.agility} e sua inteligência é {self.intell}.')
        
chars = [

    Char('Aventureiro', '6', '10', '8'),
    Char('Caçador', '8', '5', '4'),
    Char('Forasteiro', '6', '8', '5')
    
    ]

print('Selecione seu personagem: \n')
for char in chars:
        print(f"{chars.index(char)+1}. {char.name}")

char_selected = int(input('\nDigite o número do seu personagem: '))

for char in chars:

    if chars.index(char)+1 == char_selected:
        print(f'\n{char.name} selecionado!','\n')
        char.info()
        break

print('\n** FASE 2 **\n')
print('Nesta floresta você vera grandes crianturas e terá várias aventuras e talvez desventuras. Então, tome cuidado!\n')
print('Você terá de escolher entre: caminhar pelas florestas, correndo o risco de tombar com criaturas desconhecidas, ou , escolher o caminho das cavernas, mas sem saber o que há por lá\n')

class map:
    def __init__(self, name):
        self.name = name

    def mapa(self):
        print(f'{self.name}')

jorneys = [ 

    map('Caminho das montanhas'),
    map('Caminho das cavernas')

]

print('Qual caminho deseja escolher? \n')
for jorney in jorneys:
    print(f'{jorneys.index(jorney)+1}. {jorney.name}')

jorney_selected = int(input('\nDigite a opção desejada: '))

for jorney in jorneys:

    if jorneys.index(jorney)+1 == jorney_selected:
        print(f'\n{jorney.name} selecionado!\n')
        
        break

print('** QUE COMEÇE A AVENTURA! **')



  






