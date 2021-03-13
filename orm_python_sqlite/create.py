from index import  Projetos

projeto_1 = {
    'processo':"479 /2021",
    'protocolo':"540",
    'data':'11/03/2021',
    'titulo': 'SOLICITO A SDU/LESTE, O SERVIÇO DE CAPINA, LIMPEZA, RECUPERAÇÃO DA ILUMINAÇÃO PÚBLICA NA RUA PROJETADA 415 NA VILA MEIO NORTE, ZONA LESTE DA CAPITAL',
    'vereador': "Edilberto Borges - Dudu",
    'situacao':'Tramitando'
}


projetos = [projeto_1]


# Inserimos os quatro projetos na tabela 'Projetos'
Projetos.insert_many(projetos).execute()