from orm_python_sqlite.index import Projetos
from scraping_camara import Scraping_camara


sc = Scraping_camara()
projetos = Projetos.select()
novos_projetos = sc.acess(projetos[-1].processo)[::-1]
Projetos.insert_many(novos_projetos).execute()
