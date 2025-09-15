from flask import render_template, request, redirect, url_for
from flask import Flask, jsonify, request
from models.user import User, db
from flasgger import swag_from
    
class UserController:
    # A chamada para esse método seria feita diretamente pela classe, sem a necessidade de criar um objeto (uma instância):
    @staticmethod
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)

    

    @staticmethod
    def contact():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            
            

            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return render_template('contact.html', error="Usuário com este e-mail já existe", name=name, email=email)

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('contact.html')

    @staticmethod
    @swag_from({
        'tags': ['Users'],
        'summary': 'Lista usuários (JSON)',
        'responses': {
            '200': {
                'description': 'Lista de usuários',
                'content': {
                    'application/json': {
                        'example': [
                            {
                                'id': 1,
                                'name': 'Alice',
                                'email': 'alice@example.com'
                            }
                        ]
                    }
                }
            }
        }
    })
    def list_users_api():
        users = User.query.all()
        return jsonify([
            {
                'id': u.id,
                'name': u.name,
                'email': u.email
            } for u in users
        ])

    @staticmethod
    @swag_from({
        'tags': ['Users'],
        'summary': 'Cria um usuário',
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string'},
                            'email': {'type': 'string'}
                        },
                        'required': ['name', 'email']
                    },
                    'example': {
                        'name': 'Alice',
                        'email': 'alice@example.com'
                    }
                }
            }
        },
        'responses': {
            '201': {
                'description': 'Usuário criado',
                'content': {
                    'application/json': {
                        'example': {
                            'id': 1,
                            'name': 'Alice',
                            'email': 'alice@example.com'
                        }
                    }
                }
            },
            '400': {'description': 'Dados inválidos ou e-mail já cadastrado'}
        }
    })
    def create_user_api():
        data = request.get_json(silent=True) or {}
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({'error': 'name e email são obrigatórios'}), 400

        existing = User.query.filter_by(email=email).first()
        if existing:
            return jsonify({'error': 'E-mail já cadastrado'}), 400

        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()

        return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201

