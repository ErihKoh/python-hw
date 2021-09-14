from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record.phones.value


class Record:

    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, phone, new_phone):
        self.remove_phone(phone)
        self.add_phone(new_phone)


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, name, value):
        super().__init__(value)
        self.value = name


class Phone(Field):
    def __init__(self, phone, value):
        super().__init__(value)
        self.value = phone
