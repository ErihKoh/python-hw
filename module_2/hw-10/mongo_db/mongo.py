from pymongo import MongoClient
from faker import Faker


client = MongoClient(
    'mongodb+srv://hellga:hellga1408@cluster0.tkgwl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
fake = Faker()

contacts = [
    {'name': fake.first_name(), 'surname': fake.last_name(),
     'phone': fake.phone_number(), 'birth_date': f'{fake.date_of_birth()}',
     'email': fake.ascii_free_email(), 'address': fake.city() + ' ' + fake.street_address() + ' ' + fake.postcode()},
    {'name': fake.first_name(), 'surname': fake.last_name(),
     'phone': fake.phone_number(), 'birth_date': f'{fake.date_of_birth()}',
     'email': fake.ascii_free_email(), 'address': fake.city() + ' ' + fake.street_address() + ' ' + fake.postcode()},
    {'name': fake.first_name(), 'surname': fake.last_name(),
     'phone': fake.phone_number(), 'birth_date': f'{fake.date_of_birth()}',
     'email': fake.ascii_free_email(), 'address': fake.city() + ' ' + fake.street_address() + ' ' + fake.postcode()},
    {'name': fake.first_name(), 'surname': fake.last_name(),
     'phone': fake.phone_number(), 'birth_date': f'{fake.date_of_birth()}',
     'email': fake.ascii_free_email(), 'address': fake.city() + ' ' + fake.street_address() + ' ' + fake.postcode()},
    {'name': fake.first_name(), 'surname': fake.last_name(),
     'phone': fake.phone_number(), 'birth_date': f'{fake.date_of_birth()}',
     'email': fake.ascii_free_email(), 'address': fake.city() + ' ' + fake.street_address() + ' ' + fake.postcode()},
]

if __name__ == '__main__':
    with client:
        db = client.addressbookdb
        db.contacts.insert_many(contacts)

