from orm_python_sqlite.index import Projetos, Vereadores
from scraping_camara import Scraping_camara
import os
import json 
import time
from datetime import datetime


def dataHora():
    data_e_hora_atuais = datetime.now()
    return data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S").split()

def gerenciador():
    sc = Scraping_camara()
    projetos = Projetos.select()

    novos_projetos = sc.acess(projetos[-1].processo)

    if novos_projetos :
        print("------Encontrou novos Projetos-------\n")

        with open("dados.json", "w", encoding='utf-8') as outfile:  
            json.dump(novos_projetos, outfile,ensure_ascii=False)
        
        os.system("node .\instagram_api\imagens.js") #gerando as imagens

        os.system("node .\instagram_api\index.js") #postando as imagens

        Projetos.insert_many(novos_projetos).execute()

    else:
        print("Sem projetos novos")


try:
    while True:
        gerenciador()
        print("_______ACABOU_________")
        time.sleep(2000)

except Exception as err:
    d,h = dataHora()
    e = "Error: {0} no dia ".format(err) + d + " as " +h +"\n"
    arq = open('logs.txt', 'a+')
    arq.write(e)
    arq.close()



