from fastapi import APIRouter
from handler import ContactSevices
from model import Contact
from typing import Union, List

router = APIRouter()


@router.get("/contacts")
async def read_all(response_model=Union[Contact,List[Contact]]):

    result = await ContactSevices.get_contact()

    response_final = []

    for item in result:
        response_final = {
            "id": item[0],
            "name": item[1],
            "phone": item[2],
            "email": item[3]
        }

    return response_final


@router.get("/contacts/{id}", response_model=Contact)
async def read_one(id: int):

    result = await ContactSevices.get_one_contacts(id)

    response_final = []

    for item in result:
        response_final = {
            "id": item[0],
            "name": item[1],
            "phone": item[2],
            "email": item[3]
        }

    return response_final


@router.post("/contacts")
async def create_contact(contact: Contact):

    await ContactSevices.post_contacts(contact)

    return {f"Sucess Created"}


@router.delete("/contacts/{id}")
async def delete_contact(id: int):

    await ContactSevices.delete_contact(id)
    
    return {f"Sucess : Deleted"}


@router.put("/contacts/{id}")
async def update_contact(contact: Contact, id: int):

    await ContactSevices.update_contact(
        contact, id)

    return {f"Sucess Updated"}
