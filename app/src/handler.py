from postgres import Postgres
from dto import Contact


class ContactSevices:
    def __init__(self, db) -> None:
        self.db = db
        self.connection = db.connect()
    @staticmethod
    async def get_contact(self):
        try:
            self.connection
            result = db.execute_query(query='SELECT * FROM list_contacts')
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")
        return result

    @staticmethod
    async def get_one_contacts(self, id):
        try:
            self.connection
            result = db.execute_query(query=f"SELECT * FROM list_contacts WHERE id ={id}")
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")
        
        return result
    
    @staticmethod
    async def post_contacts(self, contact: Contact, Body=(...)):
        try:
            self.connection
            db.execute_query(query=f"INSERT INTO list_contacts (name,phone,email) VALUES('{contact.name}','{contact.phone}','{contact.email}')")
            db.session.commit()
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")

    @staticmethod
    async def delete_contact(self, id: int):
        try:
            self.connection
            db.execute_query(query=f"DELETE FROM list_contacts WHERE id = ({id})")
            db.session.commit()       
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")

    @staticmethod
    async def update_contact(self, contact: Contact, id): 
        try:
            self.connection
            query=f"UPDATE list_contacts set name = '{contact.name}', phone = '{contact.phone}', email ='{contact.email}' WHERE id = {id} "
            db.execute_query(query=query)
            db.session.commit()
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")

