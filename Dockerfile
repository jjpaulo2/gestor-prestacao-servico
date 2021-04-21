FROM python:3.9-buster
LABEL author="João Paulo Carvalho <jjpaulo2@protonmail.com>"

# MONTANDO VOLUME EM /srv E DEFININDO
# COMO DIRETÓRIO ATUAL

VOLUME /srv
WORKDIR /srv

# INSTALANDO AS DEPENDÊNCIAS DO PROJETO

COPY requirements.txt .
RUN pip install -r requirements.txt

# EXPONDO A PORTA QUE SERÁ USADA

EXPOSE 8888

# EXECUTANDO AS MIGRAÇÕES E RODANDO O
# SERVIDOR DE DESENVOLVIMENTO

CMD python ./manage.py migrate \
 && python ./manage.py runserver 0.0.0.0:8888