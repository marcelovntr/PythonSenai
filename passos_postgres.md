# Passos Postgres

## instalar o pacote para Postgres no Django:
```bash
pip install psycopg2-binary
```

## Acessar o PSQL:
```bash
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -U postgres
ou:
psql -U postgres
```

## criar o banco diretamente no Postgres:
- clicando ou;
```bash
CREATE DATABASE revisao_db WITH ENCODING 'UTF8';
```
## Configurar nos Swttings:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Roda as migrations
```python
    python manage.py makemigrations
    python manage.py migrate
```


