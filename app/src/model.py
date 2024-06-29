from sqlalchemy import create_engine, Column, Integer, String, Sequence
from app.src.postgres import Base


# Definir a classe da tabela
class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, Sequence('contact_id_seq'), primary_key=True)
    name = Column(String(70), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)


