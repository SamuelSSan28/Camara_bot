from index import Vereadores, Projetos

# Buscamos o livro que desejamos excluir do banco
projeto = Projetos.get(Projetos.codigo=="352 /2021")

# Excluimos o livro do banco
projeto.delete_instance()