from flask import render_template, request, redirect, url_for
from models import db
from models.task import Task
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        # TODORESOLVIDO buscar todas as tarefas do banco de dados
        tasks = Task.query.all()
        tasks = None 
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        
        if request.method == "POST":
            
            # TODORESOLVIDO capturar dados do formulário (title, description, user_id)
            title = request.form.get('title')
            description = request.form.get('description')
            user_id = request.form.get('user_id')
            # TODORESOLVIDO criar um novo objeto Task com os dados capturados
            nova_task = {
                'title': title,
                'description': description,
                'user_id': user_id
            }

            # TODORESOLVIDO adicionar no db.session e dar commit
            db.session.add(nova_task)
            db.session.commit()
            pass

            return redirect(url_for("list_tasks"))

        # TODORESOLVIDO buscar todos os usuários para exibir no <select> do formulário
        users = User.query.all()

        return render_template("create_task.html", users=users)
    
    @staticmethod
    def update_task_status(task_id):

        tasks = Task.query.all()
        # TODORESOLVIDO buscar a tarefa pelo id
        for i in range(len(tasks)):
            if int(tasks[i].id) == int(task_id):
                task = tasks[i]
                break
        # TODORESOLVIDO: se existir, alternar status entre "Pendente" e "Concluído" e dar commit na alteração
        if task.status == "Pendente":
            task.status = "Concluído"
        else:
            task.status = "Pendente"
        db.session.commit()
        pass 

        return redirect(url_for("list_tasks"))

    @staticmethod
    def delete_task(task_id):
        
        tasks = Task.query.all()
        # TODORESOLVIDO buscar a tarefa pelo id
        for i in range(len(tasks)):
            if int(tasks[i].id) == int(task_id):
                task = tasks[i]
                break

        # TODORESOLVIDO: se ela existir, remover do db.session e dar commit
        db.session.delete(task)
        db.session.commit()
        pass 
    
        return redirect(url_for("list_tasks"))