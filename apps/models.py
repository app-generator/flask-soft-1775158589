# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Produto(db.Model):

    __tablename__ = 'Produto'

    id = db.Column(db.Integer, primary_key=True)

    #__Produto_FIELDS__
    tipo = db.Column(db.Text, nullable=True)
    ativo = db.Column(db.Boolean, nullable=True)

    #__Produto_FIELDS__END

    def __init__(self, **kwargs):
        super(Produto, self).__init__(**kwargs)


class Livro(db.Model):

    __tablename__ = 'Livro'

    id = db.Column(db.Integer, primary_key=True)

    #__Livro_FIELDS__
    isbn = db.Column(db.Integer, nullable=True)
    titulo = db.Column(db.Text, nullable=True)
    resumo_sinopse = db.Column(db.String(255),  nullable=True)
    ano_publicacao = db.Column(db.DateTime, default=db.func.current_timestamp())
    edicao = db.Column(db.Integer, nullable=True)
    preco_venda = db.Column(db.Integer, nullable=True)
    preco_compra = db.Column(db.Text, nullable=True)
    qtd_estoque = db.Column(db.Integer, nullable=True)
    formato = db.Column(db.Text, nullable=True)

    #__Livro_FIELDS__END

    def __init__(self, **kwargs):
        super(Livro, self).__init__(**kwargs)


class Autor(db.Model):

    __tablename__ = 'Autor'

    id = db.Column(db.Integer, primary_key=True)

    #__Autor_FIELDS__
    id_autor = db.Column(db.Integer, nullable=True)
    nome = db.Column(db.Text, nullable=True)
    nacionalidade = db.Column(db.Text, nullable=True)

    #__Autor_FIELDS__END

    def __init__(self, **kwargs):
        super(Autor, self).__init__(**kwargs)


class Cliente(db.Model):

    __tablename__ = 'Cliente'

    id = db.Column(db.Integer, primary_key=True)

    #__Cliente_FIELDS__
    id_cliente = db.Column(db.Integer, nullable=True)
    nome = db.Column(db.Text, nullable=True)
    cpf_cnpj = db.Column(db.Integer, nullable=True)
    email = db.Column(db.Text, nullable=True)
    endereco = db.Column(db.String(255),  nullable=True)

    #__Cliente_FIELDS__END

    def __init__(self, **kwargs):
        super(Cliente, self).__init__(**kwargs)


class Editora(db.Model):

    __tablename__ = 'Editora'

    id = db.Column(db.Integer, primary_key=True)

    #__Editora_FIELDS__
    id_editora = db.Column(db.Integer, nullable=True)
    cnpj = db.Column(db.Integer, nullable=True)
    email = db.Column(db.Integer, nullable=True)
    endereco = db.Column(db.String(255),  nullable=True)
    telefone = db.Column(db.Integer, nullable=True)
    ativa = db.Column(db.Boolean, nullable=True)

    #__Editora_FIELDS__END

    def __init__(self, **kwargs):
        super(Editora, self).__init__(**kwargs)


class Venda(db.Model):

    __tablename__ = 'Venda'

    id = db.Column(db.Integer, primary_key=True)

    #__Venda_FIELDS__
    data_venda = db.Column(db.DateTime, default=db.func.current_timestamp())
    valor_total = db.Column(db.Integer, nullable=True)

    #__Venda_FIELDS__END

    def __init__(self, **kwargs):
        super(Venda, self).__init__(**kwargs)


class Itens_Venda(db.Model):

    __tablename__ = 'Itens_Venda'

    id = db.Column(db.Integer, primary_key=True)

    #__Itens_Venda_FIELDS__
    id_itens = db.Column(db.Integer, nullable=True)
    quantidade = db.Column(db.Integer, nullable=True)
    preco_unitario = db.Column(db.Integer, nullable=True)

    #__Itens_Venda_FIELDS__END

    def __init__(self, **kwargs):
        super(Itens_Venda, self).__init__(**kwargs)



#__MODELS__END
