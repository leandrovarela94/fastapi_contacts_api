import os
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cria a classe base para os modelos
Base = declarative_base()

DATABASE_URL = os.getenv('APP_POSTGRES_DATABASE_URL')

# Cria o motor de conexão
engine = create_engine(DATABASE_URL)

# Cria a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Postgres:
    def __init__(self):
        self.session = None

    def connect(self):
        try:
            self.session = SessionLocal()
            print('Conexão ao POSTGRES estabelecida.')
            return self.session
        except Exception as e:
            print(f'Erro ao conectar ao POSTGRES: {e}')

    def execute_query(self, query):
        try:
            if self.session:
                result = self.session.execute(text(query))
                self.session.commit()
                return result.fetchall()
        except Exception as e:
            print(f'Erro ao executar consulta SQL: {e}')
            self.session.rollback()
            return None
        finally:
            self.session.close()
