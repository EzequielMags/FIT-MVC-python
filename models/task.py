from models import db
from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(VARCHAR(100), nullable=False)
    description = db.Column(VARCHAR(200), nullable=False)
    user_id = db.Column(Integer, ForeignKey('users.id'), nullable=False)
    status = db.Column(VARCHAR(50), default='Pendente')
    user = relationship('User', back_populates='tasks')
    # TODORESOLVIDO: Define os campos e o relacionamento da tabela Task
    # - id: chave primária da tarefa
    # - title: título da tarefa (obrigatório)
    # - description: descrição detalhada da tarefa (obrigatório)
    # - user_id: chave estrangeira que conecta a tarefa a um usuário (não nulo)
    # - status: indica o estado da tarefa, padrão "Pendente"
    # - user: relacionamento com a classe User, usando back_populates="tasks" para criar o vínculo bidirecional

    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"