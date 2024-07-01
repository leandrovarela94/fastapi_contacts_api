from typing import List
from fastapi import APIRouter, HTTPException
from dto import Contact
from handler import ContactServices

router = APIRouter()
instance = ContactServices()

@router.get("/contacts", response_model=List[Contact])
async def read_all_contacts():
        result = await instance.get_all_contacts()

        response_final = [ {
                        "id": item[0],
                        "name": item[1],
                        "phone": item[2],
                        "email": item[3]
                    } for item in result 
                ]    
        return response_final

@router.get("/contacts/{id}", response_model=None)
async def read_one(id: int):
        result = await instance.get_one_contact(id)

        response_final = [ {
                        "id": item[0],
                        "name": item[1],
                        "phone": item[2],
                        "email": item[3]
                    } for item in result 
                ]
    
        return response_final

@router.post("/contacts", response_model=None, status_code=201)
async def create_contact(contact: Contact):

        await instance.post_contact(contact)
        return {"detail": "Contato criado com sucesso"}
    
@router.delete("/contacts/{id}", response_model=None)
async def delete_contact(id: int):

        await instance.delete_contact(id)
        return {"detail": "Contato deletado com sucesso"}
   

@router.put("/contacts/{id}", response_model=None)
async def update_contact(id: int, contact: Contact):

        await instance.update_contact(contact, id)
        
        return {"detail": "Contato atualizado com sucesso"}
    