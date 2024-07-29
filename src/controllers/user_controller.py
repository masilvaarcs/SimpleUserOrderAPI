from typing import List, Any
from flask import jsonify, request
from models.user_model import User
from faker import Faker
import random

# Instância da biblioteca Faker para dados em português do Brasil
fake = Faker("pt_BR")

# Dados de estados e cidades para variedade nos dados gerados
states_and_cities = [
    ("SP", ["São Paulo", "Campinas", "Santos"]),
    ("RJ", ["Rio de Janeiro", "Niterói", "Petrópolis"]),
    ("MG", ["Belo Horizonte", "Uberlândia", "Contagem"]),
    ("RS", ["Porto Alegre", "Caxias do Sul", "Pelotas"]),
    ("BA", ["Salvador", "Feira de Santana", "Vitória da Conquista"]),
]


def generate_random_user(user_id):
    # Escolhe um estado e uma cidade aleatoriamente
    state, cities = random.choice(states_and_cities)
    city = random.choice(cities)

    # Gera e retorna um novo usuário com dados aleatórios
    return User(
        user_id=user_id,
        name=fake.first_name(),
        phone=fake.phone_number(),
        street=fake.street_address(),
        city=city,
        neighborhood=fake.street_name(),
        zip_code=fake.postcode(),
        state=state,
        email=fake.email(),
        password="senha123",
    )


# Simulação de banco de dados em memória com usuários gerados aleatoriamente
users_db: List[User] = [generate_random_user(i + 1) for i in range(20)]


def get_users():
    """Obtém todos os usuários"""
    return jsonify([user.to_dict() for user in users_db])


def add_users():
    """Adiciona um novo usuário"""
    new_user_data = request.get_json()
    new_user = User(
        user_id=len(users_db) + 1,
        name=new_user_data["name"],
        phone=new_user_data.get("phone", ""),
        street=new_user_data.get("street", ""),
        city=new_user_data.get("city", ""),
        neighborhood=new_user_data.get("neighborhood", ""),
        zip_code=new_user_data.get("zip_code", ""),
        state=new_user_data.get("state", ""),
        email=new_user_data.get("email", ""),
        password=new_user_data.get("password", ""),
    )
    users_db.append(new_user)
    return jsonify(new_user.to_dict()), 201


def update_user(user_id):
    """Atualiza um usuário existente"""
    user = next((u for u in users_db if u.user_id == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    update_data = request.get_json()
    user.name = update_data.get("name", user.name)
    user.phone = update_data.get("phone", user.phone)
    user.street = update_data.get("street", user.street)
    user.city = update_data.get("city", user.city)
    user.neighborhood = update_data.get("neighborhood", user.neighborhood)
    user.zip_code = update_data.get("zip_code", user.zip_code)
    user.state = update_data.get("state", user.state)
    user.email = update_data.get("email", user.email)
    user.password = update_data.get("password", user.password)

    return jsonify(user.to_dict())


def delete_user(user_id):
    """Remove um usuário"""
    global users_db
    users_db = [u for u in users_db if u.user_id != user_id]
    return "", 204
