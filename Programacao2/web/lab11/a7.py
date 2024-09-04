#7 - Há uma forma de escrever string de maneira que variáveis sejam substituídas por seus valores. 
#Em python, forneça um exemplo de como fazer essa operação. A frase de modelo é esta: 'O nome da pessoa é YYYYYYY'. 
#Em lugar de YYYYYYY, deve aparecer o valor de uma variável chamada abc. Considere que a string vai ser exibida na tela, ou seja, vai estar dentro de um comando print.

frase = "O nome da pessoa é YYYYYYY."

abc = input(str("Insira seu nome: "))

print(frase.replace("YYYYYYY", abc ))