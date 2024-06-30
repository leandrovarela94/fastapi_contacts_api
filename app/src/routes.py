from fastapi import APIRouter
from postgres import Postgres
from handler import ContactSevices
from dto import Contact
from typing import Union, List

router = APIRouter()

instance = ContactSevices()

@router.get("/contacts", response_model=Union[Contact,List[Contact]])
async def read_all():

    result = await instance.get_contact()

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

    result = await instance.get_one_contacts(id)

    response_final = [ {
                        "id": item[0],
                        "name": item[1],
                        "phone": item[2],
                        "email": item[3]
                    } for item in result 
                ]
    
    return response_final


@router.post("/contacts", response_model=None)
async def create_contact(contact: Contact):

    await instance.post_contacts(contact)

    return {f"Sucess Created"}


@router.delete("/contacts/{id}")
async def delete_contact(id: int):

    await instance.delete_contact(id)
    
    return {f"Sucess : Deleted"}


@router.put("/contacts/{id}")
async def update_contact(contact: Contact, id: int):

    await instance.update_contact(
        contact, id)

    return {f"Sucess Updated"}
