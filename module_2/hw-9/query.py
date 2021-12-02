from sqlalchemy import select
from models import Session, Contact, Phone, Email, Address


def show_all_contacts():
    with Session() as session:
        contacts = session.query(Contact).all()
        for i in contacts:
            print(i)


def show_one_phone():
    last_name = input("Enter last_name: ")
    with Session() as session:
        result = session.query(Contact, Phone).join(Address).filter(Contact.last_name == last_name).one()
        print(f"Contact: {result[0]},\nPhone: {result[1]}")


def show_one_email():
    last_name = input("Enter last_name: ")
    with Session() as session:
        result = session.query(Contact, Email).join(Email).filter(Contact.last_name == last_name).one()
        print(f"Contact: {result[0]},\nEmail: {result[1]}")


def show_one_address():
    last_name = input("Enter last_name: ")
    with Session() as session:
        result = session.query(Contact, Address).join(Address).filter(Contact.last_name == last_name).one()
        print(f"Name: {result[0]},\nAddress: {result[1]}")


if __name__ == '__main__':
    show_all_contacts()
    show_one_address()
