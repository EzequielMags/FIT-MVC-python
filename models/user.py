from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# Cada classe que herda de db.Model se torna uma tabela no banco de dados.
class User(db.Model): # Declaração de um novo modelo/tabela: User

    # define o nome da tabela no banco de dados para a classe User como "users", como boa prática
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # Define uma coluna ... 
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # TODORESOLVIDO: Definir o relacionamento 1:N entre User e Task
    tasks = relationship('Task', back_populates='user',)

    def __repr__(self):
        return f"<User {self.name}>"