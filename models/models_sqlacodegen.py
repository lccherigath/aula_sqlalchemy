# coding: utf-8
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Ator(Base):
    __tablename__ = 'ator'

    id = Column(Integer, primary_key=True, server_default=text("nextval('ator_id_seq'::regclass)"))
    nome = Column(String(150), nullable=False)
    nascimento = Column(Date, nullable=False)

    filme = relationship('Filme', secondary='filme_ator')


class Filme(Base):
    __tablename__ = 'filme'

    id = Column(Integer, primary_key=True, server_default=text("nextval('filme_id_seq'::regclass)"))
    titulo = Column(String(150), nullable=False)
    data_lancamento = Column(Date, nullable=False)


class Contato(Base):
    __tablename__ = 'contato'

    id = Column(Integer, primary_key=True, server_default=text("nextval('contato_id_seq'::regclass)"))
    telefone = Column(String(15), nullable=False)
    endereco = Column(String(150), nullable=False)
    fk_ator = Column(ForeignKey('ator.id', match='FULL'), nullable=False)

    ator = relationship('Ator')


class Duble(Base):
    __tablename__ = 'duble'

    id = Column(Integer, primary_key=True, server_default=text("nextval('duble_id_seq'::regclass)"))
    nome = Column(String(150), nullable=False)
    ativo = Column(Boolean, nullable=False)
    fk_ator = Column(ForeignKey('ator.id', match='FULL'), nullable=False)

    ator = relationship('Ator')


t_filme_ator = Table(
    'filme_ator', metadata,
    Column('fk_filme', ForeignKey('filme.id', match='FULL'), primary_key=True, nullable=False),
    Column('fk_ator', ForeignKey('ator.id', match='FULL'), primary_key=True, nullable=False)
)
