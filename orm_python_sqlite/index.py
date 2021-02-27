import peewee

# Aqui criamos o banco de dados
db = peewee.SqliteDatabase('camara.db')


class BaseModel(peewee.Model):
    """Classe model base"""
    class Meta:
        # Indica em qual banco de dados a tabela
        # 'author' sera criada (obrigatorio). Neste caso,
        database = db


class Vereadores(BaseModel):
    # A tabela possui apenas o campo 'name', que receberá o nome do autor sera unico
    nome = peewee.CharField()
    perfil = peewee.CharField(unique=True)


class Projetos(BaseModel):
    # A tabela possui apenas o campo 'name', que receberá o nome do autor sera unico
    codigo = peewee.CharField(unique=True)
    data_postado = peewee.CharField()
    titulo = peewee.CharField()
    vereador = peewee.ForeignKeyField(Vereadores)


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