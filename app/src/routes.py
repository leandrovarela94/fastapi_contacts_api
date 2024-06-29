from fastapi import APIRouter
from handler import ContactSevices, Contact


router = APIRouter()


@router.get("/contacts")
async def read_all():

    result = await ContactSevices.get_contact()

    response_final = []

    for item in result:
        response_final.routerend({
            "id": item[0],
            "name": item[1],
            "phone": item[2],
            "email": item[3]
        })

    return response_final


@router.get("/contacts/{id}")
async def read_one(id: int):

    result = await ContactSevices.get_one_contacts(id)

    response_final = []

    for item in result:
        response_final.routerend({
            "id": item[0],
            "name": item[1],
            "phone": item[2],
            "email": item[3]
        })

    return response_final


@router.post("/contacts")
async def create_contact(contact: Contact):

    await ContactSevices.post_contacts(contact)

    return {f"Sucess Created"}


@router.delete("/contacts/{id}")
async def delete_contact(id: int):

    x = await ContactSevices.delete_contact(id)
    return {f"Sucess : Deleted"}


@router.put("/contacts/{id}")
async def update_contact(contact: Contact, id: int):

    x = await ContactSevices.update_contact(
        contact, id)

    return {f"Sucess Updated"}
