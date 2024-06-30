from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Contact(BaseModel):
    id: Optional[int] = Field(None, alias="id")
    name: str
    phone: str
    email: EmailStr
