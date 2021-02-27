# read.py

from index import Vereadores, Projetos

projeto = Projetos.get(Projetos.codigo == "352 /2021").get()

print(projeto) #da pra acessar os atributos pelo .


projetos = Projetos.select().join(Vereadores).where(Vereadores.nome=='Elzuila Calisto')

# Exibe a quantidade de registros que corresponde a nossa pesquisa
print("Quantidade de Projetos",projetos.count())

for projetos in projetos:
    print(projetos.codigo)