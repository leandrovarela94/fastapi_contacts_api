import orm_config
from sqlalchemy import text


class Postgres:
    def __init__(self):
        self.session = None

    def connect(self):
        try:
            self.session = orm_config.SessionLocal()
            return self.session
        
        except Exception as e:
            raise ConnectionError(message=f'Erro ao conectar ao POSTGRES: {e}')
           
    def execute_query(self, query):
        try:
            if self.session:
                result = self.session.execute(text(query))
                self.session.commit()
                return result.fetchall()
            
        except Exception as e:
            self.session.rollback()
            raise ConnectionError(message=f'Erro ao executar consulta SQL: {e}')
            
        finally:
            self.session.close()
