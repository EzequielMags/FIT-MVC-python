import os

class Config:               
                            # tipo do banco e a sua localização (arquivo)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    #  desabilita o recurso de o SQLAlchemy monitorar e emitir sinais quando um objeto é alterado, o que é a prática recomendada
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # chave secreta e única usada pelo Flask para a segurança da aplicação, assinar os cookies de sessão e proteger formulários
    SECRET_KEY = os.urandom(24)
    