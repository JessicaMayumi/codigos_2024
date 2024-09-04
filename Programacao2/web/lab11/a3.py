#3 - Considere uma classe chamada Pessoa, com os atributos nome, idade e gênero. 
#Forneça o comando que cria um objeto do tipo Pessoa em python. 
#O nome da variável deve ser "nova".

class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero= genero
    
    def __str__(self):
        return "Nome: " + self.nome + "\tIdade: " + self.idade + "\tGênero: " + self.genero

nome = input("Nome: ")
idade = input("Idade: ")
genero = input("Gênero: ")

nova = Pessoa(nome, idade, genero)

print(nova)
