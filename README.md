# sqlalchemy-tutorial
Exemplos de utilização de SQL Alchemy, framework de mapeamento objeto-relacional (ORM) de código aberto.

## Como utilizar
```
# Prepare o ambiente de desenvolvimento
sudo apt install libpq-dev python-dev python-pip python-virtualenv

# Crie um banco de dados chamado sqlalchemy_tutorial em alguma instância do PostgreSQL
# e execute o script bd/aula_sqlalchemy.sql
# Se desejar crie um container docker
docker run --name sqlalchemy-orm-psql \
    -e POSTGRES_PASSWORD=pass \
    -d postgres

# Clone o repositório e acesse o diretório
git clone https://github.com/lccherigath/sqlalchemy-tutorial.git
cd sqlalchemy-tutorial

# Crie um ambiente virtual e ative-o
virtualenv -p python3 venv
source venv/bin/activate

# Instale as dependências do projeto
pip install -r requirements.txt

# Execute os scripts com os exemplos
python inserts.py
python queries.py
python update_delete.py
```
