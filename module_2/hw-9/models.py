from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey, String, Text, Table
from sqlalchemy.orm import relationship, backref

from conn_db import Base


class Contacts(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)
    birth_date = Column(Date)

    def __init__(self, name, surname, birth_date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def __repr__(self):
        return f'{self.name}_{self.surname}'
