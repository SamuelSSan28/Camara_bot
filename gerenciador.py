from orm_python_sqlite.index import Projetos, Vereadores
from scraping_camara import Scraping_camara
import os
import json 

sc = Scraping_camara()
projetos = Projetos.select()

vereadores_dict = {}
vereadores_dict_nome = {}
vereadores = Vereadores.select()

for vereador in vereadores:
    vereadores_dict.update({vereador.nome : {"id": vereador.id, "perfil": vereador.perfil}})
    vereadores_dict_nome.update({vereador.id : {"nome": vereador.nome, "perfil": vereador.perfil}})


print(projetos[-1].processo)

novos_projetos = sc.acess(projetos[-1].processo)

if novos_projetos :
    print("FINISH HIT")
    with open("dados.json", "w", encoding='utf-8') as outfile:  
        json.dump(novos_projetos, outfile,ensure_ascii=False)
    
    os.system("node .\instagram_api\imagens.js") #gerando as imagens

    #os.system("node .\instagram_api\index.js") #postando as imagens

   # Projetos.insert_many(novos_projetos).execute()
else:
    print("Sem projetos novos")



