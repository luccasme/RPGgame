
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
        print(f'\n{char.name} selecionado!')
        char.info()
        break

print('\n** FASE 2 **\n')
print('Nesta floresta você vera grandes crianturas e terá várias aventuras e talvez desventuras. Então, tome cuidado!\n')
print('Você terá de escolher entre: caminhar pelas florestas, correndo o risco de tombar com criaturas desconhecidas, ou , escolher o caminho das cavernas, mas sem saber o que há por lá\n')

jorneys = [('Caminho da floresta', 1), ('Caminho das cavernas', 2)]

print('Qual caminho deseja escolher? \n')
for jorney in jorneys:
    print(f'{jorney[1]}. {jorney[0]}')

jorney_selected = int(input('Digite a opção desejada: '))

if jorney[1] == jorney_selected:
    print(f'\n{jorney[0]}, selecionado!\n')

print('** QUE COMEÇE A AVENTURA! **')
        

  






