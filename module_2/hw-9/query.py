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
        result = session.query(Contact, Phone).filter(Contact.last_name == last_name) \
            .filter(Contact.phone_id == Phone.id).one()
        print(f"Contact: {result[0]}, phone: {result[1]}")


def show_one_email():
    last_name = input("Enter last_name: ")
    with Session() as session:
        result = session.query(Contact, Email).filter(Contact.last_name == last_name) \
            .filter(Contact.email_id == Email.id).one()
        print(f"Contact: {result[0]}, phone: {result[1]}")


def show_one_address():
    last_name = input("Enter last_name: ")
    with Session() as session:
        result = session.query(Contact).filter(Contact.last_name == last_name).join(Address.id).one()
        print(f"Contact: {result[0]}, phone: {result[1]}")


if __name__ == '__main__':
    # show_all_contacts()

    show_one_address()