from mongo import client


def main(data_base):
    contacts = data_base.contacts.find()
    for contact in contacts:
        full_name = contact['name'] + ' ' + contact['surname']
        print(f"{full_name}, phone: {contact['phone']}, email: {contact['email']}")


if __name__ == '__main__':
    with client:
        db = client.addressbookdb
        main(db)
