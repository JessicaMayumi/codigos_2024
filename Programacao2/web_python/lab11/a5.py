#5 - Considere um objeto em python chamado "nova" que está sendo associado a uma nova instância (objeto) da classe Pessoa. 
#Essa classe possui os campos, nesta ordem: data de nascimento, tipo sanguíneo e nome. 
#Forneça o comando de criação dessa classe usando os seguintes valores: "Maria Clara", "10/02/2000" e "O+".

class Pessoa:
    def __init__(self, data_de_nascimento, tipo_sanguineo, nome):
        self.data_de_nascimento = data_de_nascimento
        self.tipo_sanguineo = tipo_sanguineo
        self.nome = nome
    
    def __str__(self):
        return "Nome: " + self.nome + "\nData de Nascimento: " + self.data_de_nascimento + "\nTipo Sanguíneo: " + self.tipo_sanguineo

nome = input("Nome: ")
dataNascimento = input("Data de Nascimento: ")
tipoSanguineo = input("Tipo Sanguíneo: ")

nova = Pessoa(dataNascimento, tipoSanguineo, nome)

print(nova)

#Inserir os valores na seguinte ordem:
#10/02/2000
#O+
#Maria Clara