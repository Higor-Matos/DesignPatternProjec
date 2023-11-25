# Utilize uma imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências do Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie os arquivos do seu projeto para o diretório de trabalho no container
COPY . .

# Informe ao Docker que a aplicação escuta na porta 5000
EXPOSE 80

# Defina o comando para iniciar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port", "80"]
