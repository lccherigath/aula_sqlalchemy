# coding: utf-8
from datetime import date
from models.models import Ator, Contato, Filme
from base import Session

session = Session()

# select * from filme
filmes = session.query(Filme).all()

print('\n#### Buscando todos os filmes:')
for filme in filmes:
    print('{}, lançado em {}'.format(filme.titulo, filme.data_lancamento.isoformat()))
    print('  Elenco:')
    for ator in filme.atores:
        print('    {}'.format(ator.nome))
    print()

# select * from ator
atores = session.query(Ator).all()

print('\n#### Buscando todos os atores:')
for ator in atores:
    print('{}, nascido em {}'.format(ator.nome, ator.nascimento.isoformat()))
    print('  Carreira:')
    for filme in ator.filmes:
        print('    {}'.format(filme.titulo))
    print()


print('\n#### Buscando um filme pela chave primária:')
# select * from filme where id=3
filme = session.query(Filme).get(3)
print('ID: {}'.format(filme.id))
print('Título: {}'.format(filme.titulo))
print('Lançamento: {}'.format(filme.data_lancamento))
print('Elenco: {}'.format( ', '.join( [ator.nome for ator in filme.atores] ) ))

print('\n#### Buscando um ator pela chave primária:')
# select * from ator where id=2
ator = session.query(Ator).get(2)
print('ID: {}'.format(ator.id))
print('Nome: {}'.format(ator.nome))
print('Nascimento: {}'.format(ator.nascimento))
print('Contatos: {}'.format([contato.to_str() for contato in ator.contatos]))
print('Dublê: {}'.format(ator.duble[0].nome if ator.duble else 'Não possui'))
print('Filmes: {}'.format( '; '.join( [filme.titulo for filme in ator.filmes] ) ))


print('\n#### Buscando apenas os títulos dos filmes lançados após 2000:')
# select titulo from filme where data_lancamento > '2000-12-31'
filmes_apos_2000 = session.query(Filme.titulo) \
    .filter(Filme.data_lancamento > date(2000, 12, 31)) \
    .all()
print(filmes_apos_2000)


from sqlalchemy import func

print('\n#### Buscando a quantidade de contatos por ator em ordem crescente:')
# select fk_ator, count(*) as "n_contatos" from contato group by fk_ator order by "n_contatos"
contatos_por_ator = session.query(Contato.fk_ator, func.count(Contato.fk_ator).label('n_contatos')) \
    .group_by(Contato.fk_ator) \
    .order_by('n_contatos') \
    .all()
print(contatos_por_ator)


print('\n#### Buscando os 6 filmes mais recentes:')
# select * from filme order by data_lancamento desc limit 6
filmes_ordenados = session.query(Filme) \
    .order_by(Filme.data_lancamento.desc()) \
    .limit(6) \
    .all()
for filme in filmes_ordenados:
    print('{} - {}'.format(filme.data_lancamento, filme.titulo))


print('\n#### Buscando a quantidade de atores cadastrados:')
# select count(*) from ator
n_atores = session.query(func.count(Ator.id)).scalar()
print(n_atores)

session.close()
