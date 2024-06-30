from postgres import Postgres
from dto import Contact


connection = Postgres()

class ContactSevices:

    @staticmethod
    async def get_contact():
        try:
            connection.connect()
            result = connection.execute_query(query='SELECT * FROM list_contacts')
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")
        return result

    @staticmethod
    async def get_one_contacts(id):
        try:
            connection.connect()
            result = connection.execute_query(query=f"SELECT * FROM list_contacts WHERE id ={id}")
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")
        
        return result
    
    @staticmethod
    async def post_contacts(contact: Contact, Body=(...)):
        try:
            connection.connect()
            connection.execute_query(query=f"INSERT INTO list_contacts (name,phone,email) VALUES('{contact.name}','{contact.phone}','{contact.email}')")
            connection.session.commit()
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")

    @staticmethod
    async def delete_contact(id: int):
        try:
            connection.connect()
            connection.execute_query(query=f"DELETE FROM list_contacts WHERE id = ({id})")
            connection.session.commit()       
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")

    @staticmethod
    async def update_contact(contact: Contact, id): 
        try:
            connection.connect()
            query=f"UPDATE list_contacts set name = '{contact.name}', phone = '{contact.phone}', email ='{contact.email}' WHERE id = {id} "
            connection.execute_query(query=query)
            connection.session.commit()
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")

