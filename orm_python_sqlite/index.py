import peewee

# Aqui criamos o banco de dados
db = peewee.SqliteDatabase('camara.db')


class BaseModel(peewee.Model):
    """Classe model base"""
    class Meta:
        database = db


class Vereadores(BaseModel):
    nome = peewee.CharField()
    perfil = peewee.CharField(unique=True)


class Projetos(BaseModel):
    processo = peewee.CharField(unique=True)
    protocolo = peewee.CharField()
    data = peewee.CharField()
    titulo = peewee.CharField()
    situacao = peewee.CharField()
    vereador = peewee.CharField()
    tipo = peewee.CharField()
    

if __name__ == '__main__':
    try:
        Vereadores.create_table()
        print("Tabela 'Vereadores' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Vereadores' ja existe!")

    try:
        Projetos.create_table()
        print("Tabela 'Projetos' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Projetos' ja existe!")