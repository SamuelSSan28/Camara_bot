from scraping_camara import Scraping_camara
import os
import json 
import time
from datetime import datetime

def gerenciador():
    sc = Scraping_camara()
    print("COmecou")
    novos_projetos = sc.acess(1)
    print(novos_projetos)
    if novos_projetos != 0 and novos_projetos != []:
        new_dict = dict(novos_projetos.items())
        with open("dados_projetos_de_lei_2021.json", "w", encoding='utf-8') as outfile:
            json.dump(new_dict, outfile,ensure_ascii=False)
        
        print("Processos foram salvos com sucesso: ")
  


gerenciador()
        
