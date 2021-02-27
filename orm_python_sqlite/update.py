from index import Vereadores, Projetos

new_author = Vereadores.get(Vereadores.nome == 'Joaquim Caldas')

projeto = Projetos.get(Projetos.codigo=="352 /2021")

# Alteramos o autor do livro
projeto.vereador = new_author

# Salvamos a alteração no banco
projeto.save()