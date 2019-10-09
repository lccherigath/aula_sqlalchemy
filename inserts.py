# coding: utf-8
from datetime import date
from models.models import Ator, Contato, Filme, Duble
from base import Session

session = Session()

# Adicionando filmes
identidade_bourne = Filme(titulo='A Identidade Bourne', data_lancamento=date(2002, 10, 11))
velozes_e_furiosos_7 = Filme(titulo='Velozes e Furiosos 7', data_lancamento=date(2015, 4, 2))
sem_dor_sem_ganho = Filme(titulo='Sem Dor, Sem Ganho', data_lancamento=date(2013, 8, 23))
gente_grande = Filme(titulo='Gente Grande', data_lancamento=date(2010, 9, 24))
click = Filme(titulo='Click', data_lancamento=date(2006, 8, 11))
street_fighter = Filme(titulo='Street Fighter - A Batalha Final', data_lancamento=date(1995, 9, 19))
kickboxer = Filme(titulo='Kickboxer - O Desafio do Dragão', data_lancamento=date(1989, 9, 8))
bloodsport = Filme(titulo='O Grande Dragão Branco', data_lancamento=date(1988, 12, 9))
cyborg = Filme(titulo='Cyborg - O dragão do futuro', data_lancamento=date(1989, 4, 7))
rocky_4 = Filme(titulo='Rocky IV', data_lancamento=date(1985, 11, 27))
os_mercenarios_2 = Filme(titulo='Os Mercenários 2', data_lancamento=date(2012, 8, 31))
soldado_universal = Filme(titulo='Soldado Universal', data_lancamento=date(1992, 7, 10))

# Adicionando atores
matt_damon = Ator(nome='Matt Damon', nascimento=date(1970, 10, 8))
dwayne_johnson = Ator(nome='Dwayne Johnson', nascimento=date(1972, 5, 2))
mark_wahlberg = Ator(nome='Mark Wahlberg', nascimento=date(1971, 6, 5))
van_damme = Ator(nome='Jean-Claude Van Damme', nascimento=date(1960, 10, 18))
adam_sandler = Ator(nome='Adam Sandler', nascimento=date(1966, 9, 9))
stallone = Ator(nome='Sylvester Stallone', nascimento=date(1946, 7, 6))
dolph_lundgren = Ator(nome='Dolph Lundgren', nascimento=date(1957, 11, 3))

# Adicionando atores a filmes
identidade_bourne.atores = [matt_damon]
velozes_e_furiosos_7.atores = [dwayne_johnson]
sem_dor_sem_ganho.atores = [dwayne_johnson, mark_wahlberg]
gente_grande.atores = [adam_sandler]
click.atores = [adam_sandler]
street_fighter.atores = [van_damme]
kickboxer.atores = [van_damme]
bloodsport.atores = [van_damme]
cyborg.atores = [van_damme]
rocky_4.atores = [stallone, dolph_lundgren]
os_mercenarios_2.atores = [stallone, dolph_lundgren, van_damme]
soldado_universal.atores = [van_damme, dolph_lundgren]

# Adicionando contatos a atores
matt_contato = Contato(telefone='415 555 2671', endereco='Burbank, CA', ator=matt_damon)
dwayne_contato = Contato(telefone='423 555 5623', endereco='Glendale, CA', ator=dwayne_johnson)
dwayne_contato_2 = Contato(telefone='421 444 2323', endereco='West Hollywood, CA', ator=dwayne_johnson)
mark_contato = Contato(telefone='421 333 9428', endereco='Glendale, CA', ator=mark_wahlberg)

# Adicionando dublês
matt_duble = Duble(nome='John Doe', ativo=True, ator=matt_damon)
dwayne_duble = Duble(nome='John Roe', ativo=True, ator=dwayne_johnson)
mark_duble = Duble(nome='Richard Roe', ativo=True, ator=mark_wahlberg)

try:
    Persistindo dados
    session.add(identidade_bourne)
    session.add(velozes_e_furiosos_7)
    session.add(sem_dor_sem_ganho)
    session.add(gente_grande)
    session.add(click)
    session.add(street_fighter)
    session.add(kickboxer)
    session.add(bloodsport)
    session.add(cyborg)
    session.add(rocky_4)
    session.add(os_mercenarios_2)
    session.add(soldado_universal)

    session.add(matt_damon)
    session.add(dwayne_johnson)
    session.add(mark_wahlberg)
    session.add(van_damme)
    session.add(adam_sandler)
    session.add(stallone)
    session.add(dolph_lundgren)

    session.add_all([matt_contato, dwayne_contato, dwayne_contato_2, mark_contato])
    
    session.add_all([matt_duble, dwayne_duble, mark_duble])
    
    session.commit()
    session.close

except Exception as e:
    print('Error: ', e)
finally:
    session.close()
