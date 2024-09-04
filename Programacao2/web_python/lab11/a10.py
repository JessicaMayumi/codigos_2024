#10 - Para executar uma aplicação python web criada com o flask, pode-se utilizar o comando app.run(). 
# Porém, há outra maneira de realizar essa execução da aplicação web. 
# Qual é essa maneira, e porque ela é mais interessante?

#Digitar flask run no terminal. Será uma maneira mais simples e recomendada de se executar o programa chamado app.py

#Resposta mais correta: É interessante porque ao enviar a aplicação para o host pythonanywhere, este é o método usado pelo host; se utilizar app.run() a aplicação "travará", pois já está sendo chamada pelo host.