from postgres import Postgres
from dto import Contact


class ContactServices:
    def __init__(self):
        self.db = Postgres()
        self.connection = self.db.connect()


    async def get_all_contacts(self):
        try:
            result = self.db.execute_query(query='SELECT * FROM list_contacts')
            return result
        except Exception as error:
            raise ConnectionError(f"Erro de Conexão com o Banco, detalhes ({error})")


    async def get_one_contact(self, id):
        try:
            result = self.db.execute_query(query=f'SELECT * FROM list_contacts WHERE id ={id}')
            return result
        except Exception as error:
            raise ConnectionError(f"Erro de Conexão com o Banco, detalhes ({error})")


    async def post_contact(self, contact: Contact):
        try:
            self.db.execute_query(
                query=f"INSERT INTO list_contacts (name,phone,email) VALUES('{contact.name}','{contact.phone}','{contact.email}')"
                )
            self.db.session.commit()
        except Exception as error:
            raise ConnectionError(f"Erro de Conexão com o Banco, detalhes ({error})")


    async def delete_contact(self, id: int):
        try:
            self.db.execute_query(query=f"DELETE FROM list_contacts WHERE id = ({id})")
            self.db.session.commit()
        except Exception as error:
            raise ConnectionError(f"Erro de Conexão com o Banco, detalhes ({error})")


    async def update_contact(self, contact: Contact, id: int):
        try:
            query = f"UPDATE list_contacts set name = '{contact.name}', phone = '{contact.phone}', email ='{contact.email}' WHERE id = {id} "
            self.db.execute_query(query=query)
            self.db.session.commit()
        except Exception as error:
            raise ConnectionError(f"Erro de Conexão com o Banco, detalhes ({error})")
