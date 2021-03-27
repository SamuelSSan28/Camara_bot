from index import  Projetos

projeto_1 = {
    'protocolo':"43",
    'processo':"548 /2021",
    'data':'----',
    'titulo': '---',
    'vereador': "---",
    'situacao':'---',
    'tipo':'----'
}


projetos = [projeto_1]


# Inserimos os quatro projetos na tabela 'Projetos'
Projetos.insert_many(projetos).execute()