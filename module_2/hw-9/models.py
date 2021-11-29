from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey, String, Text, Table
from sqlalchemy.orm import relationship, backref

engine = create_engine('postgresql+psycopg2://'
                       'postgres:hellga1408@smartbot.ci4kh2fdklto.eu-west-3.rds.amazonaws.com:5432/NoteBook')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(Date)
    phone_id = Column(Integer, ForeignKey('phone.id'))
    phone = relationship("Phone", backref="contact")
    email_id = Column(Integer, ForeignKey('email.id'))
    email = relationship("Email", backref="contact")
    address_id = Column(Integer, ForeignKey('address.id'))
    address = relationship("Address", backref="contact")

    def __init__(self, first_name, last_name, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'


class Phone(Base):
    __tablename__ = "phone"
    id = Column(Integer, primary_key=True)
    phone = Column(String)

    def __init__(self, phone):
        self.phone = phone

    def __repr__(self):
        return f'{self.phone}'


class Email(Base):
    __tablename__ = "email"
    id = Column(Integer, primary_key=True)
    email = Column(String)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return f'{self.email}'


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    address = Column(Text)

    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return f'{self.address}'
