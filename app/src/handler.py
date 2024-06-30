import postgres as client

class ContactSevices:

    def __init__(self):
        self.connect = client.Postgres().connect()

    async def get_contact(self):
        try:
            result = await self.connect.execute_query(query='SELECT * FROM list_contacts')
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")
        return result


    async def get_one_contacts(self, id):
        try:
            result = await self.connect.execute_query(query=f"SELECT * FROM list_contacts WHERE id ={id}")
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")
        
        return result
    

    async def post_contacts(self, contact: client.Contact, Body=(...)):
        try:
            await self.connect.execute_query(query=f"INSERT INTO list_contacts (name,phone,email) VALUES('{contact.name}','{contact.phone}','{contact.email}')")
            await self.connect.conn.commit()
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")


    async def delete_contact(self, id: int):
        try:
            await self.connect.execute_query(query=f"DELETE FROM list_contacts WHERE id = ({id})")
            await self.connect.conn.commit()       
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")


    async def update_contact(self, contact: client.Contact, id): 
        try:
            query=f"UPDATE list_contacts set name = '{contact.name}', phone = '{contact.phone}', email ='{contact.email}' WHERE id = {id} "
            await self.connect.execute_query(query=query)
            await self.connect.conn.commit()
        except Exception as error:
            raise ConnectionError(msg=f"Erro de Conexão com o Banco, detalhes ({error})")

