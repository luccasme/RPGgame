class Pessoa:
    # variável de classe
    pais = "Brasil"

    # método de instância
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # método de instância
    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# cria uma instância da classe Pessoa
pessoa1 = Pessoa("João", 30)

# chama o método saudacao da instância
pessoa1.saudacao()