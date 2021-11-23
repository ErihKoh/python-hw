from sqlalchemy import Column, Integer, Date, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://'
                       'postgres:hellga1408@smartbot.ci4kh2fdklto.eu-west-3.rds.amazonaws.com:5432/NoteBook')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)
    birthday = Column(Date)

    def __init__(self, name, phone, email, address, birthday):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthdate = birthday

    def __repr__(self):
        return f'{self.name}_{self.id}'


class Note(Base):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True)
    name_note = Column(String)
    tags = Column(String)
    text_note = Column(String)

    def __init__(self, name_note, tags, text_note):
        self.name_note = name_note
        self.tagas = tags
        self.text_note = text_note

    def __repr__(self):
        return f'{self.name_note}_{self.id}'
