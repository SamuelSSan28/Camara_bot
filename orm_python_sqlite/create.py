from index import Vereadores, Projetos

# Inserimos um autor 
vereador_1 = Vereadores.create(nome='Elzuila Calisto',perfil="@elzuilac")

# Inserimos um autor 
vereador_2 = Vereadores.create(nome='Joaquim Caldas',perfil="@vereadorjoaquimcaldas")

# Inserimos um autor 
vereador_3 = Vereadores.create(nome='Edilberto Borges - Dudu',perfil="@vereadordudu")


projeto_1 = {
    'processo':"374 /2021",
    'protocolo':"419",
    'data':'0',
    'titulo': 'DISPÕE SOBRE A TRANSPARÊNCIA NO PROCESSO DE VACINAÇÃO CONTRA COVID - 19 EM TERESINA - PI POR MEIO DA OBRIGATORIEDADE DA PUBLICAÇÃO DIÁRIA DE LISTA DE TODOS OS VACINADOS.',
    'vereador_id': vereador_1,
    'situacao':'zzzz',
    'setor':'zzzz',
    'fase':'zzzz',
}

projeto_2 = {
     'processo':"375 /2021",
     'protocolo':"419",
     'data':'0',
    'titulo': 'TRATA-SE DE INDICATIVO DE PROPOSIÇÃO LEGISLATIVA, SUGERINDO AO CHEFE DO PODER EXECUTIVO MUNICIPAL QUE ENCAMINHE A ESTA CASA LEGISLATIVA, UM PROJETO DE LEI QUE TENHA COMO OBJETIVO DO FORNECIMENTO DE ABSORVENTES HIGIÊNICO NAS ESCOLAS DA REDE MUNICIPAL DE ENSINO E NAS UNIDADES DE SAÚDE.',
    'vereador_id': vereador_1,
    'situacao':'zzzz',
    'setor':'zzzz',
    'fase':'zzzz',
}

projeto_3 = {
    'processo':"376 /2021",
    'protocolo':"419",
    'data':'0',
    'titulo': 'SOLICITO A SDU/LESTE, O SERVIÇO DE RECUPERAÇÃO DA ILUMINAÇÃO PÚBLICA, LIMPEZA E CAPINA DA RUA JOSÉ C MELO, LOCALIZADA NO BAIRRO NOVA TERESINA, ZONA LESTE DA CAPITAL.',
    'vereador_id': vereador_3,
    'situacao':'zzzz',
    'setor':'zzzz',
    'fase':'zzzz',
}


projetos = [projeto_1, projeto_2, projeto_3]


# Inserimos os quatro projetos na tabela 'Projetos'
Projetos.insert_many(projetos).execute()