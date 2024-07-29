import unittest
from src.app import app


class TestUserAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_users(self):
        response = self.app.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_add_user(self):
        response = self.app.post('/users/', json={
            'name': 'Charlie',
            'phone': '+55 11 99999-3333',
            'street': 'Rua dos Girassóis, 789',
            'city': 'São Paulo',
            'neighborhood': 'Vila Mariana',
            'zip_code': '04100-000',
            'state': 'SP',
            'email': 'charlie@example.com',
            'password': 'senhaSegura'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Charlie')
        self.assertEqual(response.json['phone'], '+55 11 99999-3333')
        self.assertEqual(response.json['street'], 'Rua dos Girassóis, 789')
        self.assertEqual(response.json['city'], 'São Paulo')
        self.assertEqual(response.json['neighborhood'], 'Vila Mariana')
        self.assertEqual(response.json['zip_code'], '04100-000')
        self.assertEqual(response.json['state'], 'SP')
        self.assertEqual(response.json['email'], 'charlie@example.com')
        self.assertEqual(response.json['password'], 'senhaSegura')

    def test_update_user(self):
        response = self.app.put('/users/1', json={
            'name': 'Alice Updated',
            'phone': '+55 11 99999-1112',
            'street': 'Rua das Palmeiras, 456',
            'city': 'São Paulo',
            'neighborhood': 'Jardim das Rosas',
            'zip_code': '01234-567',
            'state': 'SP',
            'email': 'alice.updated@example.com',
            'password': 'novaSenhaSegura'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Alice Updated')
        self.assertEqual(response.json['phone'], '+55 11 99999-1112')
        self.assertEqual(response.json['street'], 'Rua das Palmeiras, 456')
        self.assertEqual(response.json['city'], 'São Paulo')
        self.assertEqual(response.json['neighborhood'], 'Jardim das Rosas')
        self.assertEqual(response.json['zip_code'], '01234-567')
        self.assertEqual(response.json['state'], 'SP')
        self.assertEqual(response.json['email'], 'alice.updated@example.com')
        self.assertEqual(response.json['password'], 'novaSenhaSegura')

    def test_delete_user(self):
        # Adiciona um usuário para garantir que ele exista antes de tentar deletar
        self.app.post('/users/', json={
            'name': 'Temp User',
            'phone': '+55 11 99999-0000',
            'street': 'Rua Exemplo, 123',
            'city': 'São Paulo',
            'neighborhood': 'Centro',
            'zip_code': '01000-000',
            'state': 'SP',
            'email': 'tempuser@example.com',
            'password': 'tempSenha'
        })

        # Obtém o ID do usuário que foi adicionado
        response = self.app.get('/users/')
        user_id = next((user['id'] for user in response.json if user['name'] == 'Temp User'), None)

        # Deleta o usuário
        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)

        # Verifica se o usuário foi realmente deletado
        response = self.app.get('/users/')
        self.assertNotIn({'id': user_id, 'name': 'Temp User'}, response.json)


if __name__ == '__main__':
    unittest.main()
