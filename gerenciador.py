from orm_python_sqlite.index import Projetos, Vereadores
from scraping_camara import Scraping_camara
import os
import json 
import time
from datetime import datetime

def gerenciador():
    sc = Scraping_camara()
    try:
        projetos = Projetos.select().order_by(Projetos.processo)
    except Exception as err:
        data_e_hora_atuais = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        e = "Error: {0} no dia ".format(err) + data_e_hora_atuais+"\n"
        arq = open('logs.txt', 'a+')
        arq.write(e)
        arq.close()
        return 0
    
    print("Ultimo processo cadastrado:", projetos[-1].protocolo)
    novos_projetos = sc.acess(projetos[-1].protocolo)

    if novos_projetos != 0 and novos_projetos != []:
        new_dict = dict(sorted(novos_projetos.items()))
        
        with open("dados.json", "w", encoding='utf-8') as outfile:  
            json.dump(new_dict, outfile,ensure_ascii=False)
        
        os.system("node ./instagram_api/imagens.js") #gerando as imagens

        os.system("node ./instagram_api/index.js") #postando as imagens

        for key in novos_projetos.keys():
            dados = {"processo" : key,"protocolo" : novos_projetos[key]["protocolo"],"data" : novos_projetos[key]["data"],"titulo" : novos_projetos[key]["resumo"],"situacao" : novos_projetos[key]["situacao"],"vereador" : novos_projetos[key]["autor"],"tipo" : novos_projetos[key]["tipo"] }
            Projetos.insert(dados).execute()

        print("Processos foram salvos com sucesso: ")
    else:
        print("Sem projetos novos")


while True:
    try:
        gerenciador()
        print("**********\n")
        time.sleep(36000)

    except Exception as err:
        data_e_hora_atuais = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        e = "Error: {0} no dia ".format(err) + data_e_hora_atuais+"\n"
        arq = open('logs.txt', 'a+')
        arq.write(e)
        arq.close()



