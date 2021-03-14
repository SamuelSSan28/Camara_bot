from index import  Projetos

projeto_1 = {
    'processo':"438 /2021",
    'protocolo':"542",
    'data':'----',
    'titulo': '---',
    'vereador': "---",
    'situacao':'---',
    'tipo':'----'
}


projetos = [projeto_1]


# Inserimos os quatro projetos na tabela 'Projetos'
Projetos.insert_many(projetos).execute()