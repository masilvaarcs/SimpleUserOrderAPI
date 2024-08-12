# Use uma imagem base leve do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos de requisitos do seu projeto para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Exponha a porta em que o Flask estará rodando
EXPOSE 5000

# Comando para iniciar o aplicativo Flask
CMD ["python", "src/app.py"]
