import json
from abc import abstractmethod, ABC
from collections import UserDict
import re
from datetime import datetime

# class AbstractAssistant(ABC):
#
#     @abstractmethod
#     def add_record(self, record, records):
#         pass
#
#     @abstractmethod
#     def remove_record(self, record, records):
#         pass
#
#     @abstractmethod
#     def change_record(self):
#         pass
#
#     @abstractmethod
#     def show_records(self):
#         pass

records = []


class AddressBook:
    def __init__(self):
        pass

    def add_record(self, record):
        records.append(record)
        print(records)

    def edit_record(self, record, new_record):
        pass

    def show_record(self, record):
        pass

    def show_all(self):
        pass

    def delete_record(self, record):
        pass


# class NoteBook(Assistant):
#     def __init__(self, record):
#         super().__init__(record)


class Record:
    def __init__(self, name, phone, address, birthday, email):
        self._name = name
        self._phone = phone
        self._address = address
        self._birthday = birthday
        self._email = email
        self.record = dict()

    def create(self):
        self.record['name'] = self._name.value
        self.record['phone'] = self._phone.value
        self.record['address'] = self._address.value
        self.record['birthday'] = self._birthday.value
        self.record['email'] = self._email.value
        return self.record

    @property
    def value(self):
        return self.record

    @value.setter
    def value(self, record):
        self.record = record


class Name:
    def __init__(self, name):
        self._name = name

    @property
    def value(self):
        return self._name

    @value.setter
    def value(self, name):
        self._name = name

    def __str__(self):
        return f"{self.__class__.__name__}: {self._name}"


class Phone:
    def __init__(self, phone):
        self._phone = phone

    @property
    def value(self):
        return self._phone

    @value.setter
    def value(self, phone):
        self._phone = phone

    def __str__(self):
        return f"{self.__class__.__name__}: {self._phone}"


class Address:
    def __init__(self, address):
        self._address = address

    @property
    def value(self):
        return self._address

    @value.setter
    def value(self, address):
        self._address = address

    def __str__(self):
        return f"{self.__class__.__name__}: {self._address}"


class Email:
    def __init__(self, email):
        self._email = email

    @property
    def value(self):
        return self._email

    @value.setter
    def value(self, email):
        self._email = email

    def __str__(self):
        return f"{self.__class__.__name__}: {self._email}"


class Birthday:
    def __init__(self, birthday):
        self._birthday = birthday

    @property
    def value(self):
        return self._birthday

    @value.setter
    def value(self, birthday):
        self._birthday = birthday

    def __str__(self):
        return f"{self.__class__.__name__}: {self._birthday}"


if __name__ == "__main__":
    # ab = Assistant()
    # ab.add_record('address')
    # ab.add_record('phones')

    file = 'D:\Admin\GitHub\Python\python-hw\module_2\hw-2\smartbot\jfile.json'

    rec = Record(Name('Yurii'))
    rec.create_record()

    name = Name('Yurii').value

    print(name)

    # with open(file, 'w') as fh:
    #     json.dump(rec, fh)
