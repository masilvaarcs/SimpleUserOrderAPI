## Projeto Simple User Order API

Este projeto é uma API simples para gerenciar usuários, com funcionalidades para adicionar, atualizar, remover e listar usuários. A API foi desenvolvida usando Flask e inclui um banco de dados em memória para fins de demonstração.

### Funcionalidades Principais

- **Listar Usuários**: Retorna todos os usuários no sistema.
- **Adicionar Usuário**: Adiciona um novo usuário com os dados fornecidos.
- **Atualizar Usuário**: Atualiza informações de um usuário existente.
- **Remover Usuário**: Remove um usuário do sistema.

### Dados de Usuário Aleatórios

Toda vez que o projeto é executado, ele inicializa com um conjunto de dados de usuários gerados aleatoriamente. Esta funcionalidade é útil para testes e desenvolvimento, permitindo que os desenvolvedores trabalhem com dados realistas sem a necessidade de criar manualmente entradas no banco de dados.

#### Como Funciona

- A biblioteca [Faker](https://faker.readthedocs.io/en/master/) é utilizada para gerar dados fictícios, como nomes, endereços, telefones, e e-mails.
- O script seleciona aleatoriamente cidades e estados para tornar os dados mais variados.
- Um total de 20 usuários são criados automaticamente com a execução do projeto, cada um com um conjunto único de informações.
## Estrutura do Projeto

```plaintext
/SimpleUserOrderAPI
├── src
│   ├── controllers
│   │   ├── user_controller.py
│   │   └── order_controller.py
│   ├── models
│   │   ├── user_model.py
│   │   └── order_model.py
│   ├── views
│   │   ├── user_view.py
│   │   └── order_view.py
│   └── app.py
├── tests
│   ├── test_users.py
│   └── test_orders.py
├── README.md
└── LICENSE
```

## Dependências

Para rodar este projeto, você precisará instalar as seguintes dependências:

- **Flask**: Framework web utilizado para construir a API.
- **pytest**: Framework para testes em Python.
- **pytest-flask**: Extensão do `pytest` para facilitar testes com Flask.

### Instalação das Dependências

Você pode instalar todas as dependências usando o `pip`:

```bash
pip install Flask pytest pytest-flask
```

Alternativamente, você pode usar um arquivo `requirements.txt`:

### Arquivo `requirements.txt`

```plaintext
Flask==2.3.2
pytest==7.5.0
pytest-flask==1.2.0
```

### Instalação via `requirements.txt`

```bash
pip install -r requirements.txt
```

## Configuração do Ambiente

1. **Criar um Ambiente Virtual**

   Recomendo usar um ambiente virtual para isolar as dependências do projeto:

   ```bash
   python -m venv venv
   ```

2. **Ativar o Ambiente Virtual**

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Instalar Dependências**

   Instale as dependências conforme mencionado acima.

   ```bash
   pip install -r requirements.txt
   ```

## Executando o Projeto

1. **Execute o Servidor**

   Com o ambiente virtual ativado, execute o servidor:

   ```bash
   python src/app.py
   ```

   A API estará disponível em `http://localhost:5000`. Você pode verificar se está funcionando acessando `http://localhost:5000/users/` em um navegador ou usando uma ferramenta como `curl` ou Postman.

## Endpoints da API

### Usuários

#### Resumo das Operações

- **GET /users/{id}**: Obtém detalhes de um usuário específico pelo ID.
- **POST /users/**: Cria um novo usuário.
- **PUT /users/{id}**: Atualiza um usuário existente pelo ID.
- **DELETE /users/{id}**: Exclui um usuário pelo ID.

- **GET /users/**: Retorna a lista de usuários.

  #### Exemplo de Requisição GET

  Para obter um usuário específico:

  ```bash
  GET /users/1
  ```

  #### Exemplo de Resposta GET

  Resposta ao obter um usuário com ID 1:

  ```json
  HTTP/1.1 200 OK
  {
    "id": 1,
    "name": "João Silva",
    "phone": "+55 11 98765-4321",
    "street": "Rua das Flores, 123",
    "city": "São Paulo",
    "neighborhood": "Jardim das Acácias",
    "zip_code": "01234-567",
    "state": "SP",
    "email": "joao.silva@example.com",
    "password": "senhaSegura123"
  }
  ```

- **POST /users/**: Adiciona um novo usuário.

  #### Exemplo de Requisição POST

  Para criar um novo usuário:

  ```json
  POST /users/
  {
    "name": "João Silva",
    "phone": "+55 11 98765-4321",
    "street": "Rua das Flores, 123",
    "city": "São Paulo",
    "neighborhood": "Jardim das Acácias",
    "zip_code": "01234-567",
    "state": "SP",
    "email": "joao.silva@example.com",
    "password": "senhaSegura123"
  }
  ```

  #### Exemplo de Resposta POST

  Resposta ao criar um novo usuário (supondo que o ID seja atribuído automaticamente):

  ```json
  HTTP/1.1 201 Created
  {
    "id": 1,
    "name": "João Silva",
    "phone": "+55 11 98765-4321",
    "street": "Rua das Flores, 123",
    "city": "São Paulo",
    "neighborhood": "Jardim das Acácias",
    "zip_code": "01234-567",
    "state": "SP",
    "email": "joao.silva@example.com",
    "password": "senhaSegura123"
  }
  ```

- **PUT /users/{id}**: Atualiza um usuário existente.

  #### Exemplo de Requisição PUT

  Para atualizar um usuário com ID 1:

  ```json
  PUT /users/1
  {
    "name": "João Silva",
    "phone": "+55 11 98765-4321",
    "street": "Rua das Flores, 456",
    "city": "São Paulo",
    "neighborhood": "Jardim das Acácias",
    "zip_code": "01234-567",
    "state": "SP",
    "email": "joao.silva@example.com",
    "password": "novaSenhaSegura456"
  }
  ```

  #### Exemplo de Resposta PUT

  Resposta ao atualizar um usuário com ID 1:

  ```json
  HTTP/1.1 200 OK
  {
    "id": 1,
    "name": "João Silva",
    "phone": "+55 11 98765-4321",
    "street": "Rua das Flores, 456",
    "city": "São Paulo",
    "neighborhood": "Jardim das Acácias",
    "zip_code": "01234-567",
    "state": "SP",
    "email": "joao.silva@example.com",
    "password": "novaSenhaSegura456"
  }
  ```

- **DELETE /users/{id}**: Remove um usuário.

  #### Exemplo de Requisição DELETE

  Para excluir um usuário com ID 1:

  ```bash
  DELETE /users/1
  ```

  #### Exemplo de Resposta DELETE

  Resposta ao excluir um usuário com ID 1:

  ```json
  HTTP/1.1 204 No Content
  ```

### Pedidos

- **GET /orders/**: Retorna a lista de pedidos.
- **POST /orders/**: Adiciona um novo pedido.

  #### Exemplo de Requisição POST

  Para criar um novo pedido:

  ```json
  POST /orders/
  {
    "user_id": 1,
    "product": "Notebook",
    "quantity": 2
  }
  ```

## Testes

Para executar os testes, use o comando:

```bash
pytest tests/
```

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Configuração do Repositório no GitHub

1. **Crie um Repositório no GitHub**

   - Vá até o GitHub e crie um novo repositório com o nome `SimpleUserOrderAPI`.

2. **Adicione os Arquivos ao Repositório**

   - Navegue até a pasta raiz do projeto no seu terminal e inicialize um repositório Git:

     ```bash
     git init
     ```

   - Adicione os arquivos ao repositório:

     ```bash
     git add .
     ```

   - Faça o commit das mudanças:

     ```bash
     git commit -m "Initial commit"
     ```

   - Vincule o repositório local ao repositório remoto no GitHub:

     ```bash
     git remote add origin https://github.com/seuusuario/SimpleUserOrderAPI.git
     ```

   - Faça o push para o GitHub:

     ```bash
     git push -u origin main
     ```

3. **Atualize o `README.md`**

   - Certifique-se de atualizar o link do repositório no `README.md` para refletir o seu repositório GitHub.

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Para fazer isso, por favor, siga estas etapas:

1. Fork o repositório.
2. Crie uma branch para suas alterações (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m 'Adicionei uma nova funcionalidade'`).
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

 Abra um Pull Request.

## Contato

Caso tenha dúvidas ou problemas, você pode me contatar em [masilva.arcs@gmail.com](mailto:masilva.arcs@gmail.com).
```