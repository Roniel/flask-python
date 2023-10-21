FROM python:3.9-slim-buster

ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Define o diretório de trabalho da aplicação dentro do container
WORKDIR /app

# Copia os arquivos da aplicação para o diretório de trabalho
COPY . .

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install requests
RUN apt-get update
EXPOSE 5000
CMD [ "flask", "run" ]