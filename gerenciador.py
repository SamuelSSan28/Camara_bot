from orm_python_sqlite.index import Projetos, Vereadores
from scraping_camara import Scraping_camara
from gerar_imagens import gerador
import os

sc = Scraping_camara()
projetos = Projetos.select()

vereadores_dict = {}
vereadores_dict_nome = {}
vereadores = Vereadores.select()

for vereador in vereadores:
    #print(vereador.nome)
    vereadores_dict.update({vereador.nome : {"id": vereador.id, "perfil": vereador.perfil}})
    vereadores_dict_nome.update({vereador.id : {"nome": vereador.nome, "perfil": vereador.perfil}})

novos_projetos = sc.acess(projetos[-1].processo, vereadores_dict)[::-1]

if novos_projetos :
    gerador.gerar_imagens(novos_projetos, vereadores_dict_nome)

    os.system("node .\instagram_api\index.js") #postando as imagens

    Projetos.insert_many(novos_projetos).execute()
    print("Finish him")
else:
    print("Sem projetos novos")



