from typing import List
from flask import jsonify, request
from models.user_model import User
from faker import Faker
import random
import bcrypt  # Biblioteca para hashing de senhas

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


def hash_password(password: str) -> str:
    """Gera um hash seguro para a senha."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def generate_random_user(user_id: int) -> User:
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
        password_hash=hash_password("senha123"),  # Armazena a senha como um hash
    )


# Simulação de banco de dados em memória com usuários gerados aleatoriamente
users_db: List[User] = [generate_random_user(i + 1) for i in range(20)]


def get_next_user_id() -> int:
    """Retorna o próximo user_id disponível."""
    if not users_db:
        return 1
    max_id = max(user.user_id for user in users_db)
    return max_id + 1


def get_users():
    """Obtém todos os usuários."""
    return jsonify([user.to_dict() for user in users_db])


def get_user_by_id(user_id):
    """Obtém um usuário pelo ID"""
    user = next((u for u in users_db if u.user_id == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())


def add_user():
    """Adiciona um novo usuário."""
    new_user_data = request.get_json()

    # Validações simples (você pode expandir conforme necessário)
    if "email" not in new_user_data or not new_user_data["email"]:
        return jsonify({"error": "Email is required"}), 400

    if any(user.email == new_user_data["email"] for user in users_db):
        return jsonify({"error": "Email already exists"}), 400

    password = new_user_data.get("password", "")
    if not password:
        return jsonify({"error": "Password is required"}), 400

    new_user_id = get_next_user_id()

    new_user = User(
        user_id=new_user_id,
        name=new_user_data.get("name", ""),
        phone=new_user_data.get("phone", ""),
        street=new_user_data.get("street", ""),
        city=new_user_data.get("city", ""),
        neighborhood=new_user_data.get("neighborhood", ""),
        zip_code=new_user_data.get("zip_code", ""),
        state=new_user_data.get("state", ""),
        email=new_user_data["email"],
        password_hash=hash_password(password),  # Armazena a senha como um hash
    )
    users_db.append(new_user)
    return jsonify(new_user.to_dict()), 201


def update_user(user_id: int):
    """Atualiza um usuário existente."""
    user = next((u for u in users_db if u.user_id == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    update_data = request.get_json()

    if "email" in update_data:
        if any(
            u.email == update_data["email"] and u.user_id != user_id for u in users_db
        ):
            return jsonify({"error": "Email already exists"}), 400

    user.name = update_data.get("name", user.name)
    user.phone = update_data.get("phone", user.phone)
    user.street = update_data.get("street", user.street)
    user.city = update_data.get("city", user.city)
    user.neighborhood = update_data.get("neighborhood", user.neighborhood)
    user.zip_code = update_data.get("zip_code", user.zip_code)
    user.state = update_data.get("state", user.state)
    user.email = update_data.get("email", user.email)

    if "password" in update_data:
        user.password_hash = hash_password(update_data["password"])

    return jsonify(user.to_dict())


def delete_user(user_id: int):
    """Remove um usuário."""
    global users_db
    users_db = [u for u in users_db if u.user_id != user_id]
    return "", 204
