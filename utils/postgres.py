import os

import sqlalchemy as sa
from dotenv import load_dotenv

load_dotenv(dotenv_path='docker-compose.env')


def get_pg_conn():
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    database = os.getenv('POSTGRES_DB')

    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"

    pg_engine = sa.create_engine(url)
    pg_conn = pg_engine.connect()

    return pg_conn
