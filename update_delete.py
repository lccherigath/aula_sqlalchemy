# coding: utf-8
from datetime import date
from models.models import Filme, Duble
from base import Session

session = Session()

# Atualizando dados do filme Street Fighter para o lançamento nos EUA
session.query(Filme).filter(Filme.id == 6).update({
    Filme.titulo: 'Street Fighter',
    Filme.data_lancamento: date(1994, 12, 23)
})

# Removendo o dublê do ator The Rock
# delete from duble where id=2
session.query(Duble).filter(Duble.id == 2).delete()

session.commit()
session.close()
